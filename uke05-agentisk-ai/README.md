# Uke 5: Agentisk AI

## Læringsmål

Etter denne uken skal du kunne:

- forklare forskjellen mellom en chatbot, en fast arbeidsflyt og en AI-agent
- forstå hvordan en språkmodell kan bruke verktøy for å løse oppgaver i flere steg
- kjenne hovedideen bak RAG, enkel minnebruk og tilstand i agentiske systemer
- diskutere helserelevante anvendelser av agentisk AI
- reflektere over grenser, risiko, personvern, logging og behov for menneskelig kontroll

## Innhold

### Notebooks
1. **[01_chatbot_workflow_agent.ipynb](01_chatbot_workflow_agent.ipynb)** - begrepsinnføring til forskjellen mellom chatbot, workflow og agent
2. **[02_agentisk_ai_i_helse.ipynb](02_agentisk_ai_i_helse.ipynb)** - agentisk AI i helsefaglige anvendelser: verktøybruk, RAG, minne, case, visualiseringer og sikkerhet

## Hurtigstart

Hvis du kommer direkte til uke 5, holder det å:

1. åpne `01_chatbot_workflow_agent.ipynb`
2. lese forklaringene og kjøre de enkle kodecellene
3. fortsette med `02_agentisk_ai_i_helse.ipynb`

Notebookene kan leses uten API-nøkler, og eksemplene er laget for å kunne forstås som pedagogiske demonstrasjoner.

## Hva denne uken dekker

Denne uken handler om hvordan moderne språkmodeller kan gå fra å være rene samtalepartnere til å bli komponenter i systemer som planlegger, bruker verktøy og utfører flere deloppgaver innenfor gitte rammer.

Målet er ikke å framstille AI-agenter som autonome kliniske beslutningstakere, men å gi en realistisk og kritisk innføring i hvordan slike systemer kan brukes som støtte i helse og omsorg.

Uken dekker særlig:

- forskjellen mellom chatbot, workflow og agent
- hvordan verktøybruk kan gjøre en modell mer nyttig
- hva RAG er, og hvorfor oppslag i dokumenter eller kunnskapsbaser kan være viktig
- hva vi mener med enkel hukommelse og tilstand i en arbeidsflyt
- hvilke typer helseoppgaver som kan egne seg for agentisk AI
- hvilke feil, risikoer og ansvarsutfordringer som følger med

## Helserelevante temaer

Agentisk AI er særlig interessant når en oppgave ikke kan løses godt med ett enkelt svar, men krever flere steg, oppslag eller strukturering underveis.

Eksempler kan være:

- journalsammendrag og strukturering av tekst
- støtte til triage og informasjonsinnhenting
- pasientkommunikasjon og omskriving til mer forståelig språk
- administrativ koordinering, dokumenthåndtering og oppgavelister
- oppslag i retningslinjer eller lokale prosedyrer

Samtidig må slike systemer alltid vurderes kritisk. I helsetjenesten er det ikke nok at en løsning virker smart eller effektiv. Den må også være faglig forsvarlig, trygg, sporbar og underlagt tydelig menneskelig kontroll.

## Arbeidsmåte

1. Start med `01_chatbot_workflow_agent.ipynb`.
2. Se spesielt etter hvordan samme oppgave kan løses ulikt av en chatbot, en fast arbeidsflyt og en agent.
3. Fortsett med `02_agentisk_ai_i_helse.ipynb`.
4. Gå gjennom helsecasene og vurder hvilke som virker realistiske og nyttige i praksis.
5. Se på visualiseringene og diskuter hvilke oppgavetyper som virker mest forsvarlige å starte med.
6. Diskuter hvilke anvendelser som kan være lav risiko, og hvilke som krever strenge rammer eller ikke bør brukes.

## Sentrale spørsmål denne uken

Underveis kan du tenke over:

- Når er en vanlig chatbot tilstrekkelig?
- Når er en fast arbeidsflyt bedre enn en fri agent?
- Når kan verktøybruk øke kvaliteten, og når øker den risikoen?
- Hvordan bør et agentisk system avgrenses dersom det brukes i helse?
- Hvem har ansvar når et system gjør feil i flere steg?
- Hvilken rolle bør mennesket ha i kontroll, godkjenning og oppfølging?

## Viktige merknader

- Ikke bruk ekte pasientopplysninger i åpne AI-tjenester.
- Agentiske systemer kan gjøre feil på flere nivåer: i planlegging, i verktøybruk, i oppsummering og i anbefalinger.
- Jo mer handlekraft et system får, desto viktigere blir logging, sporbarhet og menneskelig kontroll.
- I helse bør agentisk AI som hovedregel brukes som støtte, ikke som erstatning for faglig ansvarlig personell.
- Temaene denne uken henger tett sammen med personvern, bias, regulering og ansvar, og peker derfor videre mot uke 8.

## Forbindelse til resten av kurset

Denne uken bygger direkte på [Uke 4 - Generativ AI, foundation models og multimodalitet](../uke04-generativ-ai/).

I uke 4 lærte du hva moderne språkmodeller og multimodale modeller er, og hvordan de kan brukes gjennom prompts og API-er. I uke 5 ser vi på hvordan slike modeller kan inngå i større systemer som bruker verktøy, arbeidsflyt og strukturert samhandling.

Senere i kurset blir dette relevant når vi diskuterer:

- klinisk praksis og beslutningsstøtte
- ansvarlig innføring av AI i helsetjenesten
- personvern, bias og regulering
- konkrete grenser for hva AI bør og ikke bør brukes til

## Videre

Se også:

- [Uke 4 - Generativ AI, foundation models og multimodalitet](../uke04-generativ-ai/)
- [Uke 6 - Klinisk praksis](../uke06-klinisk-praksis/)
- [Uke 8 - Etikk og implementering](../uke08-etikk-implementering/)

Denne uken markerer et viktig skifte i kurset: fra å forstå modeller til å forstå systemer som kan bruke modeller i praksis.
