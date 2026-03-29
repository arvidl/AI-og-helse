# Kaggle-data og API-tilgang

Denne guiden viser hvordan du setter opp Kaggle API lokalt for notebooks som bruker Kaggle-data.

## 1. Last ned `kaggle.json`

1. Gå til [Kaggle.com](https://www.kaggle.com) og logg inn.
2. Klikk på profilbildet ditt øverst til høyre.
3. Velg `Account`.
4. Scroll ned til seksjonen `API`.
5. Klikk `Create New API Token`.
6. Du får da lastet ned filen `kaggle.json`.

## 2. Plasser filen riktig

```bash
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

## 3. Installer Kaggle-klienten

```bash
pip install kaggle
```

Hvis du bruker conda:

```bash
conda install -c conda-forge kaggle
```

## 4. Test oppsettet

```python
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

datasets = api.dataset_list()
print(f"Fant {len(datasets)} datasett")
```

## 5. Last ned data

Eksempel med blomsterdatasettet brukt i deler av kurset:

```python
import os
from kaggle.api.kaggle_api_extended import KaggleApi

os.makedirs("./uke03-dyplæring/data/", exist_ok=True)

api = KaggleApi()
api.authenticate()
api.dataset_download_files(
    "alxmamaev/flowers-recognition",
    path="./uke03-dyplæring/data/",
    unzip=True,
)

print("Datasettet er lastet ned til ./uke03-dyplæring/data/")
```

## Feilsøking

### `403 Forbidden`

- sjekk at `~/.kaggle/kaggle.json` finnes
- sjekk at filen har riktige tillatelser: `chmod 600 ~/.kaggle/kaggle.json`
- kontroller at API-nøkkelen fortsatt er gyldig

### `401 Unauthorized`

- sjekk at `kaggle.json` inneholder riktig brukernavn og nøkkel
- prøv å generere en ny API-token i Kaggle

### `404 Not Found`

- sjekk at dataset-navnet er korrekt
- sjekk at datasettet faktisk er offentlig eller at du har tilgang

## Sikkerhet

- Ikke del `kaggle.json`.
- Ikke commit `kaggle.json` eller andre legitimasjonsfiler til Git.
- Oppbevar filen i `~/.kaggle/`, ikke i prosjektmappen.

## Nyttige kommandoer

```bash
kaggle datasets list
kaggle datasets list -s flowers
kaggle datasets download -d alxmamaev/flowers-recognition
```