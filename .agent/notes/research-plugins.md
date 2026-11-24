# Research plugins / MCP connectors for the short-paper literature search

Checked 2026-11-22. Source of the professor's list: `Aula/Short_paper_guia_rubrica.pptx`,
slides 19 ("Ferramentas para a busca de literatura") and 20 ("Sugestão de como usar IA na busca de literatura").

## Professor's list → Claude integration

| Tool (slide 19) | Claude integration | Claude Code command | Access |
|---|---|---|---|
| Elicit | Official connector (claude.com/connectors/elicit) | `claude mcp add --transport http elicit https://elicit.com/api/mcp` | Pro plan or higher |
| Consensus | Official connector | `claude mcp add consensus --transport http https://mcp.consensus.app/mcp` | OAuth; a library guide reports 1000 searches/month |
| SciSpace | Official connector (claude.com/connectors/scispace) | endpoint only in a third-party listing — use the directory | not verified |
| Undermind | Connector per undermind.ai/mcp | `claude mcp add --transport http undermind https://mcp.undermind.ai/mcp` then `claude mcp login undermind` | account sign-in |
| Scite | Official connector | `claude mcp add scite --transport http https://api.scite.ai/mcp` | premium subscription (7-day trial reported) |
| Google Scholar, Web of Science, CAPES | none official | community `scholar-mcp` / `paper-search-mcp` scrape Scholar (bot-blocked often) | — |
| RePEc/IDEAS, NBER | none found | — | — |
| SSRN | `paper-search-mcp` (metadata only) | — | — |
| Connected Papers | none found | — | — |

Official plugin marketplace (`anthropics/claude-plugins-official`, 317 plugins) has none of
these; the closest is `exa` (web + academic-paper search).

## Professor's usage rules that apply whatever the tool (slides 20, 22)
- Verify every reference by DOI or Google Scholar: these tools invent or distort references and often read only the abstract.
- Read the 3-4 chosen papers in full without AI.
- Model, equilibrium and comparative statics are the group's own; AI may not define the model.
- Log each use (tool, purpose, what was verified) for the AI declaration slide (5% of the presentation grade).
