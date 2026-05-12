# Uke 8: Etikk og implementering

> *"Med stor kraft følger stort ansvar"* - Spider-Man (og AI-utviklere)

Denne uken handler om hvordan AI kan brukes ansvarlig, lovlig og faglig forsvarlig i helse og medisin. Fokus er på fem temaer som bygger på hverandre: personvern, rettferdighet, regulering, medisinsk etikk og trustworthy AI.

Se også Helsedirektoratets rapport: ["Utvikling og bruk av kunstig intelligens"](https://www.helsedirektoratet.no/rapporter/status-og-forslag-til-videre-arbeid-med-kunstig-intelligens-ki-i-helse-og-omsorgstjenesten/utvikling-og-bruk-av-kunstig-intelligens)

Alle eksemplene bruker syntetiske eller innebygde data og kan kjøres uten API-nøkkel, GPU eller eksterne datafiler, både lokalt og i Google Colab.

## Bro fra uke 04-07

Uke 04-07 bygget en kjede fra generativ AI og API-er, via agentiske systemer, til klinisk validering og velferdsteknologi i praksis. Uke 08 samler denne kjeden i spørsmålet: Hva må være på plass for at slike systemer kan brukes ansvarlig?

Det betyr at vi ikke bare vurderer modellscore eller teknisk funksjonalitet. Vi vurderer også personvern, samtykke, dataminimering, bias og rettferdighet, regulering, dokumentasjon, menneskelig kontroll, ansvar, monitorering og mulighet til å stoppe eller endre systemet når det ikke fungerer som det skal.

## Læringsmål

Etter denne uken skal du kunne:

- forstå sentrale personvernkrav for AI i helse
- identifisere og diskutere bias og rettferdighet i algoritmiske systemer
- kjenne hovedtrekkene i CE-merking, MDR og EU-regulering av medisinsk AI
- anvende medisinsk-etiske prinsipper på klinisk bruk av AI
- forklare hva som gjør et AI-system tillitsverdig i helsetjenesten
- reflektere over implementering, risiko og ansvar i praksis

## Ukens notebooks

### `01_gdpr_personvern.ipynb`

Temaer:

- GDPR og personvern i AI-prosjekter
- anonymisering og pseudonymisering
- dataminimering og informasjonsplikt
- praktiske vurderinger ved bruk av helseopplysninger

### `02_bias_rettferdighet.ipynb`

Temaer:

- hva bias er i datasett og modeller
- fairness-begreper og typiske avveininger
- eksempler på utilsiktet diskriminering
- refleksjon rundt måling, evaluering og tiltak

Anbefalt lesemåte: bruk introduksjon, bias-typologi, fairness-metrikker og oppsummering som kjerne. De praktiske eksperimentene og utfordringsdelen kan brukes som fordypning eller øvelse dersom du har tid.

### `03_ce_mdr_regulering.ipynb`

Temaer:

- når AI kan regnes som medisinsk utstyr
- CE-merking og MDR
- risikoklassifisering
- ansvar og dokumentasjon ved innføring av AI-systemer

Anbefalt lesemåte: bruk oversikten over CE-merking, MDR/SaMD, AI Act og oppsummeringen som kjerne. Generatorer, dashbord og case-øvelser kan leses som fordypning eller praktisk øvelse.

### `04_ai_etikk_i_medisinen.ipynb`

Temaer:

- de fire medisinsk-etiske prinsippene anvendt på AI i helse
- kliniske dilemmaer ved bruk av beslutningsstøtte
- sammenhengen mellom bias, personvern og ansvar
- en enkel etisk sjekkliste for vurdering av AI-systemer

### `05_trustworthy_ai_i_helse.ipynb`

Temaer:

- hva trustworthy AI betyr i helsekontekst
- robusthet, distribusjonsskifte og usikkerhet
- human-in-the-loop og klinisk kontroll
- validering, monitorering og trygg innføring i praksis

## Arbeidsmåte

1. Start med `01_gdpr_personvern.ipynb`.
2. Fortsett med `02_bias_rettferdighet.ipynb`.
3. Gå videre til `03_ce_mdr_regulering.ipynb`.
4. Les deretter `04_ai_etikk_i_medisinen.ipynb` for å samle de etiske linjene.
5. Avslutt med `05_trustworthy_ai_i_helse.ipynb`.
6. Bruk gjerne `uke08-innhold.md` som støttefil dersom du vil ha en supplerende oversikt.

## Praktiske tips

- Les notebookene i rolig tempo og noter egne refleksjoner underveis.
- Diskuter gjerne case med medstudenter, kolleger eller en AI-sparringspartner.
- Koble stoffet til konkrete helsefaglige situasjoner: journalsystemer, triage, beslutningsstøtte, bildeanalyse og pasientkommunikasjon.

## Sluttsjekk for ansvarlig implementering

Før du omtaler en AI-løsning som klar for bruk i helse eller omsorg, bør du kunne svare kort på:

1. Hvilke data brukes, og er dataminimering, rettslig grunnlag og informasjonsplikt vurdert?
2. Hvilke grupper kan rammes av bias, lavere ytelse eller ulik nytte?
3. Kan systemet regnes som medisinsk utstyr eller høyrisiko-AI?
4. Hvem har ansvar for bruk, overstyring, feil, avvik og endringer?
5. Hvordan valideres, monitoreres, re-evalueres og eventuelt stoppes systemet?

## Få hjelp

- Se juridiske og faglige lenker i notebookene.
- Bruk [GitHub Issues](https://github.com/arvidl/AI-og-helse/issues) for å melde fra om feil eller utdaterte lenker.
- Ved spørsmål om oppsett og kjøring: se toppnivå-`README.md`.

---

Start med `01_gdpr_personvern.ipynb` og jobb deg videre mot `05_trustworthy_ai_i_helse.ipynb`.