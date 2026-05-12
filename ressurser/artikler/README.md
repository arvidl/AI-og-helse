# Artikler og videre lesning

Denne siden samler korte, kuraterte innganger til stoff som er relevant for kurset. Målet er ikke å lage en komplett litteraturliste, men å gi trygge startpunkter for deltakere som vil lese litt mer.

## Uke 4: Generativ AI og multimodalitet

### Transformers og LLM-er

- **Attention Is All You Need** (Vaswani mfl., 2017) - originalartikkelen bak transformer-arkitekturen.
- **The Illustrated Transformer** (Jay Alammar) - visuelt forklart innføring i attention og transformerblokker.
- **Hugging Face Course: NLP / Transformers** - praktisk og oppdatert innføring i språkmodeller, tokenisering og bruk av modeller.

### Prompting, strukturert output og evaluering

- **OpenAI, Google og Anthropic sine prompt-guider** - nyttige for praktiske mønstre, men les dem som leverandørdokumentasjon, ikke som kliniske retningslinjer.
- **Structured outputs / JSON schema** - relevant når modellens svar skal brukes videre i en arbeidsflyt, fordi formatkrav kan valideres bedre enn fri tekst.
- **LLM-evaluering og red-teaming** - se etter kilder som diskuterer hallusinasjoner, robusthet, bias, dokumentasjon av prompts og sammenligning av modellrespons.

### Multimodalitet

- **CLIP: Learning Transferable Visual Models From Natural Language Supervision** (Radford mfl., 2021) - grunnartikkelen for CLIP.
- **Hugging Face multimodal course material** - praktiske eksempler på bilde-tekst-modeller og zero-shot klassifikasjon.

## Uke 5: Agentisk AI

### RAG, tool calling og agenter

- **Retrieval-augmented generation (RAG)** - se etter kilder som forklarer dokumentoppslag, chunking, kildegrunnlag og evaluering av svar med referanser.
- **Tool calling / function calling** - les leverandørdokumentasjon fra OpenAI, Google og Anthropic som tekniske mønstre, ikke som helsefaglige anbefalinger.
- **Agentic workflows** - prioriter nøkterne kilder som skiller mellom chatbot, fast workflow, agent og multi-agent-systemer.
- **CrewAI-dokumentasjon** - nyttig for å forstå `Agent`, `Task`, `Tool`, `Crew` og `Process`, men undervisningseksempler må fortsatt vurderes mot helsekrav.

### Evaluering og styring

- **Human-in-the-loop** - relevant for alle systemer som kan påvirke prioritering, dokumentasjon eller klinisk oppfølging.
- **Audit logs og traceability** - viktig for å forstå hvilke verktøy, kilder og mellomsteg et system brukte.
- **Red-teaming av agentiske systemer** - særlig nyttig fordi feil kan oppstå i planlegging, verktøyvalg, kildebruk og oppsummering.

## Helsefaglig lesning

- Prioriter artikler og veiledere som diskuterer validering, personvern, ansvar, dokumentasjon og menneskelig kontroll.
- For kliniske anvendelser: skill alltid mellom pedagogiske demonstrasjoner, forskningsprototyper og systemer som faktisk kan brukes i pasientbehandling.

## Lesetips

Når du vurderer en artikkel om generativ AI i helse, spør:

1. Hvilke data er modellen testet på?
2. Er resultatene validert på uavhengige data?
3. Sammenlignes modellen med relevant menneskelig eller teknisk baseline?
4. Diskuteres feil, usikkerhet og bias?
5. Er bruksområdet beslutningsstøtte, dokumentasjonsstøtte, kommunikasjon eller forskning?
