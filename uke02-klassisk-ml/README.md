# Uke 2: Klassisk maskinlæring i helse

## Læringsmål

Etter denne uken skal du kunne:

- forklare hva maskinlæring er og hvordan det skiller seg fra regelbaserte systemer
- skille mellom supervised og unsupervised learning med helsefaglige eksempler
- bygge enkle prediksjonsmodeller for medisinske problemstillinger
- tolke sentrale evalueringsmål som sensitivitet, spesifisitet og ROC-kurve
- reflektere over hvor klassisk maskinlæring kan være nyttig, og hvor den har begrensninger

## Innhold

### Notebooks
1. **[01-klassisk-ml-101.ipynb](01-klassisk-ml-101.ipynb)** - introduksjon til klassisk maskinlæring for helsepersonell
2. **[02-fra-symptom-til-diagnose.ipynb](02-fra-symptom-til-diagnose.ipynb)** - et konkret prediksjonseksempel i medisinsk kontekst

## Hva denne uken dekker

Denne uken går fra begrepsforståelse til modeller som lærer fra data. Fokus er på klassiske metoder som er enkle nok til å forstå steg for steg, men samtidig realistiske nok til å illustrere sentrale spørsmål om prediksjon, evaluering og klinisk nytte.

Uken dekker særlig:

- hvordan maskinlæring lærer mønstre fra data
- forskjellen mellom treningsdata, testdata og generalisering
- hvordan en prediksjonsmodell kan vurderes i medisinsk praksis
- hvorfor valg av evalueringsmål avhenger av klinisk kontekst

## Arbeidsmåte

1. Start med `01-klassisk-ml-101.ipynb` for å få oversikt over begreper, modelltyper og arbeidsflyt.
2. Fortsett med `02-fra-symptom-til-diagnose.ipynb` for å se hvordan slike modeller brukes i en konkret case.
3. Stopp underveis og vurder hva som faktisk er en nyttig modell, ikke bare en modell som gir høy score.
4. Bruk refleksjonsspørsmålene og eventuelle egne varianter av datasettet til å knytte stoffet til eget fagområde.

## Refleksjon

Tenk over hvordan en statistisk modell skiller seg fra klinisk skjønn. Spør ikke bare om modellen kan forutsi noe, men også hva slags feil som er akseptable, hvem som påvirkes av dem, og hvordan resultatene bør tolkes i praksis.

## Videre

[Uke 3 - Dyplæring](../uke03-dyplæring/) bygger videre på samme idé om læring fra data, men med mer fleksible modeller for bilder og komplekse mønstre. Senere i kurset vender vi tilbake til spørsmålene om klinisk nytte, implementering og ansvar i mer anvendt form.