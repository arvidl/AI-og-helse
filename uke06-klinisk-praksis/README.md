# Uke 6: Klinisk praksis

## Læringsmål

Etter denne uken skal du kunne:

- bygge en enkel risikomodell med logistisk regresjon
- forstå hvorfor kalibrering er viktig i kliniske prediksjonsmodeller
- tolke ROC-kurve og andre grunnleggende evalueringsmål
- bruke SHAP til å forklare modellprediksjoner
- forklare hvordan terskelvalg påvirker kliniske beslutninger
- forstå hvorfor validering, generalisering og subgruppeanalyse er viktig
- reflektere over hva som kreves for å ta en modell inn i klinisk arbeidsflyt

## Innhold

### Notebooks
1. **[01_risikomodell_logistisk_regresjon_kalibrering_shap.ipynb](01_risikomodell_logistisk_regresjon_kalibrering_shap.ipynb)** - syntetisk risikomodell med trening, kalibrering, evaluering og forklarbarhet
2. **[02_klinisk_beslutningsstøtte_terskler_og_avveininger.ipynb](02_klinisk_beslutningsstøtte_terskler_og_avveininger.ipynb)** - hvordan risikoskår blir til beslutningsstøtte i praksis
3. **[03_validering_generalisering_og_subgrupper.ipynb](03_validering_generalisering_og_subgrupper.ipynb)** - hvorfor modeller må testes utover eget utviklingsmiljø
4. **[04_fra_modell_til_klinisk_arbeidsflyt.ipynb](04_fra_modell_til_klinisk_arbeidsflyt.ipynb)** - hva som kreves før en modell kan brukes i klinisk drift

## Hva ukens notebooks dekker

- syntetiske kliniske data for en enkel prediksjonsoppgave
- logistisk regresjon som baseline-modell
- kalibreringskurve og ROC-kurve
- SHAP for globale og lokale modellforklaringer
- terskelvalg og avveining mellom falske positive og falske negative
- intern versus ekstern validering og distribusjonsskifte
- subgruppeanalyse og generaliserbarhet
- koblingen mellom modell, kliniker og klinisk arbeidsflyt

## Arbeidsmåte

1. Kjør notebookene i rekkefølge fra topp til bunn.
2. Start med å forstå modellen i `01`, og gå deretter videre til hvordan den brukes i beslutninger i `02`.
3. Bruk `03` til å vurdere hvor robust modellen er når pasientgrunnlag og kontekst endrer seg.
4. Avslutt med `04` for å se hva som skal til for å ta modellen inn i faktisk klinisk praksis.

## Refleksjon

Vurder hvordan en modell kan være både nyttig og problematisk i klinisk praksis. Spør ikke bare om modellen virker, men også hvem den virker for, når den bør brukes, og hvilke krav som må oppfylles for at den skal brukes forsvarlig.

## Videre

Denne uken bygger på tidligere arbeid med maskinlæring, men flytter oppmerksomheten fra selve modellen til hvordan prediksjoner brukes i kliniske situasjoner.

Neste uke, [Uke 7 - Velferdsteknologi](../uke07-velferdsteknologi/), utvider perspektivet til teknologi i hjem, omsorg og samspill med brukere. Etter det samles de etiske, juridiske og implementeringsnære spørsmålene i [Uke 8 - Etikk og implementering](../uke08-etikk-implementering/).
