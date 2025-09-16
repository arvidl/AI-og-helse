Her er en markdown-guide for å sette opp Kaggle API tilgang:

```markdown
# Kaggle API Setup Guide

## Hvordan få tilgang til Kaggle-data via kaggle.json

### Steg 1: Last ned kaggle.json

1. Gå til [Kaggle.com](https://www.kaggle.com) og logg inn på din konto
2. Klikk på din profil-bilde (øverst til høyre)
3. Velg "Account" fra dropdown-menyen
4. Scroll ned til "API" seksjonen
5. Klikk "Create New API Token"
6. Dette vil laste ned en `kaggle.json` fil til din nedlastingsmappe

### Steg 2: Plasser kaggle.json i riktig mappe

```bash
# Opprett .kaggle mappen hvis den ikke finnes
mkdir -p ~/.kaggle

# Flytt kaggle.json filen til ~/.kaggle/ mappen
mv ~/Downloads/kaggle.json ~/.kaggle/

# Sett riktige tillatelser (viktig for sikkerhet)
chmod 600 ~/.kaggle/kaggle.json
```

### Steg 3: Verifiser at filen er på plass

```bash
# Sjekk at filen finnes
ls -la ~/.kaggle/

# Sjekk innholdet (valgfritt)
cat ~/.kaggle/kaggle.json
```

Filen skal se ut som dette:
```json
{"username":"ditt_brukernavn","key":"din_api_nøkkel"}
```

### Steg 4: Installer Kaggle API

```bash
# Installer via pip
pip install kaggle

# Eller via conda
conda install -c conda-forge kaggle
```

### Steg 5: Test tilkoblingen

```python
# Test i Python
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialiser API
api = KaggleApi()
api.authenticate()

# Test ved å liste tilgjengelige datasets
datasets = api.dataset_list()
print(f"Tilgjengelige datasets: {len(datasets)}")
```

### Steg 6: Last ned data

```python
# Eksempel: Last ned Flowers Recognition dataset
api.dataset_download_files(
    'alxmamaev/flowers-recognition',
    path='./data/',
    unzip=True
)
```

### Feilsøking

#### Problem: "403 - Forbidden"
- Sjekk at `kaggle.json` er i `~/.kaggle/` mappen
- Verifiser at filen har riktige tillatelser: `chmod 600 ~/.kaggle/kaggle.json`
- Sjekk at API-nøkkelen er gyldig i Kaggle-kontoen din

#### Problem: "404 - Not Found"
- Sjekk at dataset-navnet er korrekt
- Verifiser at du har tilgang til datasettet (ikke private datasets)

#### Problem: "401 - Unauthorized"
- Sjekk at `kaggle.json` inneholder riktig brukernavn og API-nøkkel
- Prøv å generere en ny API-nøkkel fra Kaggle

### Sikkerhetstips

- **Ikke del `kaggle.json` filen** - den inneholder dine API-legitimasjoner
- **Ikke commit filen til Git** - legg til `~/.kaggle/` i `.gitignore`
- **Rotér API-nøkkelen regelmessig** for bedre sikkerhet

### Nyttige kommandoer

```bash
# Sjekk API status
kaggle competitions list

# Last ned et spesifikt dataset
kaggle datasets download -d alxmamaev/flowers-recognition

# List alle tilgjengelige datasets
kaggle datasets list

# Søk etter datasets
kaggle datasets list -s flowers
```

### Eksempel for AI-og-helse prosjektet

```python
# For å laste ned Flowers Recognition dataset til prosjektet
import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Opprett data-mappe
os.makedirs('./uke03-dyplæring/data/', exist_ok=True)

# Initialiser og autentiser
api = KaggleApi()
api.authenticate()

# Last ned dataset
api.dataset_download_files(
    'alxmamaev/flowers-recognition',
    path='./uke03-dyplæring/data/',
    unzip=True
)

print("Dataset lastet ned til ./uke03-dyplæring/data/")
```

Denne oppsettet gir deg full tilgang til Kaggle API for å laste ned datasets direkte i Python-koden din.
```