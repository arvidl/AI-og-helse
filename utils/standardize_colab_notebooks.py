#!/usr/bin/env python3
"""Standardize Google Colab entry cells across course notebooks.

The script inserts or updates two tagged cells at the top of every notebook:

1. A markdown "Colab contract" with badge, runtime, expected time and requirements.
2. A code bootstrap cell with Colab detection, minimal package installation and
   a shared secrets helper for Colab Secrets / local environment variables.

It also clears outputs from cells that contain local machine paths, so these
paths are not published as stale execution output.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_MARKER = "<!-- AI-og-helse: colab-kontrakt v1 -->"
CODE_MARKER = "# AI-og-helse: Colab bootstrap v1"
LOCAL_PATH_PATTERNS = (
    "/Users/arvid",
    "~/GitHub",
    "/opt/anaconda3",
    "GitHub/AI-og-helse",
    "nilearn_data",
)


NOTEBOOKS = {
    "intro_openai_anthropic.ipynb": {
        "runtime": "CPU",
        "time": "10-20 min",
        "packages": [("openai", "openai"), ("anthropic", "anthropic"), ("python-dotenv", "dotenv")],
        "requirements": ["API: OPENAI_API_KEY og ANTHROPIC_API_KEY", "Data: ingen eksterne datasett", "GPU: ikke nødvendig"],
        "data_mode": "api-secrets",
        "notes": "Bruk Colab Secrets for API-nøkler, eller `.env` lokalt.",
    },
    "utils/imgur-opplasting.ipynb": {
        "runtime": "CPU",
        "time": "5-10 min",
        "packages": [],
        "requirements": ["API/data: utility-notebook, kan kreve lokal filtilpasning", "GPU: ikke nødvendig"],
        "data_mode": "local-utility",
        "notes": "Dette er en hjelpe-notebook og er ikke en primær kursnotebook.",
    },
}


def default_profile(relative_path: str) -> dict:
    packages: list[tuple[str, str]] = []
    runtime = "CPU"
    time = "5-15 min"
    requirements = ["API: ikke nødvendig", "Data: syntetisk eller innebygd i notebooken", "GPU: ikke nødvendig"]
    data_mode = "synthetic-or-inline"
    notes = "Kjør cellene ovenfra og ned. Setup-cellen installerer bare ekstra pakker når notebooken åpnes i Colab."

    if relative_path == "uke01-introduksjon/01-test-meg.ipynb":
        requirements = [
            "API: ikke nødvendig",
            "Data: ingen eksterne datasett",
            "GPU: ikke nødvendig",
            "Valgfritt: norsk BERT/transformers-demo kan aktiveres manuelt",
        ]
        time = "5-15 min"
    elif relative_path == "uke01-introduksjon/99-oppsett-miljø.ipynb":
        requirements = ["API: ikke nødvendig", "Data: ingen eksterne datasett", "GPU: valgfritt for demonstrasjon"]
        data_mode = "environment-check"
        time = "10-15 min"
    elif relative_path.startswith("uke03-dyplæring/"):
        runtime = "CPU"
        time = "10-25 min"
        requirements = ["API: ikke nødvendig", "Data: se notebookens datasettseksjon", "GPU: valgfritt med mindre annet er oppgitt"]
        data_mode = "course-data"
        if "01d_EKG" in relative_path:
            packages = [("wfdb", "wfdb")]
            requirements = ["API: ikke nødvendig", "Data: PhysioNet MIT-BIH", "GPU: valgfritt"]
            data_mode = "physionet"
            time = "20-40 min"
        elif "02b_cnn_trening" in relative_path:
            runtime = "GPU anbefalt"
            requirements = ["API: ikke nødvendig", "Data: forberedt bildedatasett fra 02a", "GPU: anbefalt"]
            data_mode = "prepared-data"
            time = "30-60 min"
        elif "02c_cnn_testing" in relative_path:
            requirements = ["API: ikke nødvendig", "Data: modellartefakt fra 02b", "GPU: ikke nødvendig"]
            data_mode = "model-artifact"
            time = "10-20 min"
        elif "03_medisinsk_bildeklassifikasjon_MR" in relative_path:
            runtime = "GPU valgfritt"
            packages = [("nibabel", "nibabel"), ("nilearn", "nilearn"), ("torchinfo", "torchinfo")]
            requirements = ["API: ikke nødvendig", "Data: OASIS via nilearn", "GPU: valgfritt"]
            data_mode = "oasis-nilearn"
            time = "30-60 min"
        elif "04a_ansiktsutrykk" in relative_path:
            runtime = "GPU anbefalt"
            packages = [("kaggle", "kaggle"), ("torchsummary", "torchsummary")]
            requirements = ["API: KAGGLE_USERNAME og KAGGLE_KEY for Kaggle API", "Data: FER2013 fra Kaggle", "GPU: anbefalt"]
            data_mode = "kaggle"
            time = "30-60 min"
        elif "04b_ansiktsutrykk" in relative_path:
            runtime = "GPU anbefalt"
            packages = [("kaggle", "kaggle"), ("torchsummary", "torchsummary")]
            requirements = ["API: KAGGLE_USERNAME og KAGGLE_KEY for Kaggle API", "Data: FER2013 og/eller modellartefakter", "GPU: anbefalt"]
            data_mode = "kaggle-and-drive-artifacts"
            time = "30-90 min"
        elif "04c_ansiktsutrykk" in relative_path:
            packages = [("kaggle", "kaggle")]
            requirements = ["API: KAGGLE_USERNAME og KAGGLE_KEY for Kaggle API", "Data: FER2013 og lagret modell", "GPU: ikke nødvendig"]
            data_mode = "kaggle-and-drive-artifacts"
            time = "15-30 min"
    elif relative_path.startswith("uke04-generativ-ai/"):
        requirements = ["API: ikke nødvendig med mindre notebooken ber om det", "Data: ingen eksterne datasett", "GPU: ikke nødvendig"]
        if "02_llm_grunnleggende" in relative_path:
            packages = [("tiktoken", "tiktoken")]
            time = "10-20 min"
        elif "03_prompt_engineering" in relative_path:
            packages = [("google-genai", "google.genai"), ("openai", "openai"), ("anthropic", "anthropic"), ("python-dotenv", "dotenv")]
            requirements = ["API: GEMINI_API_KEY/GOOGLE_API_KEY anbefalt; OpenAI/Anthropic valgfritt", "Data: ingen eksterne datasett", "GPU: ikke nødvendig"]
            data_mode = "api-secrets"
            time = "20-40 min"
        elif "04_chatgpt_claude_api" in relative_path:
            packages = [("google-genai", "google.genai"), ("openai", "openai"), ("anthropic", "anthropic"), ("python-dotenv", "dotenv")]
            requirements = ["API: GEMINI_API_KEY/GOOGLE_API_KEY, OPENAI_API_KEY og/eller ANTHROPIC_API_KEY", "Data: ingen eksterne datasett", "GPU: ikke nødvendig"]
            data_mode = "api-secrets"
            time = "20-40 min"
        elif "10_bilde_tekst_clip" in relative_path:
            runtime = "GPU valgfritt"
            packages = [("transformers", "transformers")]
            requirements = ["API: ikke nødvendig", "Data: bilder lastes/ned eller brukes fra notebooken", "GPU: valgfritt for raskere modellkjøring"]
            data_mode = "model-download"
            time = "20-40 min"
        elif "oppgaver/prompt_workshop" in relative_path:
            packages = [("openai", "openai"), ("python-dotenv", "dotenv")]
            requirements = ["API: OPENAI_API_KEY for live-kjøring; kan leses uten", "Data: ingen eksterne datasett", "GPU: ikke nødvendig"]
            data_mode = "api-secrets"
            time = "20-40 min"
    elif relative_path.startswith("uke05-agentisk-ai/"):
        requirements = ["API: ikke nødvendig med mindre notebooken ber om det", "Data: syntetisk case/materiale", "GPU: ikke nødvendig"]
        time = "15-30 min"
        if "03_crewai" in relative_path:
            packages = [("crewai", "crewai"), ("google-genai", "google.genai"), ("python-dotenv", "dotenv")]
            requirements = ["API: GOOGLE_API_KEY eller GEMINI_API_KEY", "Data: syntetisk rehabiliteringscase", "GPU: ikke nødvendig"]
            data_mode = "api-secrets"
            time = "30-60 min"
    elif relative_path.startswith("uke06-klinisk-praksis/"):
        requirements = ["API: ikke nødvendig", "Data: syntetisk klinisk datasett", "GPU: ikke nødvendig"]
        time = "15-30 min"
        if "01_risikomodell" in relative_path:
            packages = [("shap", "shap")]
            time = "20-40 min"
    elif relative_path.startswith("uke07-velferdsteknologi/"):
        requirements = ["API: ikke nødvendig", "Data: syntetisk/simulert data", "GPU: ikke nødvendig"]
        time = "10-25 min"
    elif relative_path.startswith("uke08-etikk-implementering/"):
        requirements = ["API: ikke nødvendig", "Data: syntetisk eller innebygd i notebooken", "GPU: ikke nødvendig"]
        time = "10-25 min"

    return {
        "runtime": runtime,
        "time": time,
        "packages": packages,
        "requirements": requirements,
        "data_mode": data_mode,
        "notes": notes,
    }


def profile_for(relative_path: str) -> dict:
    profile = default_profile(relative_path)
    profile.update(NOTEBOOKS.get(relative_path, {}))
    return profile


def source_to_lines(source: str) -> list[str]:
    return source.splitlines(keepends=True)


def cell_source(cell: dict) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(source)
    return source


def markdown_cell(relative_path: str, profile: dict) -> dict:
    colab_url = f"https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/{relative_path}"
    requirements = "\n".join(f"- {item}" for item in profile["requirements"])
    text = f"""{MARKDOWN_MARKER}

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})

## Colab-kjøring

- **Anbefalt runtime:** {profile["runtime"]}
- **Forventet kjøretid:** {profile["time"]}
- **Datamønster:** `{profile["data_mode"]}`

**Krav før kjøring:**
{requirements}

**Felles konvensjon:** Kjør setup-cellen rett under først. I Colab hentes hemmeligheter fra **Secrets** med `userdata.get(...)`; lokalt brukes miljøvariabler eller `.env`.

{profile["notes"]}
"""
    return {
        "cell_type": "markdown",
        "metadata": {"tags": ["ai-og-helse-colab-contract"]},
        "source": source_to_lines(text),
    }


def code_cell(profile: dict) -> dict:
    packages_repr = repr(profile["packages"])
    text = f"""{CODE_MARKER}
import importlib.util
import os
import subprocess
import sys
from pathlib import Path

IN_COLAB = "google.colab" in sys.modules
NOTEBOOK_PACKAGES = {packages_repr}
COLAB_DATA_MODE = {profile["data_mode"]!r}


def _has_import(import_name: str) -> bool:
    return importlib.util.find_spec(import_name) is not None


def ensure_packages(packages=NOTEBOOK_PACKAGES):
    \"\"\"Install only notebook-specific packages when running in Colab.\"\"\"
    if not IN_COLAB:
        return

    missing = [package for package, import_name in packages if not _has_import(import_name)]
    if missing:
        print("Installerer Colab-pakker:", ", ".join(missing))
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", *missing])
    else:
        print("Alle notebook-spesifikke Colab-pakker er tilgjengelige.")


def get_secret(name: str, *aliases: str):
    \"\"\"Read secrets from environment/.env locally or Colab Secrets in Colab.\"\"\"
    for key in (name, *aliases):
        value = os.getenv(key)
        if value:
            os.environ[name] = value
            return value

    if IN_COLAB:
        try:
            from google.colab import userdata
        except Exception:
            userdata = None

        if userdata is not None:
            for key in (name, *aliases):
                try:
                    value = userdata.get(key)
                except Exception:
                    value = None
                if value:
                    os.environ[name] = value
                    return value

    return None


def mount_drive_if_needed():
    \"\"\"Mount Google Drive explicitly in notebooks that need persistent artifacts.\"\"\"
    if not IN_COLAB:
        return None
    from google.colab import drive

    drive.mount("/content/drive")
    return Path("/content/drive/MyDrive")


ensure_packages()
print("Miljø:", "Google Colab" if IN_COLAB else "lokalt")
print("Datamønster:", COLAB_DATA_MODE)
"""
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {"tags": ["ai-og-helse-colab-bootstrap"]},
        "outputs": [],
        "source": source_to_lines(text),
    }


def clear_outputs_with_local_paths(nb: dict) -> int:
    cleared = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        outputs = cell.get("outputs", [])
        if not outputs:
            continue
        output_text = json.dumps(outputs, ensure_ascii=False)
        if any(pattern in output_text for pattern in LOCAL_PATH_PATTERNS):
            cell["outputs"] = []
            cell["execution_count"] = None
            cleared += 1
    return cleared


def upsert_top_cells(nb: dict, relative_path: str) -> None:
    profile = profile_for(relative_path)
    cells = nb.setdefault("cells", [])

    if cells and MARKDOWN_MARKER in cell_source(cells[0]):
        cells[0] = markdown_cell(relative_path, profile)
    else:
        cells.insert(0, markdown_cell(relative_path, profile))

    if len(cells) > 1 and CODE_MARKER in cell_source(cells[1]):
        cells[1] = code_cell(profile)
    else:
        cells.insert(1, code_cell(profile))


def remove_duplicate_colab_badge(nb: dict) -> None:
    cells = nb.get("cells", [])
    if len(cells) > 2:
        source = cell_source(cells[2]).strip()
        if source.startswith("[![Open In Colab]") and "colab.research.google.com" in source:
            del cells[2]


def simple_week01_import_cell(message: str = "✅ Imports klare.") -> dict:
    text = f"""# Felles imports for notebooken
import json
import os
import sys
import warnings
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

warnings.filterwarnings("ignore")
plt.rcParams["font.family"] = ["DejaVu Sans", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False

print("Miljø:", "Google Colab" if IN_COLAB else "lokalt")
print({message!r})
"""
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source_to_lines(text),
    }


def simple_week01_import_markdown() -> dict:
    text = """### Felles imports

Colab-oppsettet er allerede håndtert i standardcellen øverst. Denne cellen laster bare bibliotekene som brukes videre i notebooken.
"""
    return {"cell_type": "markdown", "metadata": {}, "source": source_to_lines(text)}


def cleanup_legacy_week01_setup(nb: dict, relative_path: str) -> None:
    if not relative_path.startswith("uke01-introduksjon/"):
        return

    cells = nb.get("cells", [])
    for idx in range(len(cells) - 1):
        markdown = cell_source(cells[idx])
        code = cell_source(cells[idx + 1])
        is_legacy_heading = "miljøoppsett" in markdown.lower()
        is_legacy_code = (
            "Sjekk om vi kjører i Google Colab" in code
            or "Universal miljøoppsett" in code
        )
        if is_legacy_heading and is_legacy_code:
            cells[idx] = simple_week01_import_markdown()
            cells[idx + 1] = simple_week01_import_cell()
            break


def update_week01_setup_text(nb: dict, relative_path: str) -> None:
    if relative_path != "uke01-introduksjon/99-oppsett-miljø.ipynb":
        return

    for cell in nb.get("cells", []):
        source = cell_source(cell)
        if "Velkommen til kurset **AI og Helse**" in source and "## 🎯 To hovedalternativer:" in source:
            text = """# 🚀 Utviklingsmiljø - lokalt med uv og Google Colab

Velkommen til kurset **AI og Helse**! Denne notebooken hjelper deg å forstå de to viktigste måtene å kjøre kursmaterialet på.

## 🎯 To hovedalternativer

### 1. 🏠 Lokalt miljø med `uv` (anbefalt for egen maskin uten CUDA)
- Raskt å opprette og gjenskape
- Bruker `.venv` og `requirements.txt`
- Fungerer godt på Mac, Linux og Windows for vanlig notebook-kjøring
- Gir full kontroll over filer, Git og videreutvikling

### 2. 📊 Google Colab (enklest for eksperimentering)
- Krever ingen lokal installasjon
- Åpnes direkte fra Colab-badgene i repoet
- Gir tilgang til begrenset gratis GPU ved behov
- Passer godt for lesing, demoer og undervisning

### CUDA/NVIDIA-unntak

For tunge dyplæringsnotebooks på Linux/Windows med NVIDIA-GPU og CUDA er `environment_cuda.yml` med conda fortsatt anbefalt. Dette er et spesialspor for GPU-binærpakker, ikke standardoppsettet for kurset.
"""
            cell["source"] = source_to_lines(text)
        elif "## 🔄 Sammenligning: Lokalt vs Colab" in source:
            text = """## 🔄 Sammenligning: lokalt `uv` vs Colab

| Aspekt | Lokalt med `uv` | Google Colab |
|--------|------------------|---------------|
| 💰 **Kostnad** | Gratis på egen maskin | Gratis med kvoter |
| 🔧 **Oppsett** | En gang per repo: `.venv` + `requirements.txt` | Ingen lokal installasjon |
| 💾 **Lagring** | Lokal disk og Git | Midlertidig runtime, evt. Google Drive |
| 🚀 **Ytelse** | Stabil lokal ytelse | Variabel, avhengig av runtime |
| 🎮 **GPU** | Avhengig av egen maskin | Begrenset gratis GPU |
| 📝 **Editor** | Cursor/Jupyter/VS Code | Nettleserbasert notebook |
| 🔄 **Reproduserbarhet** | God med `uv` og låst repo | God for enkle notebooks, mer manuell for data/API |

### 🎯 Anbefaling

- **Bruk Colab** hvis du vil komme raskt i gang uten lokal installasjon.
- **Bruk lokalt `uv`-miljø** hvis du skal arbeide videre med kurset, endre filer eller bidra med forbedringer.
- **Bruk conda CUDA-sporet** bare når du faktisk trenger NVIDIA/CUDA lokalt.
"""
            cell["source"] = source_to_lines(text)
        elif "Følg instruksjonene i hovedREADME-filen" in source:
            cell["source"] = source_to_lines(source.replace(
                "Følg instruksjonene i hovedREADME-filen for å sette opp Anaconda eller pip/venv.",
                "Følg instruksjonene i hovedREADME-filen for å sette opp `uv`-miljøet. Kortversjon: `uv venv --python 3.12`, aktiver `.venv`, og kjør `uv pip install -r requirements.txt`.",
            ))
        elif "reinstallere conda environment" in source:
            cell["source"] = source_to_lines(source.replace(
                "reinstallere conda environment",
                "opprette `.venv` på nytt med `uv`",
            ).replace(
                "`pip install [pakkenavn]` eller `conda install [pakkenavn]`",
                "`uv pip install [pakkenavn]` i aktivert `.venv`",
            ))
        elif "Universal miljøoppsett" in source:
            replacement = simple_week01_import_cell(
                "✅ Miljøtest-importer er klare. Colab-bootstrapen øverst håndterer selve Colab-oppsettet."
            )
            cell["source"] = replacement["source"]
            cell["execution_count"] = None
            cell["outputs"] = []


def optional_bert_demo_markdown() -> dict:
    text = """## Valgfri fordypning: norsk BERT

Resten av notebooken har allerede testet miljøet og vist en simulert AI-assistent. Cellene under er en **frivillig fordypning** for deg som vil se hvordan en norsk språkmodell kan lage tekstrepresentasjoner.

For å spare tid i Colab kjøres ikke denne delen automatisk. Sett `RUN_OPTIONAL_BERT_DEMO = True` i neste celle hvis du vil laste ned og teste modellen.
"""
    return {"cell_type": "markdown", "metadata": {}, "source": source_to_lines(text)}


def update_optional_bert_demo(nb: dict, relative_path: str) -> None:
    if relative_path != "uke01-introduksjon/01-test-meg.ipynb":
        return

    cells = nb.get("cells", [])
    for idx, cell in enumerate(cells):
        if "# Test at alt fungerer" in cell_source(cell):
            previous = cell_source(cells[idx - 1]) if idx > 0 else ""
            if "Valgfri fordypning: norsk BERT" not in previous:
                cells.insert(idx, optional_bert_demo_markdown())
                idx += 1
            cells[idx] = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": source_to_lines("""# Valgfri test av åpne språkmodeller
RUN_OPTIONAL_BERT_DEMO = False
BERT_DEMO_READY = False

if not RUN_OPTIONAL_BERT_DEMO:
    print("Hopper over frivillig BERT-demo.")
    print("Sett RUN_OPTIONAL_BERT_DEMO = True og kjør cellen på nytt hvis du vil teste språkmodeller.")
else:
    from transformers import AutoModel, AutoTokenizer, pipeline
    import warnings
    warnings.filterwarnings("ignore")

    print("🤖 TESTING AV NORSKE SPRÅKMODELLER")
    print("=" * 50)

    modeller_å_teste = [
        "NbAiLab/nb-bert-base",
        "ltg/norbert3-large",
        "microsoft/DialoGPT-small",
    ]

    for model_name in modeller_å_teste:
        try:
            print(f"\\n🔍 Tester {model_name}...")
            if "bert" in model_name.lower():
                tokenizer = AutoTokenizer.from_pretrained(model_name)
                model = AutoModel.from_pretrained(model_name)
                print(f"✅ {model_name} lastet inn (BERT-modell for tekstforståelse)")
                BERT_DEMO_READY = model_name == "NbAiLab/nb-bert-base"
            else:
                generator = pipeline("text-generation", model=model_name, max_length=50)
                prompt = "Pasienten presenterer symptomer på"
                result = generator(prompt, max_length=50, num_return_sequences=1)
                print(f"✅ {model_name} fungerer!")
                print(f"📝 Resultat: {result[0]['generated_text']}")
            break
        except Exception as e:
            print(f"❌ {model_name} feilet: {str(e)[:100]}...")
            continue
"""),
            }
            break

    for idx, cell in enumerate(cells):
        source = cell_source(cell)
        if "# Fysioterapi-eksempel med norsk BERT" in source:
            cells[idx] = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": source_to_lines("""# Fysioterapi-eksempel med norsk BERT
if not BERT_DEMO_READY:
    print("BERT-demoen er ikke aktivert eller modellen ble ikke lastet.")
    print("Gå tilbake til forrige celle og sett RUN_OPTIONAL_BERT_DEMO = True for å kjøre dette eksempelet.")
else:
    import torch
    from sklearn.metrics.pairwise import cosine_similarity

    print("🏃‍♀️ FYSIOTERAPI-EKSEMPEL MED NORSK BERT")
    print("=" * 50)

    def get_sentence_embedding(text):
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
            return outputs.last_hidden_state[:, 0, :].numpy()

    pasient_symptomer = [
        "Jeg har vondt i ryggen når jeg sitter lenge",
        "Kneet mitt verker etter løping",
        "Skulderen er stiv om morgenen",
        "Nakken er øm etter bilulykke",
        "Ankelen hovner etter fall",
    ]

    fysioterapi_behandlinger = [
        "Styrketrening for korsryggen og stabilisering",
        "Løpeteknikk og knestabilitet øvelser",
        "Mobilisering og tøyning av skulderkapsel",
        "Nakkestabilisering og postural trening",
        "Ankelstabilitet og balanse øvelser",
    ]

    print("🎯 AUTOMATISK MATCHING: Symptom → Behandling")
    print("-" * 50)

    symptom_embeddings = [get_sentence_embedding(symptom) for symptom in pasient_symptomer]
    behandling_embeddings = [get_sentence_embedding(behandling) for behandling in fysioterapi_behandlinger]

    for i, symptom in enumerate(pasient_symptomer):
        print(f"\\n📋 Pasient sier: '{symptom}'")
        symptom_emb = symptom_embeddings[i]
        similarities = []

        for j, behandling_emb in enumerate(behandling_embeddings):
            similarity = cosine_similarity(symptom_emb, behandling_emb)[0][0]
            similarities.append((similarity, j, fysioterapi_behandlinger[j]))

        similarities.sort(reverse=True)
        best_score, best_idx, best_behandling = similarities[0]
        print(f"🎯 AI foreslår: '{best_behandling}'")
        print(f"📊 Likhet: {best_score:.3f}")
        print("🔄 Andre alternativer:")
        for score, idx, behandling in similarities[1:3]:
            print(f"   • {behandling} (likhet: {score:.3f})")
"""),
            }
        elif 'print(f"\\n💡 HVA SKJER HER?")' in source:
            cells[idx] = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": source_to_lines("""if not BERT_DEMO_READY:
    print("Forklaringscellen hører til den valgfrie BERT-demoen og hoppes over.")
else:
    print(f"\\n💡 HVA SKJER HER?")
    print("-" * 30)
    print("✅ BERT forstår norsk tekst og konverterer til tall-representasjoner")
    print("✅ Vi sammenligner symptomer med behandlinger matematisk")
    print("✅ AI finner den mest semantisk like behandlingen")
    print("✅ Dette kan hjelpe fysioterapeuter med behandlingsforslag")

    print(f"\\n⚠️ VIKTIG Å HUSKE:")
    print("• AI er et verktøy - ikke erstatning for faglig skjønn")
    print("• Trenger validering av erfarne fysioterapeuter")
    print("• Må kombineres med klinisk undersøkelse")
    print("• Pasientsikkerhet kommer alltid først")
"""),
            }
        elif "# Bonus: Test hvor godt modellen forstår fysioterapi-terminologi" in source:
            cells[idx] = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": source_to_lines("""# Bonus: Test hvor godt modellen forstår fysioterapi-terminologi
if not BERT_DEMO_READY:
    print("Bonusdelen hører til den valgfrie BERT-demoen og hoppes over.")
else:
    print(f"\\n🧪 BONUS: Terminologi-forståelse")
    print("-" * 40)

    fysio_ord = ["mobilisering", "stabilisering", "tøyning", "styrketrening", "balanse"]
    relaterte_ord = ["bevegelse", "stabilitet", "fleksibilitet", "muskeloppbygging", "koordinasjon"]

    print("Hvor godt forstår BERT fysioterapi-begreper?")
    for fysio_ord, relatert_ord in zip(fysio_ord, relaterte_ord):
        emb1 = get_sentence_embedding(fysio_ord)
        emb2 = get_sentence_embedding(relatert_ord)
        similarity = cosine_similarity(emb1, emb2)[0][0]
        print(f"  '{fysio_ord}' ↔ '{relatert_ord}': {similarity:.3f}")

    print(f"\\n🎓 LÆRINGSUTBYTTE:")
    print("• Forstår hvordan AI kan brukes i fysioterapi")
    print("• Ser potensialet for automatisk symptom-matching")
    print("• Kjenner til begrensninger og sikkerhetshensyn")
"""),
            }


def main() -> int:
    excluded_parts = {".git", ".venv", ".ipynb_checkpoints", "__pycache__", "my_stuff"}
    notebooks = sorted(
        path
        for path in ROOT.rglob("*.ipynb")
        if not any(part in excluded_parts for part in path.relative_to(ROOT).parts)
    )
    changed = 0
    cleared_total = 0

    for path in notebooks:
        relative_path = path.relative_to(ROOT).as_posix()
        nb = json.loads(path.read_text(encoding="utf-8"))
        before = json.dumps(nb, ensure_ascii=False, sort_keys=True)

        upsert_top_cells(nb, relative_path)
        remove_duplicate_colab_badge(nb)
        cleanup_legacy_week01_setup(nb, relative_path)
        update_week01_setup_text(nb, relative_path)
        update_optional_bert_demo(nb, relative_path)
        cleared_total += clear_outputs_with_local_paths(nb)

        after = json.dumps(nb, ensure_ascii=False, sort_keys=True)
        if after != before:
            path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            changed += 1

    print(f"Oppdaterte notebooks: {changed}/{len(notebooks)}")
    print(f"Ryddet outputs med lokale stier i {cleared_total} celler")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
