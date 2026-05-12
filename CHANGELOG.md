# Changelog

## v2026.05-course-ready - 2026-05-12

This release marks a course-ready snapshot of `AI og Helse` for public use,
teaching preparation and further pilot testing.

### Highlights

- Quality-assured weeks 04-08 and strengthened the course progression from
  generative AI to agentic systems, clinical practice, welfare technology and
  responsible implementation.
- Added a course roadmap in the root `README.md` and aligned the GitHub Pages
  course portal with the repository.
- Updated Colab and README documentation for notebook structure, API key usage,
  local setup, Gemini/OpenAI/Anthropic support and representative smoke checks.
- Populated shared resources with curated article and tool references for later
  course weeks.
- Added an instructor page section with 2-hour, half-day and full-day teaching
  package suggestions.
- Normalized tracked notebooks as valid `nbformat` files and reduced large
  embedded outputs in the largest week 03 notebooks.
- Tightened repository hygiene with broader ML artifact ignores and conservative
  dependency ranges for `google-genai` and `crewai`.

### Validation Snapshot

- 46 tracked notebooks validate as `nbformat`.
- Root README Colab links point to existing notebooks.
- GitHub Pages is live and aligned with the repository overview.
- Local links in `docs/*.html` validate.
- No tracked data, model or log artifacts were found with common generated-file
  extensions.

### Known Limitations

- Not every notebook has been run end-to-end in a fresh Colab runtime.
- Some heavier data notebooks still require external data, credentials, GPU or
  prepared artifacts as documented in `COLAB_COMPATIBILITY_CHECKLIST.md`.
- The course is ready for use, but should still be treated as a teaching
  material snapshot that can improve after pilot use with learners.
