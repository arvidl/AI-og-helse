# Forslag til innhold for uke 8

Denne filen er en intern støtteoversikt for uke 8 og er oppdatert til å samsvare med innholdet som faktisk finnes i mappen `uke08-etikk-implementering/`.

## Rolle i kursrekken

Uke 8 samler trådene fra uke 04-07:

- fra uke 04: generativ AI, API-er, strukturert output og modellfallback
- fra uke 05: agentiske arbeidsflyter, verktøybruk, logging og menneskelig kontroll
- fra uke 06: klinisk validering, terskler, subgrupper, monitorering og arbeidsflyt
- fra uke 07: sensorer, varsling, velferdsteknologi, autonomi og ansvar i hjem/omsorg

Hovedpoenget er å flytte spørsmålet fra "kan dette teknisk fungere?" til "kan dette brukes lovlig, rettferdig, regulert, etisk og tillitsverdig i praksis?".

## Hovedtemaer

- **GDPR og personvern**: juridiske krav og praktiske vurderinger
- **Bias og rettferdighet**: hvordan diskriminering kan oppstå i datasett og modeller
- **Regulering**: CE-merking, MDR og EU-regulering av medisinsk AI
- **AI-etikk i medisinen**: kliniske dilemmaer, etiske prinsipper og ansvar
- **Trustworthy AI**: robusthet, usikkerhet, validering og monitorering

## Notebooks som finnes i mappen

### `01_gdpr_personvern.ipynb`

Mulige fokusområder:

- hva som regnes som personopplysninger i AI-sammenheng
- rettslig grunnlag for behandling
- særlige kategorier personopplysninger
- anonymisering, pseudonymisering og dataminimering
- automatiserte beslutninger og forklarbarhet

### `02_bias_rettferdighet.ipynb`

Mulige fokusområder:

- historisk bias og representasjonsbias
- fairness-begreper og målemetoder
- praktiske avveininger mellom nøyaktighet og rettferdighet
- refleksjon rundt tiltak for å redusere skjevheter

### `03_ce_mdr_regulering.ipynb`

Mulige fokusområder:

- når AI kan regnes som medisinsk utstyr
- grunnleggende begreper i CE-merking og MDR
- risikoklassifisering
- dokumentasjon, ansvar og oppfølging

### `04_ai_etikk_i_medisinen.ipynb`

Mulige fokusområder:

- de fire medisinsk-etiske prinsippene anvendt på AI i helse
- kliniske dilemmaer rundt beslutningsstøtte, prioritering og pasientinformasjon
- sammenhengen mellom bias, personvern og ansvar
- bruk av en enkel etisk sjekkliste for vurdering av AI-systemer

### `05_trustworthy_ai_i_helse.ipynb`

Mulige fokusområder:

- hva som menes med trustworthy AI i helsekontekst
- distribusjonsskifte og robusthet i kliniske AI-systemer
- usikkerhet og når AI bør utløse menneskelig vurdering
- human-in-the-loop, validering og kontinuerlig monitorering

## Arbeidsmåte

- start med personvern
- fortsett med bias og rettferdighet
- gå videre til regulering
- bruk deretter AI-etikk-notebooken som syntese
- avslutt med trustworthy AI som implementeringsnær oppsummering

## Viktig merknad

Denne filen er en støtteoversikt, ikke en full læringsressurs i seg selv. For faktisk undervisningsflyt bør rekkefølgen i `README.md` og notebookene brukes som fasit.