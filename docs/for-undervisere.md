# For undervisere

Denne siden er en kort, redigerbar tekstversjon av underviserstoffet på
kursportalen. Bruk den når du vil planlegge undervisning, dele et opplegg i
e-post/LMS eller gjøre endringer som er enklere å lese i GitHub-diff.

Den publiserte portalsiden finnes her:
[For undervisere](https://arvidl.github.io/AI-og-helse/for-undervisere.html).

## Bruksmåter

Kurset kan brukes på flere nivåer:

- Som komplett kursløp: bruk uke 1-8 som en gradvis progresjon fra begreper og
  modellforståelse til klinisk anvendelse, etikk og implementering.
- Som modulbasert undervisning: velg ut enkelte uker, for eksempel generativ AI,
  klinisk praksis eller etikk, og bruk dem som egne temaøkter.
- Som refleksjonsgrunnlag: bruk README-er og utvalgte notebooks som felles
  utgangspunkt for diskusjon, refleksjon og faglig orientering.

## Anbefalt oppstart

For første gjennomføring:

1. Start med kursforsiden og `Start her` for å velge riktig inngang for
   målgruppen.
2. Bruk `Uke 1` som felles introduksjon hvis deltakerne har ulik bakgrunn.
3. Velg temauker etter formål: `Uke 4` for generativ AI, `Uke 6` for klinisk
   praksis, `Uke 8` for etikk og innføring.

Mange deltakere vil ha godt utbytte av å lese og diskutere materialet uten å
kjøre all kode selv. Notebookene kan derfor brukes både som interaktive øvelser
og som lesbare fagtekster.

## Undervisningspakker

### 2 timer: rask faglig introduksjon

Bruk forsiden, `Uke 1` for begreper og ett valgt eksempel fra `Uke 4` eller
`Uke 6`. Avslutt med korte refleksjonsspørsmål om nytte, risiko og ansvar.

### Halvdag: fra begrep til case

Start med `Uke 1`, la deltakerne prøve én Colab-notebook fra `Uke 4` eller
`Uke 5`, og bruk `Uke 6` til å diskutere validering, terskler og klinisk
arbeidsflyt.

### Heldag: fra teknologi til innføring

Kombiner `Uke 4-5` for moderne AI og agenter, `Uke 6-7` for praksis og
tjenesteflyt, og `Uke 8` for personvern, regulering, bias og trustworthy AI.

## Evaluering etter pilot

Etter første bruk er det mer nyttig å spørre hvor deltakerne stoppet opp enn om
de likte kurset generelt. Be dem beskrive konkrete problemer, venting og uklare
instruksjoner.

Spør særlig:

- Hvilken side eller notebook forstod du ikke?
- Hvor måtte du vente, og hva ventet du på?
- Hvilken instruks var uklar eller vanskelig å følge?
- Hva ville du trengt mer støtte til som helsepersonell eller student?

Sorter funnene i tre nivåer:

- Må fikses før neste gjennomføring
- Bør forbedres
- Ideer til senere

Små rettelser kan gjøres fortløpende på `main`, mens større endringer kan
samles i en ny stabil kursversjon.

## Teknisk gjennomføring

Alle kursnotebooks har en felles Colab-konvensjon øverst: en informasjonscelle
med runtime, kjøretid og krav, etterfulgt av en setup-celle som håndterer
miljødeteksjon og notebook-spesifikke avhengigheter.

For kursansvarlige:

- Be deltakere bruke Colab Secrets for API-nøkler via `userdata.get(...)`.
- Ved lokal kjøring anbefales `uv` og `.env`.
- Conda er primært relevant for CUDA/NVIDIA.

## Temaspenn

- Orientering i feltet: start med `Uke 1` og `Uke 2` for felles språk rundt AI,
  maskinlæring og evaluering.
- Aktuell teknologiforståelse: bruk `Uke 4` og `Uke 5` for språkmodeller,
  generativ AI og agentiske systemer.
- Klinisk relevans: velg `Uke 6` og `Uke 7` for beslutningsstøtte,
  velferdsteknologi og praktisk bruk i helse og omsorg.
- Ansvarlig innføring: bruk `Uke 8` for personvern, regulering, bias, medisinsk
  etikk og trustworthy AI.
