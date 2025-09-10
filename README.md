# 🏥 AI og Helse - EVU Kurs (5 ECTS)

Videreutdanningskurs i kunstig intelligens for helse- og omsorgssektoren ved Universitetet i Bergen.

(Utfyllende [emnebeskrivelse](https://github.com/arvidl/AI-og-helse/blob/main/Emnebeskrivelse.md))

## 🚀 Kom i gang

### For studenter - Bruk GitHub Codespaces (anbefalt)

1. Gå til: https://github.com/arvidl/AI-og-helse
2. Klikk på den grønne "Code" knappen
3. Velg "Codespaces" fanen
4. Klikk "Create codespace on main"
5. Vent 2-3 minutter mens miljøet settes opp automatisk

Når Codespace er klar, kjør:
```bash
source ~/.bashrc
conda env update -f environment-codespaces.yml
conda activate ai-helse
python check_setup.py
```

Dette vil verifisere at alt er korrekt installert.

####  Start med Uke 1
Naviger til `uke01-introduksjon/` og åpne [`README.md`](uke01-introduksjon/README.md) for ukens oversikt.


### For lokal utvikling - Anaconda (anbefalt for Mac/PC)

```bash
# Klon repository
git clone https://github.com/arvidl/AI-og-helse.git
cd AI-og-helse

# Opprett conda environment fra yml fil
conda env create -f environment.yml

# Aktiver miljøet
conda activate ai-helse

# Installer Jupyter kernel
python -m ipykernel install --user --name ai-helse --display-name "Python 3.12 (AI-Helse)"

# Verifiser installasjon
python check_setup.py
```
**Alternativ: Bruk pip/venv (hvis du ikke har Anaconda)**

```bash
# Sørg for at du har Python 3.12 installert
python3.12 --version

# Opprett virtuelt miljø med Python 3.12
python3.12 -m venv venv

# Aktiver miljø
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

# Installer dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Verifiser installasjon
python check_setup.py
```

**For Cursor-brukere**
1. Åpne prosjektet i Cursor
2. Cursor vil automatisk detektere conda environment
3. Velg "Python 3.12 (ai-helse)" som interpreter
4. Alternativt: Cmd/Ctrl+Shift+P → "Python: Select Interpreter" → ai-helse


**API-nøkler (for lokal kjøring)**

Opprett en `.env` fil i rotmappen:
```env
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
```

**NB:** For studenter i Codespaces er API-nøkler forhåndskonfigurert.



## 📚 Kursstruktur

- **Del 1 (Uke 1-6):** AI Fundamentet - Fra AI 1.0 til AI 2.0
- **Del 2 (Uke 7-8):** Praktiske anvendelser i helse og omsorg
- **Del 3 (Uke 9-10):** Fysisk samling og eksamen

## 🎯 Læringsutbytte

### Kunnskaper
- Forstå forskjellen mellom klassisk maskinlæring (AI 1.0) og generativ AI (AI 2.0)
- Kjenne til praktiske anvendelser av AI i helse- og omsorgstjenesten
- Forstå grunnleggende prinsipper for AI-støttet analyse, optimering og beslutning
- Ha innsikt i etiske og regulatoriske aspekter ved AI i helse

### Ferdigheter
- Bruke generative AI-verktøy (ChatGPT, Claude, Gemini) for faglige oppgaver
- Vurdere egnethet av AI-løsninger for konkrete problemstillinger
- Identifisere muligheter for AI-støtte i egen arbeidshverdag
- Kritisk evaluere AI-systemer og deres begrensninger

## 📂 Repository struktur

```
AI-og-helse/
├── .devcontainer/          # GitHub Codespaces konfigurasjon
├── uke01-introduksjon/     # Introduksjon til AI
├── uke02-klassisk-ml/      # Klassisk maskinlæring
├── uke03-dyp-laering/      # Dyp læring og nevrale nettverk
├── uke04-generativ-ai/     # Store språkmodeller
├── uke05-multimodal-ai/    # RAG og AI-agenter
├── uke06-klinisk-praksis/  # AI i helsefag
├── uke07-velferdsteknologi/# Robotikk og optimering
├── uke08-etikk-implementering/
├── uke09-fysisk-samling/
├── uke10-eksamen/
├── prosjekt/               # Prosjektoppgave maler
├── utils/                  # Hjelpefunksjoner
└── data/                   # Eksempeldata
```

## 💻 Teknologi

- **Python 3.12+**
- **Jupyter Notebooks** for interaktiv læring
- **GitHub Codespaces** for cloud-basert utvikling
- **AI-verktøy:** OpenAI, Anthropic, Autogen, LangChain

## 📝 Vurdering

- **Hjemmeeksamen** (60%): 48-timers eksamen i uke 10
- **Prosjektoppgave** (40%): Praktisk anvendelse av AI
- **Obligatorisk:** 3 refleksjonsnotater (godkjent/ikke godkjent)

## 🛠️ Teknisk støtte

- **GitHub Issues:** [Rapporter problemer](https://github.com/arvidl/AI-og-helse/issues)
- **Diskusjoner:** [Kursforum](https://github.com/arvidl/AI-og-helse/discussions)
- **E-post:** Kursansvarlig
  <!--
  arvid.lundervold@uib.no
  -->

## 📖 Læringsressurser

- [Ordliste](ressurser/ordliste.md)
- [Verktøyguider](ressurser/verktoy/)
- [Artikkelsamling](ressurser/artikler/)


## 👥 Målgruppe

- Helsepersonell (leger, sykepleiere, radiografer, terapeuter, psykologer)
- Ansatte i omsorgstjenesten
- Ledere i helse og omsorg
- IT- og digitaliseringsansvarlige
- Kvalitets- og utviklingsrådgivere

## 📅 Praktisk informasjon

- **Varighet:** 10 uker (vårsemester)
- **Arbeidsomfang:** 10-12 timer per uke
- **Undervisningsspråk:** Norsk
- **Fysisk samling:** 1 dag (uke 9)

## 📄 Lisens

Dette kursmaterialet er utviklet ved Universitetet i Bergen og er lisensiert under [CC BY-SA 4.0](LICENSE).

## 🙏 Bidragsytere

- Arvid Lundervold (Kursansvarlig)
- [Bidragsytere](CONTRIBUTING.md)

---

**Lykke til med kurset!** 🎓

For spørsmål, kontakt: Kursansvarlig
<!--
arvid.lundervold@uib.no
-->




<!--


# AI og Helse - GitHub Repository Struktur

## Repository: `AI-helse-EVU`

```
AI-helse-EVU/
├── .devcontainer/
│   ├── devcontainer.json
│   └── postCreateCommand.sh
├── .github/
│   ├── workflows/
│   │   └── test-notebooks.yml
│   └── ISSUE_TEMPLATE/
│       ├── teknisk-hjelp.md
│       └── innholdsforslag.md
├── README.md
├── requirements.txt
├── setup.py
├── LICENSE
├── CONTRIBUTING.md
│
├── uke01-introduksjon/
│   ├── README.md
│   ├── 01_hva_er_ai.ipynb
│   ├── 02_ai_historie_helse.ipynb
│   ├── 03_oppsett_verktoy.ipynb
│   ├── oppgaver/
│   │   ├── refleksjon_ai_definisjon.md
│   │   └── quiz_grunnbegreper.ipynb
│   └── ressurser/
│       ├── artikler.md
│       └── videoer.md
│
├── uke02-klassisk-ml/
│   ├── README.md
│   ├── 01_supervised_learning.ipynb
│   ├── 02_unsupervised_learning.ipynb
│   ├── 03_beslutningstraer.ipynb
│   ├── 04_sykdomsprediksjon_case.ipynb
│   ├── data/
│   │   ├── diabetes_sample.csv
│   │   └── heart_disease_sample.csv
│   └── oppgaver/
│       └── bygg_prediktiv_modell.ipynb
│
├── uke03-dyp-laering/
│   ├── README.md
│   ├── 01_nevrale_nettverk_intro.ipynb
│   ├── 02_cnn_bildeanalyse.ipynb
│   ├── 03_medisinsk_bildeanalyse.ipynb
│   ├── modeller/
│   │   └── pretrained_xray_classifier.pkl
│   ├── data/
│   │   └── sample_xray_images/
│   └── oppgaver/
│       └── bildeklassifisering.ipynb
│
├── uke04-generativ-ai/
│   ├── README.md
│   ├── 01_transformer_arkitektur.ipynb
│   ├── 02_llm_grunnleggende.ipynb
│   ├── 03_prompt_engineering.ipynb
│   ├── 04_chatgpt_claude_api.ipynb
│   ├── prompts/
│   │   ├── kliniske_notater.txt
│   │   ├── pasientsamtale.txt
│   │   └── journalsammendrag.txt
│   └── oppgaver/
│       └── prompt_workshop.ipynb
│
├── uke05-multimodal-ai/
│   ├── README.md
│   ├── 01_vision_language_models.ipynb
│   ├── 02_rag_systemer.ipynb
│   ├── 03_autogen_agenter.ipynb
│   ├── 04_bygg_rag_app.ipynb
│   ├── agents/
│   │   ├── medical_assistant.py
│   │   └── config.yaml
│   └── oppgaver/
│       └── lag_ai_agent.ipynb
│
├── uke06-klinisk-praksis/
│   ├── README.md
│   ├── 01_diagnostisk_ai.ipynb
│   ├── 02_ai_sykepleie.ipynb
│   ├── 03_ai_fysioterapi.ipynb
│   ├── 04_case_studier.ipynb
│   ├── cases/
│   │   ├── babylon_health.md
│   │   ├── deepmind_aki.md
│   │   └── ibm_watson_oncology.md
│   └── oppgaver/
│       └── refleksjon_case.md
│
├── uke07-velferdsteknologi/
│   ├── README.md
│   ├── 01_sensorsystemer.ipynb
│   ├── 02_robotikk_omsorg.ipynb
│   ├── 03_optimering_logistikk.ipynb
│   ├── 04_design_workshop.ipynb
│   ├── templates/
│   │   └── ai_losning_mal.md
│   └── oppgaver/
│       └── prosjektforslag.md
│
├── uke08-etikk-implementering/
│   ├── README.md
│   ├── 01_gdpr_personvern.ipynb
│   ├── 02_bias_rettferdighet.ipynb
│   ├── 03_ce_mdr_regulering.ipynb
│   ├── 04_endringsledelse.ipynb
│   ├── maler/
│   │   ├── risikovurdering.xlsx
│   │   └── implementeringsplan.docx
│   └── oppgaver/
│       └── etisk_analyse.md
│
├── uke09-fysisk-samling/
│   ├── README.md
│   ├── agenda.md
│   ├── workshops/
│   │   ├── robot_demo.md
│   │   ├── ai_verktoy.md
│   │   └── gruppearbeid.md
│   └── presentasjoner/
│       └── mal_presentasjon.pptx
│
├── uke10-eksamen/
│   ├── README.md
│   ├── 01_fremtidsperspektiver.ipynb
│   ├── 02_agentic_ai.ipynb
│   ├── eksamen/
│   │   ├── veiledning.md
│   │   ├── hjemmeeksamen_mal.md
│   │   └── vurderingskriterier.md
│   └── ressurser/
│       └── videre_laering.md
│
├── prosjekt/
│   ├── README.md
│   ├── mal_prosjektoppgave.md
│   ├── eksempler/
│   │   ├── triagering_chatbot/
│   │   ├── bildeanalyse_hud/
│   │   └── bemanningsoptimering/
│   └── vurdering/
│       └── rubrikk.md
│
├── utils/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── visualization.py
│   ├── ai_helpers.py
│   └── evaluation.py
│
├── data/
│   ├── README.md
│   ├── synthetic/
│   │   ├── generate_health_data.py
│   │   └── sample_datasets/
│   └── external/
│       └── .gitkeep
│
└── ressurser/
    ├── README.md
    ├── artikler/
    │   ├── nature_medicine/
    │   ├── lancet_digital/
    │   └── norske_studier/
    ├── videoer/
    │   └── links.md
    ├── verktoy/
    │   ├── chatgpt_guide.md
    │   ├── claude_guide.md
    │   └── github_copilot.md
    └── ordliste.md
```

## Hovedfiler

### `.devcontainer/devcontainer.json`
```json
{
  "name": "AI og Helse EVU",
  "image": "mcr.microsoft.com/devcontainers/python:3.11",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {},
    "ghcr.io/devcontainers/features/node:1": {}
  },
  "customizations": {
    "vscode": {
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "jupyter.widgetScriptSources": ["jsdelivr.com", "unpkg.com"],
        "terminal.integrated.defaultProfile.linux": "bash"
      },
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "ms-toolsai.jupyter-keymap",
        "ms-toolsai.jupyter-renderers",
        "github.copilot",
        "github.copilot-chat",
        "ms-vscode.live-server",
        "bierner.markdown-mermaid",
        "davidanson.vscode-markdownlint"
      ]
    }
  },
  "postCreateCommand": "bash .devcontainer/postCreateCommand.sh",
  "forwardPorts": [8888, 8501, 8000],
  "portsAttributes": {
    "8888": {"label": "Jupyter", "onAutoForward": "notify"},
    "8501": {"label": "Streamlit", "onAutoForward": "notify"},
    "8000": {"label": "FastAPI", "onAutoForward": "notify"}
  },
  "remoteUser": "vscode"
}
```

### `.devcontainer/postCreateCommand.sh`
```bash
#!/bin/bash
echo "🏥 Setter opp AI og Helse miljø..."

# Oppgrader pip
pip install --upgrade pip

# Installer requirements
pip install -r requirements.txt

# Konfigurer Jupyter
jupyter nbextension enable --py widgetsnbextension

# Last ned eksempeldata
python -m utils.download_sample_data

# Kjør tester
python -m pytest tests/ -v

# Sett opp pre-commit hooks
pre-commit install

echo "✅ Miljøet er klart! Velkommen til AI og Helse kurset!"
echo "📚 Start med å åpne README.md for å komme i gang"
```

### `requirements.txt`
```txt
# Core dependencies
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.14.0

# Machine Learning
scikit-learn>=1.3.0
xgboost>=1.7.0
lightgbm>=4.0.0

# Deep Learning
torch>=2.0.0
torchvision>=0.15.0
tensorflow>=2.13.0
keras>=2.13.0

# NLP and LLMs
transformers>=4.35.0
langchain>=0.1.0
openai>=1.0.0
anthropic>=0.8.0
sentence-transformers>=2.2.0

# AI Agents
autogen>=0.2.0
langchain-experimental>=0.0.40
chromadb>=0.4.0

# Medical AI
monai>=1.3.0
nibabel>=5.1.0
pydicom>=2.4.0

# Utilities
jupyter>=1.0.0
ipywidgets>=8.0.0
streamlit>=1.28.0
gradio>=4.0.0
fastapi>=0.104.0
uvicorn>=0.24.0
python-dotenv>=1.0.0
pydantic>=2.0.0

# Development
pytest>=7.4.0
black>=23.0.0
flake8>=6.0.0
pre-commit>=3.5.0
ipykernel>=6.25.0

# Data handling
openpyxl>=3.1.0
xlrd>=2.0.0
Pillow>=10.0.0
opencv-python>=4.8.0

# Visualization
altair>=5.0.0
bokeh>=3.3.0
wordcloud>=1.9.0

# API clients
requests>=2.31.0
httpx>=0.25.0
aiohttp>=3.9.0
```

### `README.md` (Repository hovedfil)
```markdown
# 🏥 AI og Helse - EVU Kurs

Velkommen til GitHub repository for kurset "AI og helse" - et 5 studiepoengs videreutdanningskurs i kunstig intelligens for helse- og omsorgssektoren.

## 🚀 Kom i gang

### Steg 1: Åpne i GitHub Codespaces

1. Klikk på den grønne "Code" knappen
2. Velg "Codespaces" fanen
3. Klikk "Create codespace on main"
4. Vent 2-3 minutter mens miljøet settes opp

### Steg 2: Første gangs oppsett

Når Codespace er klar, kjør:
```bash
python check_setup.py
```

Dette vil verifisere at alt er korrekt installert.

### Steg 3: Start med Uke 1

Naviger til `uke01-introduksjon/` og åpne `README.md` for ukens oversikt.

## 📚 Kursstruktur

- **Uke 1-6:** AI-fundamentet (AI 1.0 vs 2.0)
- **Uke 7-8:** Praktiske anvendelser
- **Uke 9:** Fysisk samling
- **Uke 10:** Eksamen

## 🛠️ Teknisk støtte

- **Forum:** [Diskusjoner](../../discussions)
- **Problemer:** [Issues](../../issues)
- **E-post:** ai-helse@universitet.no

## 📖 Læringsressurser

- [Ordliste](ressurser/ordliste.md)
- [Verktøyguider](ressurser/verktoy/)
- [Artikkelsamling](ressurser/artikler/)

## 🎯 Læringsutbytte

Etter kurset vil du kunne:
- Forstå forskjellen mellom klassisk ML og moderne AI
- Bruke generative AI-verktøy i praksis
- Vurdere AI-løsninger for helseformål
- Implementere enkle AI-systemer

## 📝 Vurdering

- Hjemmeeksamen (60%)
- Prosjektoppgave (40%)
- 3 obligatoriske refleksjonsnotater

## 🤝 Bidra

Se [CONTRIBUTING.md](CONTRIBUTING.md) for retningslinjer.

## 📄 Lisens

Dette kursmaterialet er lisensiert under CC BY-SA 4.0.

---

**Lykke til med kurset!** 🎓
```

## Eksempel på ukemodul

### `uke04-generativ-ai/README.md`
```markdown
# Uke 4: Generativ AI og Store Språkmodeller (AI 2.0)

## 🎯 Ukens læringsmål

- Forstå transformer-arkitekturen
- Mestre prompt engineering
- Bruke ChatGPT/Claude API programmatisk
- Anvende LLM for helsefaglige oppgaver

## 📚 Innhold

1. **Teori** (2 timer)
   - [01_transformer_arkitektur.ipynb](01_transformer_arkitektur.ipynb)
   - [02_llm_grunnleggende.ipynb](02_llm_grunnleggende.ipynb)

2. **Praktisk** (4 timer)
   - [03_prompt_engineering.ipynb](03_prompt_engineering.ipynb)
   - [04_chatgpt_claude_api.ipynb](04_chatgpt_claude_api.ipynb)

3. **Selvstudium** (4 timer)
   - Les: ["Attention is All You Need"](https://arxiv.org/abs/1706.03762) (første 5 sider)
   - Se: [Visualisering av Transformers](https://www.youtube.com/watch?v=...)
   - Øv: Prompt-oppgaver i `prompts/`

## 🏃 Hurtigstart

```python
# Test at alt fungerer
from transformers import pipeline

# Last inn norsk språkmodell
generator = pipeline("text-generation", model="NbAiLab/nb-gpt-j-6B")

# Generer tekst
prompt = "Pasienten presenterer symptomer på"
result = generator(prompt, max_length=50)
print(result[0]['generated_text'])
```

## ✍️ Ukens oppgaver

### Obligatorisk
- [ ] Refleksjonsnotat: "Muligheter og begrensninger med LLM i klinisk praksis"
- [ ] Quiz: Transformer-arkitektur

### Valgfritt
- [ ] Lag en prompt-samling for ditt fagområde
- [ ] Eksperimenter med few-shot learning

## 💡 Tips

- Start med enkle prompts, øk kompleksitet gradvis
- Test samme prompt i ChatGPT og Claude - sammenlign
- Dokumenter hva som fungerer/ikke fungerer

## 🔗 Ressurser

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Claude Best Practices](https://docs.anthropic.com/claude/docs)
- [Prompts for Healthcare](prompts/)

## ❓ Ofte stilte spørsmål

**Q: Trenger jeg API-nøkler?**
A: Nei, disse er inkludert i kurset via miljøvariabler.

**Q: Kan jeg bruke norsk i prompts?**
A: Ja! Moderne LLM håndterer norsk godt.

## 📅 Veiledning

- **Tirsdag kl 14-16:** Live gjennomgang (Teams)
- **Torsdag kl 10-11:** Spørretimen (frivillig)

---

*Neste uke: [Multimodal AI og moderne arkitekturer →](../uke05-multimodal-ai/)*
```

Dette rammeverket gir:
1. Komplett kursstruktur i markdown
2. GitHub Codespaces-oppsett med alle nødvendige verktøy
3. Progressive læringsmoduler fra grunnleggende til avansert
4. Praktiske øvelser tilpasset helsepersonell
5. Selvstudium-vennlig struktur
6. Ferdigkonfigurert utviklingsmiljø

-->