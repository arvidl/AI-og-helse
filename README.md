# 🏥 AI og Helse 

**Åpen variant** av (avansert) kurs i kunstig intelligens for medisinere og personell i helse- og omsorgssektoren 


## 📚 Kursstruktur

- **Del 1 (Uke 1-6):** AI Fundamentet - fra AI 1.0 til AI 2.0
- **Del 2 (Uke 7-8):** Praktiske anvendelser i medisin, helse og omsorg


## 🎯 Læringsutbytte

### Kunnskaper
- Forstå forskjellen mellom klassisk maskinlæring (AI 1.0), dyplæring og generativ AI (AI 2.0)
- Kjenne til praktiske anvendelser av AI i helse- og omsorgstjenesten
- Forstå grunnleggende prinsipper for AI-støttet analyse, optimering og beslutning
- Ha innsikt i etiske og regulatoriske aspekter ved AI i helse og medisin

### Ferdigheter
- Bruke generative AI-verktøy (ChatGPT, Claude, Gemini, ...) for faglige oppgaver i medisin og helse
- Vurdere egnethet av AI-løsninger for konkrete problemstillinger
- Identifisere muligheter for AI-støtte i egen arbeidshverdag
- Kritisk evaluere AI-systemer og deres begrensninger (og muligheter)

### Bruk av kurset
"... på svømmekurs bør man oppholde seg mye i bassenget ..."
- Det anbefales å "gå i bassenget" (= eksperimentere med notebooks)
- For noen i målgruppen, kan et realistisk læringsutbytte oppnås ved kun å **lese**, **inspisere**, **kontemplere**: tekst, kode, figurer og referanser rett i GitHub-repositoriet (https://github.com/arvidl/AI-og-helse) -  "holde seg på land ...", samt bruke en AI-sparringspartner

## 📂 Repo-struktur

```
AI-og-helse/
├── .devcontainer/               # GitHub Codespaces konfigurasjon
├── uke01-introduksjon/          # Introduksjon til AI
├── uke02-klassisk-ml/           # Klassisk maskinlæring
├── uke03-dyplæring/             # Dyplæring og nevrale nettverk
├── uke04-generativ-ai/          # Store språkmodeller
├── uke05-multimodal-ai/         # RAG og AI-agenter
├── uke06-klinisk-praksis/       # AI i helsefag
├── uke07-velferdsteknologi/     # Robotikk og optimering
├── uke08-etikk-implementering/  # Etikk, bias/fairness, GDPR, MDR, EU AI Act
├── prosjekt/                    # Prosjektoppgave maler
├── utils/                       # Hjelpefunksjoner
└── data/                        # Eksempeldata
```

## 💻 Teknologi

- **Python 3.12+**
- **Jupyter Notebooks** for interaktiv læring
- **GitHub Codespaces** for sky-basert utvikling
- **Google Colabratory** for sky-basert notebook-kjøring og eksperimentering
- **AI-verktøy:** OpenAI (gpt-), Anthropic (claude-), Scikit-learn, PyTorch, ...


## 🛠️ Teknisk støtte

- **GitHub Issues:** [Rapporter problemer](https://github.com/arvidl/AI-og-helse/issues)
- **Diskusjoner:** Kollegaer, Medstudenter, AI-sparringpartner(e)


## 📖 Læringsressurser

- [Ordliste](ressurser/ordliste.md)
- [Verktøyguider](ressurser/verktoy/)
- [Artikkelsamling](ressurser/artikler/)


## 👥 Målgruppe

- Helsepersonell (leger, sykepleiere, radiografer, terapeuter, psykologer)
- Ansatte i omsorgstjenesten (deler av kurset)
- Ledere i helse og omsorg (deler av kurset)
- IT- og digitaliseringsansvarlige (deler av kurset)
- Kvalitets- og utviklingsrådgivere (deler av kurset)

## 📅 Praktisk informasjon

- **Varighet:** 8 uker 
- **Arbeidsomfang:** 10-12 timer per uke
- **Læringsspråk (i Jupyter notatbøker):** Norsk (+ engelske fagtermer, e.g. "notebooks")


## 📄 Lisens

Dette kursmaterialet er lisensiert under [CC BY-SA 4.0](LICENSE) / [MIT License](https://github.com/arvidl/AI-og-helse/blob/main/LICENSE) Copyright (c) 2025 Arvid Lundervold

## 🙏 Bidragsytere

- Arvid Lundervold
- [Bidragsytere](CONTRIBUTING.md)


### 🛠️ Hvordan kurset er laget og ressurser brukt

- bygger på domenekunnskap, godt nettverk av fagfeller og entusiasme for feltet
- bruk av AI kode-editoren Cursor Ultra 
- utviklet på en MacBook Pro (M4 Max) 
- diverse lisenser (GitHub, OpenAI, Anthropic, Perplexity, Gooogle) 
- ca. 40 timeverk (for basisdelen) 


------

## 🚀 Kom i gang


### Bruk Google Colab (enkleste alternativ)

Gå til https://github.com/arvidl/AI-og-helse/blob/main/README.md og sjekk Repo-struktur og aktuell uke01-, ..., uke08-

f.eks. [uke01-introduksjon](https://github.com/arvidl/AI-og-helse/tree/main/uke01-introduksjon)

1. For hver notebook, trykk på [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke01-introduksjon/00-velkommen.ipynb) 
2. Notebooken vises da i din nettleser
3. Aksepter at den ikke er autorisert av Google ("Run anyway")
4. Lær deg bruk av Python og [Jupyter Notebooks](https://colab.research.google.com/github/jckantor/CBE30338/blob/master/docs/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.ipynb) i Google Colab ([FAQ](https://research.google.com/colaboratory/faq.html))


### Bruk GitHub Codespaces (for de som ønsker et sky-basert utviklingsmiljø med VS Code)

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


### For lokal utvikling - Anaconda (anbefalt for Mac/Linux/PC)

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


## **API-nøkler (for lokal kjøring)**


### **NB:** Det kreves at API-nøkler blir konfigurert av kursdeltager:

Dvs. hver deltaker skaffer selv, lagrer og bruker sine egne API-nøkler

Her er en strukturert måte å gjøre det på:

---

#### 1. Skaff egne API-nøkler

Hver deltaker må selv registrere seg:

* **OpenAI:** [platform.openai.com](https://platform.openai.com/)
* **Anthropic:** [console.anthropic.com](https://console.anthropic.com/)

Begge krever at man legger inn kort/betalingsinfo (med gratis startkreditter for nye brukere).

---

### 2. Hvordan lagre nøklene trygt

Du kan velge én av to enkle metoder:

**a) `.env`-fil (anbefalt)**

1. Lag en fil i samme mappe som notebooken med navnet `.env`
2. Legg inn:

   ```
   OPENAI_API_KEY=sk-xxxx
   ANTHROPIC_API_KEY=sk-ant-xxxx
   ```
3. Installer `python-dotenv` (én gang):

   ```bash
   pip install python-dotenv
   ```
4. I notebooken:

   ```python
   from dotenv import load_dotenv
   load_dotenv()

   import os
   openai_key = os.getenv("OPENAI_API_KEY")
   anthropic_key = os.getenv("ANTHROPIC_API_KEY")
   ```

**b) Direkte miljøvariabler (mer "avansert")**

* I terminal (før du starter Jupyter):

  ```bash
  export OPENAI_API_KEY="sk-xxxx"
  export ANTHROPIC_API_KEY="sk-ant-xxxx"
  ```
* Notebooken bruker `os.getenv()` som i eksempelet over.

---

#### 3. Bruke nøklene i kode

**OpenAI (GPT-modeller):**

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hei fra OpenAI!"}]
)
print(response.choices[0].message.content)
```

**Anthropic (Claude-modeller):**

```python
from anthropic import Anthropic
import os

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=100,
    messages=[{"role": "user", "content": "Hei fra Claude!"}]
)
print(response.content[0].text)
```

### NB!
* Husk, ikke dele noen egne nøkler i kursmaterialet – hver deltaker har ansvar for sine.
* Der det kan være aktuelt, har vi lagt inn et sjekksteg i notebooken som gir en feilmelding hvis nøkkel mangler:

  ```python
  if not openai_key or not anthropic_key:
      raise ValueError("Mangler API-nøkkel. Sett den i .env-filen først!")
  ```


## **API-nøkler (for kjøring i skyen)**

Dette er avhengig om du kjører i **Google Colab** eller i **GitHub Codespaces**

For nærmere beskrivelse, se notebooken [`intro_openai_anthropic.ipynb`](./intro_openai_anthropic.ipynb).



---

#### 5. Oppsummering

* Deltakere skaffer **egne nøkler** fra OpenAI og Anthropic.
* Nøklene lagres lokalt i `.env` eller som miljøvariabler dersom du kjører lokalt
* Dersom du kjører i skyen må du konsultere [`intro_openai_anthropic.ipynb`](./intro_openai_anthropic.ipynb).
* Aktuelle Notebooks er ferdig satt opp til å hente nøkler og bruke dem.

---





**Lykke til med kurset!** 🎓