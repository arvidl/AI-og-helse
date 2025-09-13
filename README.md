# 🏥 AI og Helse 

**Åpen variant** av kurs i kunstig intelligens for helse- og omsorgssektoren 


## 📚 Kursstruktur

- **Del 1 (Uke 1-6):** AI Fundamentet - Fra AI 1.0 til AI 2.0
- **Del 2 (Uke 7-8):** Praktiske anvendelser i helse og omsorg
- **<strike>Del 3 (Uke 9-10):</strike>** <strike>Fysisk samling og eksamen</strike> (*kun aktuelt for studiepoeng-givende kurs-variant ved undervsiningsinstitusjon*) 

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
├── prosjekt/               # Prosjektoppgave maler
├── utils/                  # Hjelpefunksjoner
└── data/                   # Eksempeldata
```

## 💻 Teknologi

- **Python 3.12+**
- **Jupyter Notebooks** for interaktiv læring
- **GitHub Codespaces** for cloud-basert utvikling
- **AI-verktøy:** OpenAI, Anthropic, Autogen, LangChain

## 📝 <strike>Vurdering</strike> (ikke aktuelt i åpent kurs)
<!-- 
- **Hjemmeeksamen** (60%): 48-timers eksamen i uke 10
- **Prosjektoppgave** (40%): Praktisk anvendelse av AI
- **Obligatorisk:** 3 refleksjonsnotater (godkjent/ikke godkjent)

-->

## 🛠️ Teknisk støtte

- **GitHub Issues:** [Rapporter problemer](https://github.com/arvidl/AI-og-helse/issues)
- **Diskusjoner:** [Kursforum](https://github.com/arvidl/AI-og-helse/discussions)
<!-- - **E-post:** Kursansvarlig
  
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

- **Varighet:** 8 uker (<strike>10 uker i vårsemester</strike>)
- **Arbeidsomfang:** 10-12 timer per uke
- **Undervisningsspråk:** Norsk
- <strike>**Fysisk samling:** 1 dag i uke 9 (under planlegging)</strike>

## 📄 Lisens

Dette kursmaterialet er lisensiert under [CC BY-SA 4.0](LICENSE).

## 🙏 Bidragsytere

- Arvid Lundervold
- [Bidragsytere](CONTRIBUTING.md)



------

## 🚀 Kom i gang

### Bruk GitHub Codespaces (anbefalt)

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

### Bruk Google Colab (enklere alternativ)

1. For hver notebook, trykk på [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke01-introduksjon/00-velkommen.ipynb) 
2. Notebooken vises da i din nettleser
3. Aksepter at den ikke er autorisert av Google (Run anyway)
4. Lær deg bruk av Python og [Jupyter Notebooks](https://colab.research.google.com/github/jckantor/CBE30338/blob/master/docs/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.ipynb) i Google Colab ([FAQ](https://research.google.com/colaboratory/faq.html))

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

**Lykke til med kurset!** 🎓