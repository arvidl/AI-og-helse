# Uke 4: Generativ AI, foundation models og multimodalitet

## Larningsmal

Etter denne uken skal du kunne:

- forklare hovedideene bak transformer-arkitekturen
- forsta grunnleggende LLM-begreper som tokens, temperatur og kontekstvindu
- bruke prompt engineering for helsefaglige oppgaver
- teste enkle API-kall mot OpenAI og Anthropic pa en trygg mate
- forsta at moderne foundation models ogsa kan vaere multimodale, ikke bare tekstbaserte
- reflektere over hvordan tekst-, bilde- og multimodale modeller kan brukes i helse og medisin

## Innhold

### Notebooks
1. **[01_transformer_arkitektur.ipynb](01_transformer_arkitektur.ipynb)** - introduksjon til attention og transformers
2. **[02_llm_grunnleggende.ipynb](02_llm_grunnleggende.ipynb)** - hvordan store sprakmodeller fungerer i praksis
3. **[03_prompt_engineering.ipynb](03_prompt_engineering.ipynb)** - teknikker for bedre prompts i helsefaglige scenarier
4. **[04_chatgpt_claude_api.ipynb](04_chatgpt_claude_api.ipynb)** - enkel API-bruk, sammenligning av modeller og feilhåndtering
5. **[10_bilde_tekst_clip_zero_shot_blomster.ipynb](10_bilde_tekst_clip_zero_shot_blomster.ipynb)** - introduksjon til multimodale foundation models gjennom CLIP, bilde-tekst-likhet og zero-shot klassifikasjon

### Tilleggsressurser
- **[prompts/](prompts/)** - eksempelprompts for kliniske notater, pasientsamtaler og journalsammendrag
- **[oppgaver/prompt_workshop.ipynb](oppgaver/prompt_workshop.ipynb)** - interaktiv workshop med ovingsoppgaver

## Hva denne uken dekker

Denne uken gir en innforing i moderne AI-modeller som bygger pa transformer-arkitekturen. Fokus er forst pa sprakmodeller og generativ AI, og deretter pa hvordan samme utviklingslinje ogsa har fort til multimodale modeller som kan koble tekst og bilde.

Uken er derfor bygd opp i tre trinn:

- forst: hvordan transformere og store sprakmodeller fungerer
- deretter: hvordan slike modeller kan brukes gjennom gode prompts og API-er
- til slutt: et forste mote med multimodale foundation models gjennom CLIP

Dette gjor uke 4 til en grunnmur for resten av kurset. Uken leder videre til agentisk AI i uke 5, der slike modeller settes i arbeid gjennom verktoybruk, arbeidsflyt og helsefaglige case.

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
5. Kjor deretter `10_bilde_tekst_clip_zero_shot_blomster.ipynb` for a se hvordan moderne foundation models ogsa kan koble tekst og bilde.
6. Bruk promptfilene og workshop-notebooken til ekstra oving.

## Refleksjon

Tenk over folgende sporsmal underveis:

- Hva skiller en klassisk ML-modell fra en transformerbasert foundation model?
- Hva er forskjellen mellom a bruke en modell via prompt, via API og via et mer komplett system?
- Hvordan endres mulighetene nar modellen ikke bare behandler tekst, men ogsa kan knytte tekst til bilder?
- Hvilke helsefaglige oppgaver kan egne seg for sprakmodeller, og hvilke kan egne seg for multimodale modeller?

## Viktige merknader

- Ikke legg ekte pasientopplysninger inn i aapne LLM-tjenester.
- Flere av eksemplene kan leses og delvis provas uten API-nokler.
- Cache-filer for genererte responser er ikke en del av kursinnholdet.
- CLIP-notebooken er tatt med her fordi den gir et nyttig forste mote med multimodalitet, selv om den ikke er generativ AI i snever forstand.
- Malet denne uken er ikke a dekke alt i dybden, men a gi et solid grunnlag for videre bruk og kritisk vurdering.

## Videre

Neste uke: [Uke 5 - Agentisk AI](../uke05-agentisk-ai/)
