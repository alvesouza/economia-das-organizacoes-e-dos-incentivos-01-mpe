"""Scenes for aula-01-does-organization-matter. One Scene per beat.

Durations come from beats.json, extended by PAUSE_S for every [pause] the script marks:
Speechify ignores intra-clip silence, so the pauses are held frames, and explainer-compile pads
the audio. While Speechify credits are exhausted, beats.json holds durations ESTIMATED at the
rate `george` speaks (197 wpm); re-measure with fill_durations.py once audio exists.

Colour roles, fixed for the whole video and declared in plan.md:
    BLUE   the object being studied           GREY   muted: lines already past; background
    YELLOW the live line / object of attention RED    what breaks: wrong attempt, valley
    GREEN  the result that survives; the coherent jump
"""
import json

from manim import *
from video_explainer import SLOTS, Beat, Stage, axes_panel, eq, note, table, title

PAUSE_S = 2.5          # held silence per [pause] marker in script.md
FOCUS, MUTED, BROKEN, KEEP, OBJ = YELLOW, GREY, RED, GREEN, BLUE
_SECONDS, _PAUSES = None, None


def beat(scene, bid):
    """A Beat whose length is the narration plus its scripted silences."""
    global _SECONDS, _PAUSES
    if _SECONDS is None:
        data = json.loads(open("beats.json", encoding="utf-8").read())
        _SECONDS = {b["id"]: b["seconds"] for b in data["beats"]}
        _PAUSES = {b["id"]: b.get("pauses", 0) for b in data["beats"]}
    return Beat(scene, bid, beats={bid: _SECONDS[bid] + _PAUSES[bid] * PAUSE_S})


class Stack:
    """A column of equation lines on a FIXED grid: live line FOCUS, lines above MUTED.

    Carried from the Macro videos. The grid is sized once from the slot's geometry, so a line
    is never repositioned after it is placed; re-fitting the group on every line collapsed
    the spacing there and drew the last lines on top of each other.
    """

    def __init__(self, stage, size=34, rows=6, slot="main"):
        self.st, self.size, self.rows, self.slot = stage, size, rows, slot
        self.group = VGroup()
        box = SLOTS[slot]
        self.pitch = box["height"] / rows
        self.top = box["center"][1] + box["height"] / 2
        self.x = box["center"][0]

    def _place(self, line, row):
        box = SLOTS[self.slot]
        if line.width > box["width"]:
            line.scale_to_fit_width(box["width"])
        if line.height > self.pitch * 0.86:
            line.scale_to_fit_height(self.pitch * 0.86)
        return line.move_to([self.x, self.top - self.pitch * (row + 0.5), 0])

    def add(self, tex, colour=FOCUS, size=None):
        """Animations that mute the current live line and write `tex` on the next row."""
        line = eq(tex, size=size or self.size, colour=colour)
        row = len(self.group)
        if row == 0:
            self.group.add(line)
            anims = self.st.show(self.slot, self.group, fit=False)
            self._place(line, 0)
            return anims
        anims = [self.group[-1].animate.set_color(MUTED)]
        self._place(line, row)
        self.group.add(line)
        anims.append(FadeIn(line))
        return anims


# Manim's Text drops word spaces below roughly font_size 30 ("hours per car" renders as
# "hoursper car"; checked on a still, 2026-10-09). Small text is therefore built at twice
# the size and scaled down. ponytail: local workaround; the real fix belongs in the kit's
# table()/axes_panel(), which share the bug.
X2 = 2


def small(text, size, colour=WHITE):
    """Text at `size` that keeps its word spacing."""
    return Text(text, font_size=size * X2, color=colour).scale(1 / X2)


def grid(head, rows, widths, size=20, colours=None, row_height=0.62):
    """table() built at twice the size and scaled down, so cell text keeps its spaces."""
    return table(head, rows, col_widths=[w * X2 for w in widths], font_size=size * X2,
                 row_height=row_height * X2, cell_colours=colours or {}).scale(1 / X2)


def tbl(head, rows, widths, size=20, colours=None, n=None):
    """A real table; `n` reveals only the first n rows (the rest drawn empty)."""
    shown = [r if (n is None or i < n) else tuple("" for _ in r) for i, r in enumerate(rows)]
    return grid(head, shown, widths, size=size, colours=colours)


def panel(x_range, y_range, x_label, y_label, width, height):
    """axes_panel() with axis labels that keep their spaces (built here, not by the kit)."""
    ax, group = axes_panel(x_range, y_range, width=width, height=height)
    group.add(small(x_label, 20, MUTED).next_to(ax.x_axis, DOWN, buff=0.28))
    group.add(small(y_label, 20, MUTED).rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.22))
    return ax, group


# ------------------------------------------------------------------ the cube

PAYOFF = {(0, 0, 0): 10, (1, 0, 0): 6, (0, 1, 0): 8, (0, 0, 1): 9,
      (1, 1, 0): 8, (1, 0, 1): 10, (0, 1, 1): 9, (1, 1, 1): 16}
SIDE = {(0, 0, 0): LEFT, (1, 0, 0): RIGHT, (0, 1, 0): LEFT, (1, 1, 0): RIGHT,
        (0, 0, 1): LEFT, (1, 0, 1): UL,   # UL: the 000-111 diagonal passes just below this vertex
        (0, 1, 1): LEFT, (1, 1, 1): RIGHT}


def cube(payoffs=True):
    """The lattice {0,1}^3 in oblique projection: J right, T into the page, S up.

    Returns (group, dots, labels). Labels are built in place and start hidden when
    payoffs=False, so revealing them later never repositions anything.
    """
    o, ej, et, es = np.array([-2.6, -2.1, 0]), RIGHT * 3.4, np.array([1.6, 1.1, 0]), UP * 2.6
    pos = {v: o + v[0] * ej + v[1] * et + v[2] * es for v in PAYOFF}
    edges = VGroup(*[Line(pos[u], pos[v], color=MUTED, stroke_width=3)
                     for u in PAYOFF for v in PAYOFF if sum(abs(a - b) for a, b in zip(u, v)) == 1
                     and u < v])
    dots = {v: Dot(pos[v], radius=0.09, color=OBJ) for v in PAYOFF}
    labels = {v: Text(str(PAYOFF[v]), font_size=30, color=WHITE).next_to(dots[v], SIDE[v], buff=0.16)
              for v in PAYOFF}
    ford = Text("Ford", font_size=22, color=MUTED).next_to(dots[(0, 0, 0)], DOWN, buff=0.3)
    toyota = Text("Toyota", font_size=22, color=MUTED).next_to(dots[(1, 1, 1)], UP, buff=0.3)
    if not payoffs:
        for lab in labels.values():
            lab.set_opacity(0)
    group = VGroup(edges, *dots.values(), *labels.values(), ford, toyota)
    return group, dots, labels


def path(dots, order, colour=BROKEN):
    """The edge path from Ford's corner adding practices in `order` (indices into J, T, S)."""
    v, pts = [0, 0, 0], [dots[(0, 0, 0)].get_center()]
    for i in order:
        v[i] = 1
        pts.append(dots[tuple(v)].get_center())
    return VMobject(color=colour, stroke_width=7).set_points_as_corners(pts)


# ------------------------------------------------------------------ Act 0

class BeatOpen(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatOpen")
        head = ["1987", "a comparable GM plant", "NUMMI"]
        w = [4.4, 4.0, 2.6]
        r1 = ("assembly hours per car", "31", "19")
        r2 = ("defects per 100 cars", "135", "45")
        b.step(st.show("title", title("Fremont, California")), t=0.8, hold=1)
        b.step(st.show("note", note("1982: General Motors closes the plant")), t=0.7, hold=2)
        b.step(st.show("note", note("defects passed down the line; some mornings it "
                                    "could not even start")), t=0.7, hold=3)
        b.step(st.show("title", title("1984: the plant reopens as NUMMI")), t=0.8, hold=2)
        b.step(st.show("note", note("a joint venture: General Motors and Toyota")),
               t=0.7, hold=2)
        b.step(st.show("note", note("over 85% of the first workforce: the people GM had "
                                    "laid off")), t=0.7, hold=3)
        b.step(st.show("title", title("By 1987")), t=0.8, hold=1)
        b.step(st.show("main", tbl(head, [r1, r2], w, n=1)), t=1.0, hold=3)
        b.step(st.show("main", tbl(head, [r1, r2], w, colours={(0, 2): KEEP, (1, 2): KEEP})),
               t=1.0, hold=3)
        b.step(st.show("note", note("as good as Toyota's best plant in Japan")), t=0.7, hold=2)
        b.step(st.show("title", title("Same building. Same people. Same union.")),
               t=0.8, hold=3)
        b.step(st.show("note", note("GM owned half of this plant, and could walk its floor "
                                    "every day")), t=0.7, hold=3)
        b.step(st.show("title", title("If you can see it, why can't you copy it?",
                                      colour=FOCUS)), t=0.8, hold=3)
        b.step(st.show("note", note("the answer takes two lines of mathematics")),
               t=0.7, hold=2)
        b.run()


# ------------------------------------------------------------------ Act I: Ford

class BeatFordFacts(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatFordFacts")
        head = ["Ford", "before", "after"]
        w = [4.4, 3.4, 4.4]
        r1 = ("chassis assembly", "12.5 hours", "93 minutes (early 1914)")
        r2 = ("Model T price", "$850 (1908)", "$260 (mid-1920s)")
        b.step(st.show("title", title("1908: the Model T")), t=0.8, hold=1)
        b.step(st.show("note", note("launched at about 850 dollars")), t=0.7, hold=2)
        b.step(st.show("title", title("1913, Highland Park: move the work to the worker")),
               t=0.8, hold=2)
        b.step(st.show("note", note("small parts, then engines, then in August the whole "
                                    "chassis")), t=0.7, hold=3)
        b.step(st.show("main", tbl(head, [(r1[0], r1[1], ""), ("", "", "")], w)),
               t=1.0, hold=2)
        b.step(st.show("main", tbl(head, [r1, ("", "", "")], w, colours={(0, 2): FOCUS})),
               t=1.0, hold=3)
        b.step(st.show("note", note("roughly eight times less labour per chassis")),
               t=0.7, hold=3)
        b.step(st.show("main", tbl(head, [r1, r2], w, colours={(1, 2): FOCUS})),
               t=1.0, hold=3)
        b.step(st.show("note", note("less than a third of the launch price")), t=0.7, hold=3)
        b.step(st.show("title", title("A machine you buy? Or a way of organising work?")),
               t=0.8, hold=3)
        b.step(st.show("note", note("the same car, over and over; parts that fit without "
                                    "filing")), t=0.7, hold=3)
        b.step(st.show("note", note("workers who repeat one motion all day; and volume")),
               t=0.7, hold=3)
        b.step(st.show("title", title("When does a line pay at all?", colour=FOCUS)),
               t=0.8, hold=2)
        b.run()


class BeatScale(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatScale")
        s = Stack(st, size=32, rows=6, slot="right")
        ax, panel_ = panel([0, 4, 1], [0, 6, 1], "chassis per year, q", "average cost",
                           width=5.0, height=3.7)
        st.fit(panel_, "left", scale=True)
        old = ax.plot(lambda q: 0.5 / q + 2.0, x_range=[0.15, 4], color=MUTED)
        line = ax.plot(lambda q: 2.6 / q + 0.6, x_range=[0.48, 4], color=OBJ)
        lab_old = small("old way", 20, MUTED).next_to(ax.c2p(3.0, 2.17), UP, 0.12)
        lab_line = small("line", 20, OBJ).next_to(ax.c2p(3.0, 1.47), DOWN, 0.12)
        cross = DashedLine(ax.c2p(1.5, 0), ax.c2p(1.5, 3.4), color=FOCUS)
        b.step(st.show("title", title("Two ways to build a chassis")), t=0.8, hold=1)
        b.step(st.show("left", panel_, fit=False), t=0.9, hold=1)
        b.step(s.add(r"C_0(q)=F_0+c_0\,q"), t=1.0, hold=3)
        b.step(s.add(r"C_L(q)=F_L+c_L\,q,\quad F_L>F_0,\ c_L<c_0"), t=1.0, hold=3)
        b.step(s.add(r"AC_i(q)=\frac{F_i}{q}+c_i"), t=1.0, hold=2)
        b.step([Create(old), FadeIn(lab_old)], t=1.2, hold=2)
        b.step([Create(line), FadeIn(lab_line)], t=1.2, hold=3)
        b.step(s.add(r"\frac{F_L}{q}+c_L<\frac{F_0}{q}+c_0"), t=1.0, hold=3)
        b.step(s.add(r"\frac{F_L-F_0}{q}<c_0-c_L"), t=1.0, hold=3)
        b.step(s.add(r"q>\bar q\equiv\frac{F_L-F_0}{c_0-c_L}", colour=KEEP), t=1.0, hold=4)
        b.step([Create(cross)], t=0.8, hold=2)
        b.step(st.show("note", note("illustrative: about 11 labour-hours saved per chassis; "
                                    "extra fixed cost 1.1 million hours a year")),
               t=0.7, hold=3)
        b.step(st.show("right", eq(r"\bar q=\frac{1{,}095{,}000}{12.5-1.55}=100{,}000",
                                   size=34, colour=KEEP)), t=1.0, hold=3)
        b.step(st.show("title", title("The line needs volume; volume needs a cheap car; "
                                      "a cheap car needs the line")), t=0.8, hold=4)
        b.step(st.show("note", note("choices that pay only together: the class in miniature")),
               t=0.7, hold=3)
        b.run()


class BeatFiveDollar(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatFiveDollar")
        s = Stack(st, size=36, rows=5)
        head = ["Ford, labour turnover", "per year"]
        w = [6.0, 3.6]
        rows = [("1913", "370%"), ("1914", "54%"), ("1915", "16%")]
        b.step(st.show("title", title("1913: monotony, and turnover")), t=0.8, hold=1)
        b.step(st.show("main", tbl(head, rows, w, n=1, colours={(0, 1): BROKEN})),
               t=1.0, hold=3)
        b.step(st.show("note", note("for every job on the payroll, almost four hires a year")),
               t=0.7, hold=3)
        b.step(st.show("note", note("on a moving line, a missing worker holds up everyone "
                                    "downstream")), t=0.7, hold=3)
        b.step(st.show("title", title("January 1914: the five dollar day")), t=0.8, hold=2)
        b.step(st.show("note", note("roughly double the going wage; most of it a bonus "
                                    "tied to rules of conduct")), t=0.7, hold=3)
        b.step(st.show("title", title("Why would a profit maximiser pay double?")),
               t=0.8, hold=2)
        b.step(s.add(r"\min_{w}\ \frac{w}{e(w)},\qquad e'(w)>0"), t=1.0, hold=3)
        b.step(s.add(r"\frac{d}{dw}\,\frac{w}{e(w)}=\frac{e(w)-w\,e'(w)}{e(w)^2}=0"),
               t=1.0, hold=3)
        b.step(s.add(r"e(w^*)=w^*\,e'(w^*)"), t=1.0, hold=3)
        b.step(s.add(r"\frac{e'(w^*)\,w^*}{e(w^*)}=1", colour=KEEP), t=1.0, hold=3)
        b.step(st.show("note", note("the Solow condition: 1% more pay buys exactly 1% "
                                    "more effort")), t=0.7, hold=3)
        b.step(s.add(r"e(w)=\sqrt{w-w_0}\ \Rightarrow\ w^*-w_0=\tfrac{w^*}{2}"
                     r"\ \Rightarrow\ w^*=2w_0"), t=1.0, hold=3)
        b.step(st.show("note", note("an illustration, not a calibration: outside wage 2.50, "
                                    "best wage 5")), t=0.7, hold=3)
        b.step(st.show("main", tbl(head, rows, w, colours={(1, 1): KEEP, (2, 1): KEEP})),
               t=1.0, hold=3)
        b.step(st.show("note", note("Raff and Summers (1987): an efficiency wage")),
               t=0.7, hold=2)
        b.step(st.show("title", title("The line made the high wage pay: "
                                      "a first complementarity", colour=FOCUS)),
               t=0.8, hold=4)
        b.run()


class BeatFordSystem(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatFordSystem")
        head = ["design choice", "Ford"]
        w = [3.6, 7.8]
        rows = [("product", "one model: 'any colour, so long as it is black'"),
                ("machines", "dedicated: one part of one car"),
                ("process", "the moving line"),
                ("jobs", "narrow: one motion, learned in minutes"),
                ("pay", "high: the five dollar day"),
                ("parts", "made in-house, exactly to specification")]
        b.step(st.show("title", title("Ford's choices, as a system")), t=0.8, hold=1)
        b.step(st.show("note", note("an organisation: a point in a space of designs, "
                                    "one coordinate per choice")), t=0.7, hold=3)
        b.step(st.show("main", tbl(head, rows, w, n=2)), t=1.0, hold=3)
        b.step(st.show("main", tbl(head, rows, w, n=4)), t=1.0, hold=3)
        b.step(st.show("main", tbl(head, rows, w, n=6)), t=1.0, hold=3)
        b.step(st.show("title", title("Read it from the bottom up")), t=0.8, hold=2)
        b.step(st.show("main", tbl(head, rows, w, colours={(5, 1): FOCUS, (3, 1): FOCUS})),
               t=1.0, hold=3)
        b.step(st.show("main", tbl(head, rows, w, colours={(1, 1): FOCUS, (0, 1): FOCUS})),
               t=1.0, hold=3)
        b.step(st.show("main", tbl(head, rows, w, colours={(2, 1): FOCUS, (4, 1): FOCUS})),
               t=1.0, hold=3)
        b.step(st.show("note", note("three models: each set of machines at a third of "
                                    "its volume")), t=0.7, hold=3)
        b.step(st.show("note", note("the old wage: a workforce that turns over almost four "
                                    "times a year")), t=0.7, hold=3)
        b.step(st.show("title", title("A coherent system: each choice a best response to "
                                      "the others", colour=KEEP)), t=0.8, hold=3)
        b.step(st.show("note", note("built for first-time buyers who wanted any car, "
                                    "cheap. What if the question changes?")),
               t=0.7, hold=3)
        b.run()


# ------------------------------------------------------------------ Act II: GM

class BeatGMFacts(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatGMFacts")
        head = ["General Motors under Alfred Sloan", ""]
        w = [6.0, 5.6]
        rows = [("a ladder of brands, by price", "Chevrolet ... Cadillac"),
                ("'a car for every purse and purpose'", "GM's own phrase"),
                ("a new model every year", "style as a reason to buy"),
                ("1919: its own finance company", "pay in instalments")]
        b.step(st.show("title", title("By the 1920s, the question had changed")),
               t=0.8, hold=1)
        b.step(st.show("note", note("1921: the Model T alone, 55% of the US market; all GM brands together, 11%")), t=0.7, hold=3)
        b.step(st.show("note", note("more and more buyers were replacing a car, "
                                    "not buying a first one")), t=0.7, hold=3)
        b.step(st.show("note", note("a replacement buyer pays for the difference: "
                                    "comfort, power, style")), t=0.7, hold=3)
        b.step(st.show("main", tbl(head, rows, w, n=2)), t=1.0, hold=3)
        b.step(st.show("main", tbl(head, rows, w, n=3)), t=1.0, hold=2)
        b.step(st.show("main", tbl(head, rows, w, n=4)), t=1.0, hold=2)
        b.step(st.show("note", note("credit brought in buyers who could not pay at once: "
                                    "a bigger market")), t=0.7, hold=3)
        b.step(st.show("title", title("1927: Ford gives up the Model T")), t=0.8, hold=2)
        b.step(st.show("note", note("production stopped May to November, "
                                    "retooling for the Model A")), t=0.7, hold=3)
        b.step(st.show("note", note("by the end of the 1920s, GM was selling more cars "
                                    "than Ford")), t=0.7, hold=3)
        b.step(st.show("note", note("1940: GM 45%, Ford 16% (Milgrom and Roberts, p. 4)")), t=0.7, hold=3)
        b.step(st.show("title", title("Not a cheaper Model T: a different question")),
               t=0.8, hold=3)
        b.step(st.show("note", note("buyers who care about difference, and a bigger market")),
               t=0.7, hold=2)
        b.step(st.show("title", title("How many models should a firm make?",
                                      colour=FOCUS)), t=0.8, hold=2)
        b.run()


class BeatVariety(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatVariety")
        s = Stack(st, size=32, rows=7, slot="right")
        ax, panel_ = panel([1, 10, 1], [-30, 50, 10], "number of models, n",
                           "profit (illustrative)", width=5.0, height=3.7)
        st.fit(panel_, "left", scale=True)
        curve = ax.plot(lambda n: 100 * np.log(n) - 25 * n, x_range=[1, 10], color=OBJ)
        top = DashedLine(ax.c2p(4, -30), ax.c2p(4, 38.6), color=FOCUS)
        b.step(st.show("title", title("How many models? A deliberately simple model")),
               t=0.8, hold=1)
        b.step(st.show("note", note("q cars a year; n models, each with a fixed cost F")),
               t=0.7, hold=3)
        b.step(s.add(r"p(n)=\bar p+a\ln n"), t=1.0, hold=3)
        b.step(st.show("note", note("a: how much buyers care about finding the right car")),
               t=0.7, hold=3)
        b.step(s.add(r"\Pi(n)=q\,(\bar p+a\ln n-c)-nF"), t=1.0, hold=3)
        b.step(st.show("left", panel_, fit=False), t=0.9, hold=1)
        b.step([Create(curve)], t=1.2, hold=2)
        b.step(s.add(r"\Pi'(n)=\frac{qa}{n}-F"), t=1.0, hold=3)
        b.step(s.add(r"\frac{qa}{n^*}=F"), t=1.0, hold=2)
        b.step(s.add(r"n^*=\frac{aq}{F}", colour=KEEP), t=1.0, hold=3)
        b.step([Create(top)], t=0.8, hold=2)
        b.step(s.add(r"\Pi''(n)=-\frac{qa}{n^2}<0"), t=1.0, hold=3)
        b.step(s.add(r"\frac{aq}{F}\le1\Rightarrow\Pi'(1)\le0\Rightarrow n^*=1"),
               t=1.0, hold=4)
        b.step(st.show("note", note("Ford's world: a close to zero, F enormous, "
                                    "aq/F far below one")), t=0.7, hold=3)
        b.step(st.show("title", title("Ford's one model was the corner solution",
                                      colour=FOCUS)), t=0.8, hold=3)
        b.run()


class BeatVarietyStatics(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatVarietyStatics")
        s = Stack(st, size=36, rows=5)
        head = ["firm", "what moved", "n*"]
        w = [3.4, 4.4, 4.0]
        rows = [("Ford", "a near 0, F large", "1: the corner"),
                ("GM, 1920s", "a up, q up", "a ladder of brands"),
                ("Toyota, postwar", "q small, so cut F", "many, small batches")]
        b.step(st.show("title", title("Let the world move: differentiate the answer")),
               t=0.8, hold=1)
        b.step(s.add(r"\frac{\partial n^*}{\partial a}=\frac{q}{F}>0"), t=1.0, hold=3)
        b.step(s.add(r"\frac{\partial n^*}{\partial q}=\frac{a}{F}>0"), t=1.0, hold=3)
        b.step(s.add(r"\frac{\partial n^*}{\partial F}=-\frac{aq}{F^2}<0"), t=1.0, hold=3)
        b.step(s.add(r"\ln n^*=\ln a+\ln q-\ln F"), t=1.0, hold=3)
        b.step(st.show("note", note("every elasticity is one in size")), t=0.7, hold=2)
        b.step(s.add(r"a=2,\ q=50,\ F=25:\ n^*=4\qquad F=12.5:\ n^*=8"), t=1.0, hold=3)
        b.step(st.show("main", tbl(head, rows, w, n=1)), t=1.0, hold=2)
        b.step(st.show("main", tbl(head, rows, w, n=2)), t=1.0, hold=3)
        b.step(st.show("main", tbl(head, rows, w, colours={(2, 1): FOCUS})), t=1.0, hold=4)
        b.step(st.show("note", note("one formula orders three firms: Ford at the corner, "
                                    "GM rides a and q, Toyota cuts F")), t=0.7, hold=3)
        b.step(st.show("main", eq(r"\frac{\partial^2\Pi}{\partial n\,\partial a}"
                                  r"=\frac{q}{n}>0", size=50, colour=KEEP)), t=1.0, hold=4)
        b.step(st.show("note", note("a choice whose return rises with another variable: "
                                    "keep this sign")), t=0.7, hold=3)
        b.run()


def org_chart(top_text, units, width=5.4):
    """One box over a row of unit boxes, joined by lines. Text sizes keep cells legible."""
    head = VGroup(Rectangle(width=width * 0.8, height=0.9, color=OBJ),
                  small(top_text, 18))
    head[1].scale_to_fit_width(min(head[1].width, width * 0.74))
    head.move_to(UP * 1.0)
    bw = (width - 0.15 * (len(units) - 1)) / len(units)
    row = VGroup(*[VGroup(Rectangle(width=bw, height=0.7, color=MUTED),
                          small(u, 15)) for u in units])
    for box in row:
        box[1].scale_to_fit_width(min(box[1].width, bw * 0.86))
    row.arrange(RIGHT, buff=0.15).move_to(DOWN * 0.8)
    links = VGroup(*[Line(head[0].get_bottom(), box[0].get_top(), color=MUTED,
                          stroke_width=2) for box in row])
    return VGroup(head, links, row)


class BeatMForm(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatMForm")
        ford = org_chart("one operation, decisions at the top", ["plant"])
        gm = org_chart("central office: capital, targets, returns",
                       ["Chevrolet", "Oakland", "Oldsmobile", "Buick", "Cadillac"], width=6.0)
        b.step(st.show("title", title("Variety brings an organisational problem")),
               t=0.8, hold=1)
        b.step(st.show("left", ford), t=1.0, hold=2)
        b.step(st.show("note", note("one model: one thing to decide about")), t=0.7, hold=3)
        b.step(st.show("note", note("Henry Ford: the 'great big chart', where a message takes about six weeks to reach the top")), t=0.7, hold=4)
        b.step(st.show("note", note("five brands: nobody at the top can know enough about "
                                    "all of them")), t=0.7, hold=3)
        b.step(st.show("right", gm), t=1.0, hold=3)
        b.step(st.show("title", title("Decentralised operations, centralised financial "
                                      "control")), t=0.8, hold=3)
        b.step(st.show("note", note("Alfred Chandler: the multidivisional form")),
               t=0.7, hold=3)
        b.step(st.show("note", note("1927 to 1937: Ford lost $200 million; GM earned over $2 billion (M&R, p. 4)")), t=0.7, hold=3)
        b.step(st.show("title", title("n information streams: the top would absorb n, "
                                      "a division absorbs one")), t=0.8, hold=3)
        b.step([gm[0][0].animate.set_color(FOCUS)], t=0.8, hold=2)
        b.step(st.show("note", note("the centre keeps the money: every division will "
                                    "always ask for more")), t=0.7, hold=3)
        b.step(st.show("title", title("Variety and divisions are chosen together",
                                      colour=KEEP)), t=0.8, hold=3)
        b.step(st.show("note", note("GM's ladder with Ford's command: drowns in decisions")),
               t=0.7, hold=2)
        b.step(st.show("note", note("Ford's one model with GM's divisions: nothing for "
                                    "them to do")), t=0.7, hold=2)
        b.step(st.show("note", note("how to divide decisions between a centre and its "
                                    "units: Aula 7")), t=0.7, hold=2)
        b.run()


# ------------------------------------------------------------------ Act III: Toyota

class BeatToyota(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatToyota")
        head = ["Toyota practice", "through Ford's eyes"]
        w = [7.6, 4.4]
        rows = [("just in time: make what the next station asks (kanban)",
                 "any hiccup stops the line"),
                ("quick changeovers: small batches pay", ""),
                ("any worker can stop the line (andon)", "throwing away output"),
                ("multi-skilled teams that solve problems", ""),
                ("a few long-term suppliers", "at their mercy")]
        left_only = [(r[0], "") for r in rows]
        b.step(st.show("title", title("Postwar Toyota: the opposite of Ford's situation")),
               t=0.8, hold=1)
        b.step(st.show("note", note("a small market; many vehicles in small numbers; "
                                    "little capital")), t=0.7, hold=3)
        b.step(st.show("note", note("on the shop floor: Taiichi Ohno")), t=0.7, hold=2)
        b.step(st.show("main", tbl(head, left_only, w, size=19, n=1)), t=1.0, hold=3)
        b.step(st.show("main", tbl(head, left_only, w, size=19, n=2)), t=1.0, hold=2)
        b.step(st.show("main", tbl(head, left_only, w, size=19, n=3)), t=1.0, hold=3)
        b.step(st.show("note", note("a stopped line forces the cause of a defect to be "
                                    "found, not passed on")), t=0.7, hold=3)
        b.step(st.show("main", tbl(head, left_only, w, size=19, n=4)), t=1.0, hold=2)
        b.step(st.show("main", tbl(head, left_only, w, size=19)), t=1.0, hold=2)
        b.step(st.show("note", note("operators repair their own machines; Toyota redesigned twice as often as GM (M&R, p. 5)")), t=0.7, hold=4)
        b.step(st.show("title", title("Now look through Ford's eyes")), t=0.8, hold=1)
        b.step(st.show("main", tbl(head, rows, w, size=19,
                                   colours={(0, 1): BROKEN, (2, 1): BROKEN, (4, 1): BROKEN})),
               t=1.0, hold=3)
        b.step(st.show("note", note("each practice, taken alone, looks like a mistake")),
               t=0.7, hold=3)
        b.step(st.show("note", note("'so many different aspects that it was difficult to pin "
                                    "down\nwhat the crucial success factors were' "
                                    "(Cabral 2017, p. 57)")), t=0.8, hold=4)
        b.run()


class BeatTwoProblems(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatTwoProblems")
        head = ["", "coordination", "motivation"]
        w = [2.2, 5.2, 4.8]
        full = [("Ford", "the line sets the pace; one model", "the five dollar day"),
                ("GM", "centre allocates money; divisions run products",
                 "divisions judged by return on capital"),
                ("Toyota", "kanban cards pull production",
                 "teams own quality; long-term employment")]
        coord = [(r[0], r[1], "") for r in full]
        none = [(r[0], "", "") for r in full]

        def mix(k):
            return [full[i] if i < k else coord[i] for i in range(3)]

        def cmix(k):
            return [coord[i] if i < k else none[i] for i in range(3)]
        b.step(st.show("title", title("Every organisation solves two problems")),
               t=0.8, hold=1)
        b.step(st.show("note", note("coordination: the right things, at the right time, in "
                                    "the right quantities, so the pieces fit")),
               t=0.7, hold=3)
        b.step(st.show("main", tbl(head, cmix(1), w, size=18)), t=1.0, hold=3)
        b.step(st.show("main", tbl(head, cmix(2), w, size=18)), t=1.0, hold=3)
        b.step(st.show("main", tbl(head, cmix(3), w, size=18)), t=1.0, hold=3)
        b.step(st.show("note", note("motivation: people must want to do what the plan "
                                    "needs")), t=0.7, hold=3)
        b.step(st.show("main", tbl(head, mix(1), w, size=18)), t=1.0, hold=2)
        b.step(st.show("main", tbl(head, mix(2), w, size=18)), t=1.0, hold=3)
        b.step(st.show("main", tbl(head, mix(3), w, size=18)), t=1.0, hold=3)
        b.step(st.show("title", title("coordination is about information; motivation is "
                                      "about interests")), t=0.8, hold=3)
        b.step(st.show("note", note("the course: Aulas 6-8 coordination, "
                                    "Aulas 9-16 motivation")), t=0.7, hold=3)
        b.step(st.show("title", title("The two sets of choices must fit each other",
                                      colour=KEEP)), t=0.8, hold=3)
        b.step(st.show("note", note("M&R, p. 17: 'incentives and delegated authority are complements'")), t=0.7, hold=3)
        b.step(st.show("note", note("anyone may stop Toyota's line because its workers stop "
                                    "it for good reasons")), t=0.7, hold=3)
        b.run()


class BeatThreeSystems(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatThreeSystems")
        head = ["", "Ford", "GM", "Toyota"]
        w = [3.4, 2.7, 3.2, 3.2]
        rows = [("products", "one model", "a ladder of brands", "many, small batches"),
                ("machines", "dedicated", "specialised, shared parts", "flexible"),
                ("inventory", "buffers", "buffers", "almost none"),
                ("jobs", "narrow", "narrow", "broad, rotating"),
                ("who stops the line", "managers", "managers", "anyone"),
                ("suppliers", "in-house", "many, arm's length", "a few, for years")]
        b.step(st.show("title", title("Three firms, one industry")), t=0.8, hold=1)
        b.step(st.show("note", note("in broad strokes: a caricature, not an inventory")),
               t=0.7, hold=2)
        b.step(st.show("main", tbl(head, rows, w, size=18, n=1)), t=1.0, hold=2)
        b.step(st.show("main", tbl(head, rows, w, size=18, n=2)), t=1.0, hold=2)
        b.step(st.show("main", tbl(head, rows, w, size=18, n=3)), t=1.0, hold=2)
        b.step(st.show("main", tbl(head, rows, w, size=18, n=4)), t=1.0, hold=2)
        b.step(st.show("main", tbl(head, rows, w, size=18, n=5)), t=1.0, hold=2)
        b.step(st.show("main", tbl(head, rows, w, size=18)), t=1.0, hold=2)
        b.step(st.show("note", note("down a column it hangs together; across a row, three "
                                    "different answers")), t=0.7, hold=3)
        b.step(st.show("title", title("Three coherent systems, three environments: "
                                      "a, q and F")), t=0.8, hold=2)
        b.step(st.show("main", tbl(head, rows, w, size=18,
                                   colours={(i, 3): FOCUS for i in range(6)})),
               t=1.0, hold=3)
        b.step(st.show("note", note("the obvious move: adopt the best practices, "
                                    "one at a time")), t=0.7, hold=3)
        b.step(st.show("title", title("That is wrong. Let us see why", colour=BROKEN)),
               t=0.8, hold=2)
        b.run()


# ------------------------------------------------------------------ Act IV: the math of fit

class BeatWrongAttempt(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatWrongAttempt")
        s = Stack(st, size=40, rows=4)
        head = ["just in time, adopted ...", "result"]
        w = [7.2, 4.8]
        rows = [("alone: late suppliers, untrained workers", "line stops: profit falls"),
                ("with reliable suppliers and problem-solving teams",
                 "defects exposed: profit rises")]
        b.step(st.show("title", title("The assumption hiding in 'best practices'")),
               t=0.8, hold=1)
        b.step(s.add(r"x=(x_1,\dots,x_n),\qquad x_i\in\{0,1\}"), t=1.0, hold=3)
        b.step(s.add(r"\pi(x)=\pi_0+\sum_{i=1}^{n}v_i\,x_i"), t=1.0, hold=3)
        b.step(st.show("note", note("each practice adds its own value, whatever else "
                                    "the firm does")), t=0.7, hold=3)
        b.step(s.add(r"\pi(x)\big|_{x_i=1}-\pi(x)\big|_{x_i=0}=v_i"), t=1.0, hold=3)
        b.step(st.show("note", note("so adopt every positive v, in any order: "
                                    "every step pays")), t=0.7, hold=3)
        b.step(st.show("title", title("Test it: just in time at a GM plant")), t=0.8, hold=2)
        b.step(st.show("main", tbl(head, rows, w, size=19, n=1,
                                   colours={(0, 1): BROKEN})), t=1.0, hold=3)
        b.step(st.show("note", note("no buffer left to absorb a late delivery or a defect")),
               t=0.7, hold=3)
        b.step(st.show("main", tbl(head, rows, w, size=19,
                                   colours={(0, 1): BROKEN, (1, 1): KEEP})), t=1.0, hold=3)
        b.step(st.show("title", title("Same practice, two opposite values")), t=0.8, hold=3)
        b.step(st.show("main", eq(r"\pi(x)=\pi_0+\sum_{i}v_i\,x_i", size=52,
                                  colour=BROKEN)), t=1.0, hold=3)
        b.step(st.show("note", note("the mistake is not in the arithmetic: it is in the "
                                    "plus sign")), t=0.7, hold=3)
        b.run()


class BeatIncreasingDiff(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatIncreasingDiff")
        s = Stack(st, size=30, rows=6, slot="right")
        payoffs = grid(["f(x, y)", "y = 0", "y = 1"],
                       [("x = 0", "0", "-1"), ("x = 1", "-2", "5")],
                       [1.9, 1.6, 1.6], size=24, row_height=0.8, colours={(1, 2): KEEP})
        b.step(st.show("title", title("Two practices: x = just in time, y = teams")),
               t=0.8, hold=1)
        b.step(st.show("left", payoffs), t=1.0, hold=2)
        b.step(st.show("note", note("illustrative profits, measured from where the firm "
                                    "stands today")), t=0.7, hold=3)
        b.step(s.add(r"f(1,0)-f(0,0)=-2"), t=1.0, hold=3)
        b.step(s.add(r"f(1,1)-f(0,1)=5-(-1)=6"), t=1.0, hold=3)
        b.step(st.show("note", note("cross effect: 6 - (-2) = 8. In the additive world, 0")),
               t=0.7, hold=3)
        b.step(st.show("title", title("Complements: increasing differences")), t=0.8, hold=1)
        b.step(s.add(r"f(1,1)-f(0,1)\ \ge\ f(1,0)-f(0,0)"), t=1.0, hold=3)
        b.step(s.add(r"f(1,1)-f(1,0)\ \ge\ f(0,1)-f(0,0)\quad(7\ge-1)"), t=1.0, hold=3)
        b.step(st.show("note", note("complementarity is symmetric")), t=0.7, hold=2)
        b.step(s.add(r"f(1,1)+f(0,0)\ \ge\ f(1,0)+f(0,1)\quad(5\ge-3)"), t=1.0, hold=3)
        b.step(st.show("note", note("supermodularity: both plus neither beats one of each")),
               t=0.7, hold=3)
        b.step(s.add(r"f(x\vee y)+f(x\wedge y)\ \ge\ f(x)+f(y)", colour=KEEP), t=1.0, hold=3)
        b.step(st.show("title", title("Doing more of one raises the return to the other",
                                      colour=KEEP)), t=0.8, hold=3)
        b.run()


class BeatCrossPartial(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatCrossPartial")
        s = Stack(st, size=34, rows=4)
        head = ["f", "cross partial", "reading"]
        w = [2.8, 3.2, 6.0]
        rows = [("x y", "1", "complements"),
                ("x + y", "0", "additive: the wrong first attempt"),
                ("Pi(n; a)", "q / n > 0", "variety and taste: complements all along")]
        b.step(st.show("title", title("From zero-one to continuous choices")), t=0.8, hold=1)
        b.step(st.show("note", note("raise x by h and y by k, both positive")), t=0.7, hold=3)
        b.step(s.add(r"\big[f(x{+}h,y{+}k)-f(x,y{+}k)\big]-\big[f(x{+}h,y)-f(x,y)\big]"
                     r"\ \ge\ 0"), t=1.0, hold=3)
        b.step(st.show("note", note("divide by h k > 0: the inequality keeps its direction")),
               t=0.7, hold=2)
        b.step(s.add(r"\frac{1}{k}\Big[\frac{f(x{+}h,y{+}k)-f(x,y{+}k)}{h}"
                     r"-\frac{f(x{+}h,y)-f(x,y)}{h}\Big]\ \ge\ 0"), t=1.0, hold=3)
        b.step(s.add(r"h\to0:\quad\frac{f_x(x,y{+}k)-f_x(x,y)}{k}\ \ge\ 0"), t=1.0, hold=3)
        b.step(s.add(r"k\to0:\quad f_{xy}(x,y)\ \ge\ 0", colour=KEEP), t=1.0, hold=3)
        b.step(st.show("note", note("and back: a cross partial never negative integrates to "
                                    "increasing differences")), t=0.7, hold=3)
        b.step(st.show("title", title("Three checks")), t=0.8, hold=1)
        b.step(st.show("main", tbl(head, rows, w, size=20, n=1)), t=1.0, hold=2)
        b.step(st.show("main", tbl(head, rows, w, size=20, n=2,
                                   colours={(1, 2): BROKEN})), t=1.0, hold=3)
        b.step(st.show("main", tbl(head, rows, w, size=20,
                                   colours={(1, 2): BROKEN, (2, 2): KEEP})), t=1.0, hold=3)
        b.step(st.show("note", note("the sign we kept from Act Two")), t=0.7, hold=2)
        b.run()


class BeatSubstitutes(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatSubstitutes")
        s = Stack(st, size=40, rows=5)
        head = ["", "big buffers", "no buffers"]
        w = [4.6, 3.6, 3.6]
        rows = [("narrow jobs, no problem solving", "Ford: coherent", "incoherent"),
                ("teams that remove causes", "incoherent", "Toyota: coherent")]
        b.step(st.show("title", title("Not every pair is complementary")), t=0.8, hold=1)
        b.step(st.show("note", note("two ways to protect a line: inventory buffers, "
                                    "and problem solving")), t=0.7, hold=3)
        b.step(st.show("note", note("big buffers: problem solving worth little. "
                                    "No buffers: worth a lot")), t=0.7, hold=3)
        b.step(s.add(r"f_{xy}\ \le\ 0\qquad\text{(substitutes)}"), t=1.0, hold=3)
        b.step(st.show("title", title("A trick: turn one variable upside down")),
               t=0.8, hold=1)
        b.step(s.add(r"z\equiv-y"), t=1.0, hold=2)
        b.step(s.add(r"g(x,z)\equiv f(x,-z)"), t=1.0, hold=2)
        b.step(s.add(r"g_{xz}=f_{xy}\cdot\frac{d(-z)}{dz}=-f_{xy}"), t=1.0, hold=3)
        b.step(s.add(r"g_{xz}\ \ge\ 0\qquad\text{(complements)}", colour=KEEP), t=1.0, hold=3)
        b.step(st.show("note", note("everything proved for complements applies to "
                                    "substitutes")), t=0.7, hold=3)
        b.step(st.show("main", tbl(head, rows, w, size=20,
                                   colours={(0, 1): KEEP, (1, 2): KEEP,
                                            (0, 2): BROKEN, (1, 1): BROKEN})), t=1.0, hold=4)
        b.step(st.show("note", note("the mixtures are incoherent: the wrong first attempt, "
                                    "from a new angle")), t=0.7, hold=3)
        b.step(st.show("title", title("Read an organisation pair by pair", colour=KEEP)),
               t=0.8, hold=2)
        b.run()


class BeatTopkis(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatTopkis")
        s = Stack(st, size=36, rows=6)
        b.step(st.show("title", title("Why do complements move together?")), t=0.8, hold=1)
        b.step(st.show("note", note("t: a feature of the environment, not chosen by the "
                                    "firm")), t=0.7, hold=2)
        b.step(s.add(r"\max_x\ f(x,t),\qquad f_{xx}<0"), t=1.0, hold=3)
        b.step(s.add(r"f_x\big(x^*(t),\,t\big)=0\quad\text{for every }t"), t=1.0, hold=3)
        b.step(s.add(r"f_{xx}\,\frac{dx^*}{dt}+f_{xt}=0"), t=1.0, hold=3)
        b.step(s.add(r"\frac{dx^*}{dt}=-\frac{f_{xt}}{f_{xx}}"), t=1.0, hold=3)
        b.step(st.show("note", note("denominator negative: second-order condition. "
                                    "Numerator non-negative: increasing differences")),
               t=0.7, hold=3)
        b.step(s.add(r"\frac{dx^*}{dt}=-\frac{(\ge0)}{(<0)}\ \ge\ 0", colour=KEEP),
               t=1.0, hold=3)
        b.step(st.show("title", title("If the environment raises the return to x, "
                                      "x* rises")), t=0.8, hold=2)
        b.step(s.add(r"\text{variety: }\ -\frac{q/n}{-qa/n^2}=\frac{n}{a}=\frac{q}{F}"),
               t=1.0, hold=3)
        b.step(st.show("note", note("the same answer as differentiating n* = aq/F "
                                    "directly")), t=0.7, hold=2)
        b.step(st.show("title", title("Topkis (1978): no derivatives, no concavity needed")),
               t=0.8, hold=3)
        b.step(st.show("note", note("Milgrom and Roberts (1990): from mass production to "
                                    "flexible manufacturing")), t=0.7, hold=3)
        b.step(st.show("title", title("Not one practice changing: all of them, together",
                                      colour=KEEP)), t=0.8, hold=2)
        b.run()


class BeatTwoChoices(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatTwoChoices")
        s = Stack(st, size=34, rows=8)
        b.step(st.show("title", title("Two complementary choices, every line")),
               t=0.8, hold=1)
        b.step(st.show("note", note("x: flexibility, rewarded by t.  y: worker skill.  "
                                    "b > 0: the complementarity")), t=0.7, hold=3)
        b.step(s.add(r"\pi=tx+sy+bxy-\tfrac{c}{2}x^2-\tfrac{c}{2}y^2"), t=1.0, hold=3)
        b.step(s.add(r"\pi_x:\ t+by-cx=0"), t=1.0, hold=2)
        b.step(s.add(r"\pi_y:\ s+bx-cy=0"), t=1.0, hold=2)
        b.step(s.add(r"y=\frac{s+bx}{c}"), t=1.0, hold=2)
        b.step(s.add(r"t+b\,\frac{s+bx}{c}-cx=0"), t=1.0, hold=2)
        b.step(s.add(r"ct+bs+b^2x-c^2x=0"), t=1.0, hold=2)
        b.step(s.add(r"x\,(c^2-b^2)=ct+bs"), t=1.0, hold=2)
        b.step(s.add(r"x^*=\frac{ct+bs}{c^2-b^2}", colour=KEEP), t=1.0, hold=3)
        b.step(st.show("main", eq(r"y^*=\frac{s+bx^*}{c}=\frac{cs+bt}{c^2-b^2}", size=46,
                                  colour=KEEP)), t=1.0, hold=3)
        b.step(st.show("note", note("the b-squared-s terms cancel; a c comes out of the "
                                    "numerator")), t=0.7, hold=3)
        b.step(st.show("main", eq(r"H=\begin{pmatrix}-c & b\\ b & -c\end{pmatrix},\qquad"
                                  r"\det H=c^2-b^2>0\iff c>b", size=42)), t=1.0, hold=3)
        b.step(st.show("note", note("the complementarity cannot exceed the rising cost of "
                                    "each choice")), t=0.7, hold=3)
        b.step(st.show("title", title("Otherwise more of both pays forever: no optimum",
                                      colour=BROKEN)), t=0.8, hold=2)
        b.run()


class BeatMultiplier(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatMultiplier")
        s = Stack(st, size=30, rows=6, slot="right")
        ax, panel_ = panel([0, 3, 1], [0, 2.5, 0.5], "x: flexibility", "y: skill",
                           width=5.0, height=3.9)
        st.fit(panel_, "left", scale=True)
        y_br = Line(ax.c2p(0, 0.5), ax.c2p(3, 2.0), color=OBJ)            # y = (1 + x)/2
        x_old = Line(ax.c2p(0.5, 0), ax.c2p(1.75, 2.5), color=MUTED)      # x = (1 + y)/2
        x_new = Line(ax.c2p(1.5, 0), ax.c2p(2.75, 2.5), color=OBJ)        # x = (3 + y)/2
        pts, xx, yy = [ax.c2p(1, 1)], 1.0, 1.0
        for _ in range(6):
            xx = (3 + yy) / 2
            pts.append(ax.c2p(xx, yy))
            yy = (1 + xx) / 2
            pts.append(ax.c2p(xx, yy))
        stairs = VMobject(color=FOCUS, stroke_width=5).set_points_as_corners(pts)
        new_eq = Dot(ax.c2p(7 / 3, 5 / 3), radius=0.09, color=KEEP)
        b.step(st.show("title", title("Raise t, the reward to flexibility")), t=0.8, hold=1)
        b.step(s.add(r"\frac{dx^*}{dt}=\frac{c}{c^2-b^2}>0"), t=1.0, hold=3)
        b.step(s.add(r"\frac{dy^*}{dt}=\frac{b}{c^2-b^2}>0"), t=1.0, hold=3)
        b.step(st.show("note", note("t is not in y's first-order condition, and yet y "
                                    "rises")), t=0.7, hold=3)
        b.step(s.add(r"b=0:\ \frac{dx^*}{dt}=\frac{1}{c},\quad\frac{dy^*}{dt}=0"),
               t=1.0, hold=3)
        b.step(s.add(r"\frac{c/(c^2-b^2)}{1/c}=\frac{1}{1-(b/c)^2}"), t=1.0, hold=3)
        b.step(s.add(r"=1+\Big(\frac{b}{c}\Big)^2+\Big(\frac{b}{c}\Big)^4+\cdots",
                     colour=KEEP), t=1.0, hold=3)
        b.step(st.show("left", panel_, fit=False), t=0.9, hold=1)
        b.step([Create(y_br)], t=0.9, hold=2)
        b.step([Create(x_old)], t=0.9, hold=2)
        b.step([Create(x_new)], t=0.9, hold=2)
        b.step([Create(stairs)], t=2.0, hold=3)
        b.step([FadeIn(new_eq)], t=0.6, hold=2)
        b.step(s.add(r"c{=}2,\,b{=}1:\ x^*:1\to\tfrac73,\ y^*:1\to\tfrac53,\ "
                     r"\text{ratio }\tfrac43", colour=KEEP), t=1.0, hold=3)
        b.step(st.show("title", title("The ping-pong between two lines is the systems "
                                      "effect", colour=KEEP)), t=0.8, hold=3)
        b.step(st.show("note", note("M&R, ch. 4, n. 8: each increase can lead to 'another round of increases'")), t=0.7, hold=3)
        b.run()


class BeatEvidence(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatEvidence")
        s = Stack(st, size=38, rows=4)
        head = ["Ichniowski, Shaw and Prennushi (1997)", ""]
        w = [5.0, 7.4]
        rows = [("steel finishing lines", "36, owned by 17 companies"),
                ("the innovative bundle", "incentive pay, teams, flexible jobs, "
                                          "employment security, training"),
                ("bundle vs. traditional lines", "clearly more productive"),
                ("single practices in isolation", "no effect on productivity")]
        b.step(st.show("title", title("A tidy story, or true?")), t=0.8, hold=1)
        b.step(st.show("note", note("prediction one: complements are adopted together")),
               t=0.7, hold=3)
        b.step(st.show("note", note("prediction two, sharper: the interaction term")),
               t=0.7, hold=2)
        b.step(s.add(r"y=\beta_0+\beta_1x+\beta_2z+\beta_3\,xz+\varepsilon"), t=1.0, hold=3)
        b.step(s.add(r"z{=}0:\ \Delta_x y=\beta_1\qquad z{=}1:\ \Delta_x y=\beta_1+\beta_3"),
               t=1.0, hold=3)
        b.step(s.add(r"(\beta_1+\beta_3)-\beta_1=\beta_3"), t=1.0, hold=3)
        b.step(s.add(r"\text{complements: }\beta_3>0\qquad\text{additive: }\beta_3=0",
                     colour=KEEP), t=1.0, hold=3)
        b.step(st.show("title", title("Steel finishing lines")), t=0.8, hold=1)
        b.step(st.show("main", tbl(head, rows, w, size=18, n=2)), t=1.0, hold=3)
        b.step(st.show("main", tbl(head, rows, w, size=18,
                                   colours={(2, 1): KEEP, (3, 1): BROKEN})), t=1.0, hold=4)
        b.step(st.show("note", note("correlated adoption alone is no proof: a good manager "
                                    "raises the value of everything at once")),
               t=0.7, hold=4)
        b.step(st.show("title", title("The interaction term is the stronger test",
                                      colour=KEEP)), t=0.8, hold=2)
        b.run()


# ------------------------------------------------------------------ Act V: the valley

class BeatCube(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatCube")
        s = Stack(st, size=26, rows=5, slot="right")
        group, dots, labs = cube(payoffs=False)
        b.step(st.show("title", title("Three practices, adopted whole")), t=0.8, hold=1)
        b.step(st.show("left", group), t=1.0, hold=2)
        b.step(st.show("note", note("J: just in time    T: teams    S: suppliers    "
                                    "eight organisations")), t=0.7, hold=3)
        b.step(s.add(r"\pi=10-4J-2T-S+4JT+5JS+2TS+2JTS", colour=OBJ), t=1.0, hold=3)
        b.step(st.show("note", note("an illustrative index, with Ford's corner at 10")),
               t=0.7, hold=3)
        b.step([labs[(0, 0, 0)].animate.set_opacity(1)], t=0.6, hold=1)
        b.step([labs[v].animate.set_opacity(1) for v in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]],
               t=0.8, hold=2)
        b.step([labs[v].animate.set_opacity(1)
                for v in [(1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]], t=0.8, hold=3)
        b.step(st.show("title", title("Supermodular? Check J and T, line by line")),
               t=0.8, hold=1)
        b.step(s.add(r"\pi(1,1,S)-\pi(0,1,S)=(8{+}8S)-(8{+}S)=7S"), t=1.0, hold=3)
        b.step(s.add(r"\pi(1,0,S)-\pi(0,0,S)=(6{+}4S)-(10{-}S)=-4{+}5S"), t=1.0, hold=3)
        b.step(s.add(r"7S-(-4+5S)=4+2S>0"), t=1.0, hold=3)
        b.step(s.add(r"J,S:\ 5+2T>0\qquad T,S:\ 2+2J>0", colour=KEEP), t=1.0, hold=3)
        # The labels were already given an .animate target (the opacity reveal). Beat declares
        # every step before playing any, and a second .animate on the same mobject overwrites
        # the first one's target, so recolouring uses FadeToColor (target built at play time).
        b.step(st.show("title", title("Every pair complementary: supermodular")),
               t=0.8, hold=2)
        b.step([FadeToColor(labs[(1, 1, 1)], KEEP)], t=0.6, hold=2)
        b.step([FadeToColor(labs[v], BROKEN) for v in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]],
               t=0.8, hold=3)
        b.step(st.show("note", note("from Ford's corner, every first step loses: "
                                    "6, 8, 9 < 10")), t=0.7, hold=3)
        b.run()


class BeatValley(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatValley")
        group, dots, labs = cube()
        head = ["order", "profits along the path"]
        w = [1.7, 4.0]
        rows = [("J T S", "10, 6, 8, 16"), ("J S T", "10, 6, 10, 16"),
                ("T J S", "10, 8, 8, 16"), ("T S J", "10, 8, 9, 16"),
                ("S J T", "10, 9, 10, 16"), ("S T J", "10, 9, 9, 16")]
        b.step(st.show("title", title("Maybe the order matters: all six paths")),
               t=0.8, hold=1)
        b.step(st.show("left", group), t=1.0, hold=2)
        b.step(st.show("right", tbl(head, rows, w, size=20, n=2)), t=1.0, hold=3)
        b.step(st.show("right", tbl(head, rows, w, size=20, n=4)), t=1.0, hold=3)
        b.step(st.show("right", tbl(head, rows, w, size=20)), t=1.0, hold=3)
        deep, best = path(dots, [0, 1, 2]), path(dots, [2, 0, 1])
        b.step([Create(deep)], t=1.2, hold=2)
        b.step(st.show("note", note("the deepest road starts with just in time: "
                                    "down to 6, a fall of 40%")), t=0.7, hold=3)
        b.step([Create(best)], t=1.2, hold=2)
        b.step(st.show("note", note("the best road still drops to 9; every road pays "
                                    "first")), t=0.7, hold=3)
        b.step(st.show("title", title("Why: the stand-alone gain is the smallest gain")),
               t=0.8, hold=2)
        b.step(st.show("main", eq(r"\pi(x+e_i)-\pi(x)\ \ge\ \pi(e_i)-\pi(0)"
                                  r"\quad\text{for every }x\text{ with }x_i=0", size=40,
                                  colour=FOCUS)), t=1.0, hold=4)
        b.step(st.show("note", note("a firm judges its first change where every complement "
                                    "is missing")), t=0.7, hold=3)
        b.step(st.show("title", title("Complementarity does not prevent the valley: "
                                      "it creates it", colour=BROKEN)), t=0.8, hold=3)
        b.step(st.show("note", note("Topkis: choices move together. Not: the road between "
                                    "them is uphill")), t=0.7, hold=2)
        b.run()


class BeatTwoPeaks(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatTwoPeaks")
        s = Stack(st, size=30, rows=5, slot="right")
        group, dots, labs = cube()
        ford_n = [labs[v] for v in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
        toy_n = [labs[v] for v in [(0, 1, 1), (1, 0, 1), (1, 1, 0)]]
        b.step(st.show("title", title("Local and global optima")), t=0.8, hold=1)
        b.step(st.show("left", group), t=1.0, hold=1)
        b.step(s.add(r"\text{local optimum: no single change raises }\pi"), t=1.0, hold=3)
        b.step(s.add(r"N(000):\ 6,\ 8,\ 9\ <\ 10"), t=1.0, hold=2)
        b.step([lab.animate.set_color(BROKEN) for lab in ford_n], t=0.8, hold=2)
        b.step(s.add(r"N(111):\ 9,\ 10,\ 8\ <\ 16"), t=1.0, hold=2)
        b.step([labs[(1, 1, 1)].animate.set_color(KEEP)], t=0.6, hold=2)
        b.step(st.show("title", title("Two peaks on one function, a valley between")),
               t=0.8, hold=3)
        b.step(st.show("note", note("M&R, ch. 4, n. 9: a profit surface 'like a mountain with three peaks'")), t=0.7, hold=3)
        b.step(st.show("note", note("marginal analysis at a local peak: change nothing")),
               t=0.7, hold=3)
        b.step(s.add(r"\pi(111)-\pi(000)=+6", colour=KEEP), t=1.0, hold=3)
        b.step(s.add(r"\max_i\ \pi(e_i)-\pi(000)=9-10=-1", colour=BROKEN), t=1.0, hold=3)
        b.step(st.show("title", title("The package says go. Every step says stop")),
               t=0.8, hold=3)
        b.step([lab.animate.set_color(WHITE) for lab in toy_n], t=0.6, hold=1)
        b.step(st.show("note", note("why change is lumpy: a new plant, a new leader, "
                                    "a crisis")), t=0.7, hold=3)
        b.step(st.show("note", note("or a partner who brings the entire system at once")),
               t=0.7, hold=2)
        b.run()


class BeatNUMMI(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatNUMMI")
        group, dots, labs = cube()
        head = ["1987", "hours / car", "defects / 100"]
        w = [2.3, 1.8, 1.8]
        rows = [("GM plant", "31", "135"), ("NUMMI", "19", "45"), ("Takaoka", "16", "45")]
        b.step(st.show("title", title("Back to Fremont")), t=0.8, hold=1)
        b.step(st.show("note", note("the old crew: 'the worst workforce in the American car "
                                    "industry', said a union official")), t=0.7, hold=3)
        b.step(st.show("left", group), t=1.0, hold=2)
        # st.show() has just moved the cube into its slot: build on the placed vertices
        jump = Arrow(dots[(0, 0, 0)].get_center(), dots[(1, 1, 1)].get_center(),
                     buff=0.12, color=KEEP, stroke_width=7)
        reds = [path(dots, [0, 1, 2]), path(dots, [1, 0, 2])]
        b.step([GrowArrow(jump)], t=1.0, hold=3)
        b.step(st.show("note", note("Toyota brought the whole system at once: "
                                    "a jump, not a walk")), t=0.7, hold=3)
        b.step(st.show("right", tbl(head, rows, w, size=20,
                                    colours={(1, 1): KEEP, (1, 2): KEEP})), t=1.0, hold=4)
        b.step(st.show("note", note("Womack, Jones and Roos (1990), from Krafcik's plant "
                                    "study")), t=0.7, hold=2)
        b.step(st.show("title", title("GM tried to spread it, plant by plant")),
               t=0.8, hold=2)
        b.step([Create(reds[0])], t=1.0, hold=1)
        b.step([Create(reds[1])], t=1.0, hold=2)
        b.step(st.show("note", note("'largely unsuccessful': by the late 1990s, still not "
                                    "across its US plants")), t=0.7, hold=3)
        b.step(st.show("title", title("Brazil: NUMMI-trained managers, the whole system "
                                      "at once")), t=0.8, hold=3)
        b.step(st.show("note", note("NUMMI ended in 2010; GM had pulled out in 2009")),
               t=0.7, hold=2)
        b.step(st.show("title", title("Causal ambiguity is real. The cube says more",
                                      colour=FOCUS)), t=0.8, hold=3)
        b.step(st.show("note", note("even a rival who knew every factor would lose money "
                                    "adopting them one at a time")), t=0.7, hold=3)
        b.run()


class BeatClose(Scene):
    def construct(self):
        st, b = Stage(self), beat(self, "BeatClose")
        head = ["today's results", ""]
        w = [5.0, 6.6]
        rows = [("a moving line pays when", "q > (F_L - F_0) / (c_0 - c_L)"),
                ("efficiency wage", "e'(w) w / e(w) = 1"),
                ("number of models", "n* = a q / F"),
                ("complements move together", "dx*/dt = - f_xt / f_xx >= 0"),
                ("the systems multiplier", "1 / (1 - (b/c)^2)")]
        group, dots, labs = cube()
        b.step(st.show("title", title("Does organisation matter?")), t=0.8, hold=1)
        b.step(st.show("note", note("Fremont, same people: 31 vs. 19 hours per car, "
                                    "135 vs. 45 defects")), t=0.7, hold=3)
        b.step(st.show("main", tbl(head, rows, w, size=19, n=3)), t=1.0, hold=3)
        b.step(st.show("main", tbl(head, rows, w, size=19)), t=1.0, hold=3)
        b.step(st.show("title", title("1. Complements move together", colour=KEEP)),
               t=0.8, hold=3)
        b.step(st.show("title", title("2. Between two systems, the road runs through "
                                      "a valley", colour=BROKEN)), t=0.8, hold=3)
        b.step(st.show("main", group), t=1.0, hold=2)
        # built after placement, on the placed vertices
        jump = Arrow(dots[(0, 0, 0)].get_center(), dots[(1, 1, 1)].get_center(),
                     buff=0.12, color=KEEP, stroke_width=7)
        reds = [path(dots, o) for o in ([0, 1, 2], [1, 0, 2], [2, 0, 1])]
        b.step([Create(r) for r in reds], t=1.4, hold=2)
        b.step([GrowArrow(jump)], t=1.0, hold=3)
        b.step(st.show("note", note("complements move together, and the road between two "
                                    "good systems runs through a valley")), t=0.7, hold=4)
        b.step(st.show("title", title("Ask of any best practice: a complement of what?")),
               t=0.8, hold=3)
        b.step(st.show("note", note("read Milgrom and Roberts ch. 1 (pp. 2-18) and ch. 4, complementarities (pp. 108-113)")), t=0.7, hold=3)
        b.step(st.show("note", note("then Cabral 3.5; M&R Food for Thought 1-3 (p. 18); Cabral 1.1 and 3.14")), t=0.7, hold=3)
        b.step(st.show("title", title("Next: bargaining")), t=0.8, hold=2)
        b.run()
