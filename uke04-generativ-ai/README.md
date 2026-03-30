# Uke 4: Generativ AI og store sprakmodeller

## Larningsmal

Etter denne uken skal du kunne:

- forklare hovedideene bak transformer-arkitekturen
- forsta grunnleggende LLM-begreper som tokens, temperatur og kontekstvindu
- bruke prompt engineering for helsefaglige oppgaver
- teste enkle API-kall mot OpenAI og Anthropic pa en trygg mate

## Innhold

### Notebooks
1. **[01_transformer_arkitektur.ipynb](01_transformer_arkitektur.ipynb)** - introduksjon til attention og transformers
2. **[02_llm_grunnleggende.ipynb](02_llm_grunnleggende.ipynb)** - hvordan store sprakmodeller fungerer i praksis
3. **[03_prompt_engineering.ipynb](03_prompt_engineering.ipynb)** - teknikker for bedre prompts i helsefaglige scenarier
4. **[04_chatgpt_claude_api.ipynb](04_chatgpt_claude_api.ipynb)** - enkel API-bruk, sammenligning av modeller og feilhåndtering

### Tilleggsressurser
- **[prompts/](prompts/)** - eksempelprompts for kliniske notater, pasientsamtaler og journalsammendrag
- **[oppgaver/prompt_workshop.ipynb](oppgaver/prompt_workshop.ipynb)** - interaktiv workshop med ovingsoppgaver

## Hurtigstart

```python
import os

print("OPENAI_API_KEY finnes:", bool(os.getenv("OPENAI_API_KEY")))
print("ANTHROPIC_API_KEY finnes:", bool(os.getenv("ANTHROPIC_API_KEY")))
```

Notebookene `03_prompt_engineering.ipynb` og `04_chatgpt_claude_api.ipynb` kan bruke API-nokler hvis du vil kjoere live-eksempler. Se toppnivaa-`README.md`, `COLAB_SETUP.md` og `intro_openai_anthropic.ipynb` for oppsett.

## Arbeidsmate

1. Start med `01_transformer_arkitektur.ipynb`.
2. Fortsett med `02_llm_grunnleggende.ipynb`.
3. Kjor deretter `03_prompt_engineering.ipynb`.
4. Avslutt med `04_chatgpt_claude_api.ipynb`.
5. Bruk promptfilene og workshop-notebooken til ekstra oving.

## Viktige merknader

- Ikke legg ekte pasientopplysninger inn i aapne LLM-tjenester.
- Flere av eksemplene kan leses og delvis provas uten API-nokler.
- Cache-filer for genererte responser er ikke en del av kursinnholdet.

## Videre

Neste uke: [Uke 5 - Multimodal AI](../uke05-multimodal-ai/)
