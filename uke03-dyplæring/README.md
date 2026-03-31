# Uke 3: Dyplæring og konvolusjonelle nevrale nettverk

## Læringsmål

Etter denne uken skal du kunne:

- forklare grunnideen bak nevrale nettverk og CNN-er
- forstå hvorfor dyplæring er særlig relevant for bilder og signaler
- følge en enkel arbeidsflyt for trening, evaluering og testing av modeller
- bruke forklarbarhetsverktøy som Grad-CAM for å undersøke modellatferd
- reflektere over forskjeller mellom naturlige og medisinske bilder i AI-arbeid

## Innhold

### Notebooks
1. **[01a_nn_intro.ipynb](01a_nn_intro.ipynb)** - grunnleggende teori om nevrale nettverk
2. **[01b_læring_i_nn.ipynb](01b_læring_i_nn.ipynb)** - læring i nevrale nettverk
3. **[01c_UCI_heart_disease_klassifikasjon.ipynb](01c_UCI_heart_disease_klassifikasjon.ipynb)** - klassifikasjon med helsedata
4. **[01d_EKG_arytmi_klassifikasjon.ipynb](01d_EKG_arytmi_klassifikasjon.ipynb)** - EKG-arytmi som eksempel på dypere modellering
5. **[02a_cnn_bildeklassifikasjon.ipynb](02a_cnn_bildeklassifikasjon.ipynb)** - oppsett, datasett og CNN-arkitektur
6. **[02b_cnn_trening.ipynb](02b_cnn_trening.ipynb)** - trening og lagring av modell
7. **[02c_cnn_testing.ipynb](02c_cnn_testing.ipynb)** - testing, evaluering og Grad-CAM
8. **[02d_cnn_konklusjon.ipynb](02d_cnn_konklusjon.ipynb)** - oppsummering og veien videre
9. **[03_medisinsk_bildeklassifikasjon_MR.ipynb](03_medisinsk_bildeklassifikasjon_MR.ipynb)** - medisinsk bildeanalyse med MR-eksempel
10. **[04a_ansiktsutrykk_klassifikasjon.ipynb](04a_ansiktsutrykk_klassifikasjon.ipynb)** - emosjonsklassifikasjon del 1
11. **[04b_ansiktsutrykk_klassifikasjon.ipynb](04b_ansiktsutrykk_klassifikasjon.ipynb)** - emosjonsklassifikasjon del 2
12. **[04c_ansiktsutrykk_klassifikasjon.ipynb](04c_ansiktsutrykk_klassifikasjon.ipynb)** - emosjonsklassifikasjon del 3

## Hva denne uken dekker

Denne uken bygger videre på maskinlæringsideen fra uke 2, men går over til modeller som kan lære mer komplekse representasjoner. Tyngdepunktet ligger på bilder, mønstergjenkjenning og hvordan lagvise modeller kan oppdage strukturer som er vanskelige å kode eksplisitt.

Uken dekker særlig:

- overgangen fra klassiske modeller til nevrale nettverk
- hvorfor konvolusjoner er nyttige for bildeanalyse
- hvordan trening, validering og testing henger sammen
- hvordan forklarbarhet kan brukes for å undersøke modellens fokus
- hvordan medisinske bilder og helsesignaler skiller seg fra enklere undervisningseksempler

## Arbeidsmåte

1. Start med `01a_nn_intro.ipynb` og `01b_læring_i_nn.ipynb` for å få det konseptuelle grunnlaget på plass.
2. Fortsett med `01c_UCI_heart_disease_klassifikasjon.ipynb` og `01d_EKG_arytmi_klassifikasjon.ipynb` for å se nevrale nettverk i helsekontekst.
3. Gå deretter gjennom `02a`-`02d` som en sammenhengende arbeidsflyt for CNN-basert bildeklassifikasjon.
4. Bruk `03_medisinsk_bildeklassifikasjon_MR.ipynb` og `04a`-`04c` som eksempler på hvordan samme idé kan anvendes på ulike datatyper og problemstillinger.

## Refleksjon

Tenk over hva du vinner og hva du mister når modellen blir mer fleksibel og mer kompleks. Spør ikke bare om ytelsen blir bedre, men også om modellen blir vanskeligere å forstå, forklare og stole på i medisinske sammenhenger.

## Videre

[Uke 4 - Generativ AI, foundation models og multimodalitet](../uke04-generativ-ai/) markerer neste store skifte i kurset: fra modeller som lærer spesifikke oppgaver til modeller som kan brukes mer generelt gjennom språk, prompts og API-er.
