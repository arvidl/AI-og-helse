# Oppsett for Google Colab

Denne filen er en kort praktisk guide til å bruke notebookene i Google Colab.

For full oversikt over alle notebooker, se toppnivå-`README.md`.

## Hurtigstart

1. Åpne ønsket notebook via Colab-badge i `README.md`.
2. Godta eventuelt meldingen om at notebooken ikke er autorisert av Google.
3. Les den første Colab-informasjonscellen. Den angir anbefalt runtime, forventet kjøretid og krav til API, data og GPU.
4. Kjør setup-cellen rett under. Den oppdager Colab, installerer bare notebook-spesifikke pakker som mangler, og definerer felles hjelpefunksjoner for secrets og Google Drive.
5. Kjør resten av cellene i rekkefølge.
6. Hvis notebooken bruker API-er eller eksterne data, følg instruksjonene i notebooken.

## Direkte lenker for å komme i gang

- [00-velkommen.ipynb](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke01-introduksjon/00-velkommen.ipynb)
- [01-test-meg.ipynb](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke01-introduksjon/01-test-meg.ipynb)
- [02-hva-er-ai.ipynb](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke01-introduksjon/02-hva-er-ai.ipynb)
- [intro_openai_anthropic.ipynb](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/intro_openai_anthropic.ipynb)

## Viktige merknader

- Alle kursnotebooks har en felles Colab-konvensjon øverst: Colab-badge, runtime-anbefaling, forventet kjøretid, krav og en standard setup-celle.
- Ikke alle notebooks er like "plug-and-play" selv om inngangen er standardisert.
- Noen notebooks krever API-nøkler, Kaggle-credentials, eksterne datasett, Google Drive, modellartefakter eller GPU-runtime.
- Se `COLAB_COMPATIBILITY_CHECKLIST.md` for en vedlikeholdt oversikt over alle notebooks og hva som krever manuelt oppsett.

## API-nøkler og secrets

API-baserte notebooks følger samme mønster:

- I Colab: legg nøklene i **Secrets** i venstremenyen, for eksempel `GEMINI_API_KEY`, `GOOGLE_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `KAGGLE_USERNAME` eller `KAGGLE_KEY`.
- Lokalt: bruk miljøvariabler eller `.env`.
- Setup-cellen definerer `get_secret(...)`, som først leser lokale miljøvariabler og deretter Colab Secrets via `userdata.get(...)`.

## Data og runtime

Notebookene merker datamønster eksplisitt øverst:

- `synthetic-or-inline`: kan normalt kjøres direkte.
- `api-secrets`: krever API-nøkkel for live-kjøring.
- `kaggle`: krever Kaggle credentials i Colab Secrets.
- `physionet`: laster eller forventer åpne PhysioNet-data.
- `oasis-nilearn`: laster OASIS-data via `nilearn`.
- `model-artifact` / `kaggle-and-drive-artifacts`: krever filer fra tidligere notebook eller Google Drive.

## Tips for Colab

- Lagre arbeidet ditt til Google Drive jevnlig.
- Bruk GPU kun når nødvendig; Colab har begrenset kvote.
- For API-baserte notebooks: bruk `intro_openai_anthropic.ipynb` som referanse for sikker håndtering av nøkler i Colab.
