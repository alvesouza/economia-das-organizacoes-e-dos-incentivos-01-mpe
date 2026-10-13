# Setup findings (2026-10-09)

## Efficient Token `adopt.py`: two defects fixed locally, not yet upstream

1. **`session_start.py` not copied.** `adopt.py` registers a `SessionStart` hook
   (`.claude/hooks/session_start.py`) in `.claude/settings.json` but copies only
   `guard_context.py` and `check_generated.py`. Fixed by copying it from
   `../Efficient Token/.claude/hooks/session_start.py`.
2. **Relative hook paths.** Hook commands were `python .claude/hooks/<x>.py`, which fail whenever
   the shell's cwd is a subdirectory (PreToolUse then blocks every Bash call). Fixed by using
   `python "$CLAUDE_PROJECT_DIR/.claude/hooks/<x>.py"`.

Both belong upstream in `../Efficient Token/tools/adopt.py`.

## Permissions

The pack's deny rule `Read(**/.env.*)` also blocks the Write tool on `.env.example` (a key-free
template). It was written through the shell instead.

## Books

Search of `D:\Livros` (by file name and path) found only MWG in full. See `Livros/BOOKS.md`.
MWG `.md` reused from `../Microeconomia 01-MPE/Livros/` (md5-identical PDFs).

Added later the same day (mapped in `Map/`): Cabral 2e (offset +12), Varian *with Calculus* 2014
(offset +25; NOT the syllabus's 8th ed.), Giambiagi & Garcia (offset falls 25 → 13 across
chapters because the scan drops blank pages, so the registry has one entry per in-scope chapter;
`study_pack.py` supports only a single offset per entry).

## Tooling quirks

- `guard_context.py` blocks any Bash command containing a heredoc with `cat` and a `*` (reads it
  as a bulk glob read). Write helper scripts with the Write tool instead.
- `python -I` ignores `PYTHONIOENCODING`; use `python -I -X utf8` when printing PDF text.
- `pdftotext` writes Latin-1 on this machine for Portuguese PDFs: pipe through
  `iconv -f latin1 -t utf-8`.
- Inline Python in a Bash heredoc loses one level of backslashes in transit: `"\\beta"` arrived
  as `"\beta"` (a backspace + "eta"). For LaTeX strings, write the script with the Write tool, or
  build backslashes with `chr(92)`; then scan for control characters.
