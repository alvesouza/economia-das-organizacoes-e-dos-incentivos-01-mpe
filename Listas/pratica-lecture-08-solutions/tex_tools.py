"""LaTeX output of a bimatrix with best replies underlined, to paste into the .tex files."""
from fractions import Fraction as F


def tex_num(x):
    """LaTeX for an integer or Fraction."""
    x = F(x)
    if x.denominator == 1:
        return str(x.numerator)
    sign = "-" if x < 0 else ""
    return sign + r"\tfrac{" + str(abs(x.numerator)) + "}{" + str(x.denominator) + "}"


def latex_bimatrix(rowlab, collab, A, B):
    """tabular of the bimatrix (A, B): row player's best replies in each column and column
    player's best replies in each row are wrapped in \\br{...}."""
    R, C = len(A), len(A[0])
    colmax = [max(A[r][c] for r in range(R)) for c in range(C)]
    rowmax = [max(B[r][c] for c in range(C)) for r in range(R)]
    cl = r" \\ \cline{2-%d}" % (C + 1)
    lines = [r"\begin{tabular}{r|" + "c|" * C + "}",
             r"\multicolumn{1}{r}{} & "
             + " & ".join(r"\multicolumn{1}{c}{" + c + "}" for c in collab) + cl]
    for r in range(R):
        cells = []
        for c in range(C):
            a, b = tex_num(A[r][c]), tex_num(B[r][c])
            a = r"\br{" + a + "}" if A[r][c] == colmax[c] else a
            b = r"\br{" + b + "}" if B[r][c] == rowmax[r] else b
            cells.append("$" + a + r",\ " + b + "$")
        lines.append(rowlab[r] + " & " + " & ".join(cells) + cl)
    lines.append(r"\end{tabular}")
    return "\n".join(lines)
