# Uke 4: Generativ AI, foundation models og multimodalitet

## Læringsmål

Etter denne uken skal du kunne:

- forklare hovedideene bak transformer-arkitekturen
- forstå grunnleggende LLM-begreper som tokens, temperatur og kontekstvindu
- bruke prompt engineering for helsefaglige oppgaver
- teste enkle API-kall mot Gemini, OpenAI og Anthropic på en trygg måte
- forstå at moderne foundation models også kan være multimodale, ikke bare tekstbaserte
- reflektere over hvordan tekst-, bilde- og multimodale modeller kan brukes i helse og medisin

## Innhold

### Notebooks
1. **[01_transformer_arkitektur.ipynb](01_transformer_arkitektur.ipynb)** - introduksjon til attention og transformers
2. **[02_llm_grunnleggende.ipynb](02_llm_grunnleggende.ipynb)** - hvordan store språkmodeller fungerer i praksis
3. **[03_prompt_engineering.ipynb](03_prompt_engineering.ipynb)** - teknikker for bedre prompts i helsefaglige scenarier
4. **[04_chatgpt_claude_api.ipynb](04_chatgpt_claude_api.ipynb)** - enkel API-bruk, sammenligning av modeller og feilhåndtering
5. **[10_bilde_tekst_clip_zero_shot_blomster.ipynb](10_bilde_tekst_clip_zero_shot_blomster.ipynb)** - introduksjon til multimodale foundation models gjennom CLIP, bilde-tekst-likhet og zero-shot klassifikasjon
6. **[oppgaver/prompt_workshop.ipynb](oppgaver/prompt_workshop.ipynb)** - anvendt workshop der prompt-teknikkene fra notebook 3 øves på i korte helsefaglige oppgaver

### Tilleggsressurser
- **[prompts/](prompts/)** - eksempelprompts for kliniske notater, pasientsamtaler og journalsammendrag

## Hva denne uken dekker

Denne uken gir en innføring i moderne AI-modeller som bygger på transformer-arkitekturen. Fokus er først på språkmodeller og generativ AI, og deretter på hvordan samme utviklingslinje også har ført til multimodale modeller som kan koble tekst og bilde.

Uken er derfor bygd opp i tre trinn:

- først: hvordan transformere og store språkmodeller fungerer
- deretter: hvordan slike modeller kan brukes gjennom gode prompts og API-er
- til slutt: et første møte med multimodale foundation models gjennom CLIP

Dette gjør uke 4 til en grunnmur for resten av kurset. Uken leder videre til agentisk AI i uke 5, der slike modeller settes i arbeid gjennom verktøybruk, arbeidsflyt og helsefaglige case.

## Hurtigstart

```python
import os

print("OPENAI_API_KEY finnes:", bool(os.getenv("OPENAI_API_KEY")))
print("GEMINI_API_KEY/GOOGLE_API_KEY finnes:", bool(os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")))
print("ANTHROPIC_API_KEY finnes:", bool(os.getenv("ANTHROPIC_API_KEY")))
```

Notebookene `03_prompt_engineering.ipynb`, `04_chatgpt_claude_api.ipynb` og `oppgaver/prompt_workshop.ipynb` kan bruke API-nøkler hvis du vil kjøre live-eksempler. Uke 4 støtter særlig `GEMINI_API_KEY`/`GOOGLE_API_KEY`, `OPENAI_API_KEY` og `ANTHROPIC_API_KEY`/`CLAUDE_API_KEY`. Se toppnivå-`README.md`, `COLAB_SETUP.md` og `intro_openai_anthropic.ipynb` for oppsett.

## Arbeidsmåte

1. Start med `01_transformer_arkitektur.ipynb`.
2. Fortsett med `02_llm_grunnleggende.ipynb`.
3. Kjør deretter `03_prompt_engineering.ipynb`.
4. Avslutt med `04_chatgpt_claude_api.ipynb`.
5. Kjør deretter `10_bilde_tekst_clip_zero_shot_blomster.ipynb` for å se hvordan moderne foundation models også kan koble tekst og bilde.
6. Bruk `oppgaver/prompt_workshop.ipynb` og promptfilene til anvendt øving. Workshoppen repeterer noen tema fra notebook 3 med vilje, men som praktisk trening heller enn ny teori.

## Refleksjon

Tenk over følgende spørsmål underveis:

- Hva skiller en klassisk ML-modell fra en transformerbasert foundation model?
- Hva er forskjellen mellom å bruke en modell via prompt, via API og via et mer komplett system?
- Hvordan endres mulighetene når modellen ikke bare behandler tekst, men også kan knytte tekst til bilder?
- Hvilke helsefaglige oppgaver kan egne seg for språkmodeller, og hvilke kan egne seg for multimodale modeller?

## Viktige merknader

- Ikke legg ekte pasientopplysninger inn i åpne LLM-tjenester.
- Flere av eksemplene kan leses og delvis prøves uten API-nøkler.
- Cache-filer for genererte responser er ikke en del av kursinnholdet. Lokale cachemapper som `cache/` og `cache_api_demo/` kan slettes eller gjenskapes ved kjøring.
- CLIP-notebooken er tatt med her fordi den gir et nyttig første møte med multimodalitet, selv om den ikke er generativ AI i snever forstand.
- Målet denne uken er ikke å dekke alt i dybden, men å gi et solid grunnlag for videre bruk og kritisk vurdering.

## Videre

Neste uke: [Uke 5 - Agentisk AI](../uke05-agentisk-ai/)
