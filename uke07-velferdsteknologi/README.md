# Uke 7: Velferdsteknologi

## Læringsmål

Etter denne uken skal du kunne:

- forklare hvordan A*-søk finner en korteste vei i et rutenett
- forstå samspillet mellom heuristikk, hinder og navigasjon
- lese og eksperimentere med en enkel planleggingsalgoritme
- knytte slik teknologi til praktiske anvendelser i velferdsteknologi og robotikk
- forstå hvordan sensorer kan brukes til aktivitetstolkning og hendelsesforståelse
- diskutere hvordan beslutningsstøtte kan brukes i hjem og omsorg
- reflektere over sikkerhet, etikk og menneske-maskin-samspill i velferdsteknologiske systemer

## Innhold

### Notebooks
1. **[01_robotnavigasjon_i_rutenett_med_astar.ipynb](01_robotnavigasjon_i_rutenett_med_astar.ipynb)** - introduksjon til A*-søk med visualisering i et 2D-grid
2. **[02_sensorer_aktivitet_og_hendelsesforståelse.ipynb](02_sensorer_aktivitet_og_hendelsesforståelse.ipynb)** - hvordan enkle sensorer kan brukes til å tolke aktivitet og avvik
3. **[03_beslutningsstøtte_i_hjem_og_omsorg.ipynb](03_beslutningsstøtte_i_hjem_og_omsorg.ipynb)** - varsling, prioritering og støtte i omsorgstjenester
4. **[04_sikkerhet_etikk_og_menneske_maskin_samspill.ipynb](04_sikkerhet_etikk_og_menneske_maskin_samspill.ipynb)** - trygg bruk, personvern og etiske avveininger

## Hva ukens notebooks dekker

Uken følger en tydelig progresjon fra teknologiens grunnlag til praktisk og ansvarlig bruk: først navigasjon og robotikk, deretter sensortolkning, så beslutningsstøtte i hjem og omsorg, og til slutt sikkerhet, etikk og menneske-maskin-samspill.

Alle eksemplene bruker syntetiske eller simulerte data og kan kjøres uten API-nøkkel, GPU eller eksterne datafiler, både lokalt og i Google Colab.

- grunnideen bak graf- og rutenettbasert søk
- A*-algoritmen med 4-naboer
- demo med startpunkt, målpunkt og tilfeldige hindringer
- enkel visualisering av funnet rute
- bruk av sensorer til å observere aktivitet i et hjemmemiljø
- enkle eksempler på varsling og beslutningsstøtte
- samspillet mellom teknisk sikkerhet, brukervennlighet og etikk

## Arbeidsmåte

1. Start med `01_robotnavigasjon_i_rutenett_med_astar.ipynb` for å forstå et konkret teknologisk eksempel på hvordan et system kan orientere seg og handle i et miljø.
2. Gå deretter til `02_sensorer_aktivitet_og_hendelsesforståelse.ipynb` for å se hvordan velferdsteknologi også bygger på tolkning av signaler og observasjoner.
3. Fortsett med `03_beslutningsstøtte_i_hjem_og_omsorg.ipynb` for å se hvordan slike signaler kan omsettes til varsler, prioriteringer og støtte til ansatte.
4. Avslutt med `04_sikkerhet_etikk_og_menneske_maskin_samspill.ipynb` for å samle trådene og reflektere over trygg, ansvarlig og menneskenær bruk.

## Refleksjon

Tenk over hvordan velferdsteknologi ikke bare handler om algoritmer, men også om brukssituasjon, trygghet, verdighet og ansvar. Spør ikke bare hva teknologien kan gjøre, men også hvordan den bør brukes.

## Videre

Denne uken tar med seg idéen om beslutningsstøtte fra klinisk praksis og flytter den inn i hjem, omsorg og daglig oppfølging, der sensorer, varsler og menneske-maskin-samspill blir sentrale.

[Uke 8 - Etikk og implementering](../uke08-etikk-implementering/) bygger videre på dette ved å systematisere personvern, bias, regulering og trustworthy AI for hele kursets anvendelser.
