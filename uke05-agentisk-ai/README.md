# Uke 5: Agentisk AI

## Larningsmal

Etter denne uken skal du kunne:

- forklare forskjellen mellom en chatbot, en fast arbeidsflyt og en AI-agent
- forsta hvordan en sprakmodell kan bruke verktoy for a lose oppgaver i flere steg
- kjenne hovedideen bak RAG, enkel minnebruk og tilstand i agentiske systemer
- diskutere helserelevante anvendelser av agentisk AI
- reflektere over grenser, risiko, personvern, logging og behov for menneskelig kontroll

## Innhold

### Notebooks
1. **[01_chatbot_workflow_agent.ipynb](01_chatbot_workflow_agent.ipynb)** - begrepsinnforing med forskjellen mellom chatbot, workflow og agent
2. **[02_agentisk_ai_i_helse.ipynb](02_agentisk_ai_i_helse.ipynb)** - agentisk AI i helsefaglige anvendelser: verktoybruk, RAG, minne, case og sikkerhet

## Hva denne uken dekker

Denne uken handler om hvordan moderne sprakmodeller kan ga fra a vaere rene samtalepartnere til a bli komponenter i systemer som planlegger, bruker verktoy og utforer flere deloppgaver innenfor gitte rammer.

Malet er ikke a framstille AI-agenter som autonome kliniske beslutningstakere, men a gi en realistisk og kritisk innforing i hvordan slike systemer kan brukes som stotte i helse og omsorg.

Uken dekker saerlig:

- forskjellen mellom chatbot, workflow og agent
- hvordan verktoybruk kan gjore en modell mer nyttig
- hva RAG er, og hvorfor oppslag i dokumenter eller kunnskapsbaser kan vaere viktig
- hva vi mener med enkel hukommelse og tilstand i en arbeidsflyt
- hvilke typer helseoppgaver som kan egne seg for agentisk AI
- hvilke feil, risikoer og ansvarsutfordringer som folger med

## Helserelevante temaer

Agentisk AI er saerlig interessant nar en oppgave ikke kan loses godt med ett enkelt svar, men krever flere steg, oppslag eller strukturering underveis.

Eksempler kan vaere:

- journalsammendrag og strukturering av tekst
- stotte til triage og informasjonsinnhenting
- pasientkommunikasjon og omskriving til mer forstaelig sprak
- administrativ koordinering, dokumenthandtering og oppgavelister
- oppslag i retningslinjer eller lokale prosedyrer

Samtidig ma slike systemer alltid vurderes kritisk. I helsetjenesten er det ikke nok at en losning virker smart eller effektiv. Den ma ogsa vaere faglig forsvarlig, trygg, sporbar og underlagt tydelig menneskelig kontroll.

## Arbeidsmate

1. Start med `01_chatbot_workflow_agent.ipynb`.
2. Se spesielt etter hvordan samme oppgave kan loses ulikt av en chatbot, en fast arbeidsflyt og en agent.
3. Fortsett med `02_agentisk_ai_i_helse.ipynb`.
4. Ga gjennom helsecasene og vurder hvilke som virker realistiske og nyttige i praksis.
5. Diskuter hvilke anvendelser som kan vaere lav risiko, og hvilke som krever strenge rammer eller ikke bor brukes.

## Sentrale sporsmal denne uken

Underveis kan du tenke over:

- Nar er en vanlig chatbot tilstrekkelig?
- Nar er en fast arbeidsflyt bedre enn en fri agent?
- Nar kan verktoybruk oke kvaliteten, og nar oker den risikoen?
- Hvordan bor et agentisk system avgrenses dersom det brukes i helse?
- Hvem har ansvar nar et system gjor feil i flere steg?
- Hvilken rolle bor mennesket ha i kontroll, godkjenning og oppfolging?

## Viktige merknader

- Ikke bruk ekte pasientopplysninger i apne AI-tjenester.
- Agentiske systemer kan gjore feil pa flere nivaer: i planlegging, i verktoybruk, i oppsummering og i anbefalinger.
- Jo mer handlekraft et system far, desto viktigere blir logging, sporbarhet og menneskelig kontroll.
- I helse bor agentisk AI som hovedregel brukes som stotte, ikke som erstatning for faglig ansvarlig personell.
- Temaene denne uken henger tett sammen med personvern, bias, regulering og ansvar, og peker derfor videre mot uke 8.

## Forbindelse til resten av kurset

Denne uken bygger direkte pa [Uke 4 - Generativ AI, foundation models og multimodalitet](../uke04-generativ-ai/).

I uke 4 laerte du hva moderne sprakmodeller og multimodale modeller er, og hvordan de kan brukes gjennom prompts og API-er. I uke 5 ser vi pa hvordan slike modeller kan inga i storre systemer som bruker verktoy, arbeidsflyt og strukturert samhandling.

Senere i kurset blir dette relevant nar vi diskuterer:

- klinisk praksis og beslutningsstotte
- ansvarlig innforing av AI i helsetjenesten
- personvern, bias og regulering
- konkrete grenser for hva AI bor og ikke bor brukes til

## Videre

Se ogsa:

- [Uke 4 - Generativ AI, foundation models og multimodalitet](../uke04-generativ-ai/)
- [Uke 6 - Klinisk praksis](../uke06-klinisk-praksis/)
- [Uke 8 - Etikk og implementering](../uke08-etikk-implementering/)

Denne uken markerer et viktig skifte i kurset: fra a forsta modeller til a forsta systemer som kan bruke modeller i praksis.
