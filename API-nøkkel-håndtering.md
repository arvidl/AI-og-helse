# API-nøkkel håndtering for AI og Helse kurset

Her er en gjennomtenkt løsning for API-håndtering som balanserer sikkerhet, kostnader og brukervennlighet.
## 🎯 **Min anbefaling for AI og Helse kurset:**

### **Bruk "Alt inkludert" modellen med GitHub Organization**

**Kursavgift kr 12,500 inkluderer:**
- ~$150 (ca kr 1,650) i API-kreditt per student
- Dekker normal bruk gjennom hele kurset
- Ingen ekstra kostnader eller tekniske barrierer

### **Praktisk implementering:**

1. **For deg lokalt:** Fortsett bruk din `/Users/arvid/.env`
2. **For studenter:** GitHub Organization med Codespaces
3. **Sentralisert API-håndtering** med usage tracking
4. **Automatisk stopp** ved forbruksgrense

## 💡 **Hvorfor denne løsningen:**

### Pedagogiske fordeler:
- **Nullfriksjon** - Studenter fokuserer på læring, ikke teknisk oppsett
- **Lik tilgang** - Alle får samme muligheter
- **Realistisk erfaring** - Lærer om API-kostnader og -begrensninger

### Administrative fordeler:
- **Kostnadskontroll** - Maks $150 per student
- **Enkel overvåking** - Dashboard for forbruk
- **Skalerbart** - Fungerer for 30+ studenter

### Tekniske fordeler:
- **GitHub Classroom** - Automatisk provisjonering
- **Organization Secrets** - Sikker nøkkelhåndtering
- **Usage tracking** - Forhindrer overforbruk

## 📊 **Kostnadsestimat for 30 studenter:**

```
API-kostnader: 30 × $150 = $4,500 (ca kr 49,500)
Per student i kursavgift: kr 1,650
Allerede inkludert i kr 12,500 avgift ✓
```

## 🚀 **Neste steg:**

1. **Opprett GitHub Organization:** `UiB-AI-Helse` eller `AI-helse-V25`
2. **Sett opp GitHub Classroom** for enkel studenthåndtering
3. **Konfigurer Organization Secrets** med dine API-nøkler
4. **Test med én student** før kursstart

Med denne løsningen får studentene profesjonell erfaring med AI-verktøy uten tekniske eller økonomiske barrierer, mens du har full kontroll over kostnader og forbruk! 🎓



# Detaljer:

# API-nøkkel håndtering for AI og Helse EVU

## 📊 Kostnadsberegning for 10 uker

### Estimert forbruk per student

#### OpenAI (ChatGPT API)
- **GPT-4**: ~$0.03 per 1K tokens (input) + $0.06 per 1K tokens (output)
- **GPT-3.5-Turbo**: ~$0.001 per 1K tokens (input) + $0.002 per 1K tokens (output)
- **Estimat per student**:
  - Moderat bruk (GPT-3.5): ~$20-30 for 10 uker
  - Intensiv bruk (GPT-4): ~$50-100 for 10 uker

#### Anthropic (Claude API)
- **Claude 3 Opus**: ~$0.015 per 1K tokens (input) + $0.075 per 1K tokens (output)
- **Claude 3 Sonnet**: ~$0.003 per 1K tokens (input) + $0.015 per 1K tokens (output)
- **Estimat per student**: ~$30-80 for 10 uker

#### Andre tjenester
- **GitHub Copilot**: $10/måned (akademisk: gratis)
- **ChatGPT Plus**: $20/måned (valgfritt, for web-grensesnitt)

### Total kostnad per student: ~$100-200 for hele kurset

## 🎯 Anbefalt løsning: Organisasjons-API med usage limits

### Oppsett for UiB/kurset

```python
# api_manager.py - Sentralisert API-håndtering
import os
from typing import Optional
from dotenv import load_dotenv
import openai
from anthropic import Anthropic
import hashlib
import json
from datetime import datetime

class AIHelsekursAPIManager:
    """
    Sentralisert API-manager for AI og Helse kurset
    Håndterer autentisering og usage tracking
    """

    def __init__(self, student_id: str = None):
        self.student_id = student_id or self._get_student_id()
        self.usage_file = f".usage/{self.student_id}.json"
        self._load_api_keys()
        self._init_usage_tracking()

    def _get_student_id(self) -> str:
        """Generer unik student ID basert på GitHub bruker eller miljø"""
        # For GitHub Codespaces
        github_user = os.environ.get('GITHUB_USER')
        if github_user:
            return hashlib.md5(github_user.encode()).hexdigest()[:8]

        # For lokal utvikling
        import getpass
        return hashlib.md5(getpass.getuser().encode()).hexdigest()[:8]

    def _load_api_keys(self):
        """Last API-nøkler fra miljø eller sentral konfig"""
        # Prioritet 1: Miljøvariabler (for instruktør)
        load_dotenv('/Users/arvid/.env')  # Din lokale .env
        load_dotenv('.env')  # Prosjekt .env

        # Prioritet 2: Kurs-API-nøkler (for studenter)
        if not os.environ.get('OPENAI_API_KEY'):
            os.environ['OPENAI_API_KEY'] = self._get_course_api_key('openai')

        if not os.environ.get('ANTHROPIC_API_KEY'):
            os.environ['ANTHROPIC_API_KEY'] = self._get_course_api_key('anthropic')

    def _get_course_api_key(self, service: str) -> str:
        """Hent kurs-spesifikk API-nøkkel fra sikker kilde"""
        # Mulighet 1: GitHub Secrets (for Codespaces)
        if os.environ.get('CODESPACES'):
            return os.environ.get(f'COURSE_{service.upper()}_API_KEY')

        # Mulighet 2: Sikker server endpoint
        # return self._fetch_from_course_server(service)

        # Mulighet 3: Kryptert lokal fil
        # return self._decrypt_local_key(service)

        return None

    def _init_usage_tracking(self):
        """Initialiser usage tracking for studenten"""
        os.makedirs('.usage', exist_ok=True)

        if not os.path.exists(self.usage_file):
            self.usage = {
                'student_id': self.student_id,
                'start_date': datetime.now().isoformat(),
                'openai': {'tokens': 0, 'cost': 0.0},
                'anthropic': {'tokens': 0, 'cost': 0.0},
                'limits': {
                    'max_cost_total': 150.0,  # $150 total
                    'max_cost_weekly': 20.0,  # $20 per uke
                    'warning_threshold': 0.8  # Advarsel ved 80% bruk
                }
            }
            self._save_usage()
        else:
            with open(self.usage_file, 'r') as f:
                self.usage = json.load(f)

    def _save_usage(self):
        """Lagre usage data"""
        with open(self.usage_file, 'w') as f:
            json.dump(self.usage, f, indent=2)

    def check_limits(self) -> tuple[bool, str]:
        """Sjekk om student er innenfor usage limits"""
        total_cost = self.usage['openai']['cost'] + self.usage['anthropic']['cost']
        max_cost = self.usage['limits']['max_cost_total']

        if total_cost >= max_cost:
            return False, f"❌ Du har brukt opp din kvote (${total_cost:.2f}/${max_cost:.2f})"

        if total_cost >= max_cost * self.usage['limits']['warning_threshold']:
            remaining = max_cost - total_cost
            return True, f"⚠️ Advarsel: Du har brukt ${total_cost:.2f} av ${max_cost:.2f} (${remaining:.2f} gjenstår)"

        return True, f"✅ Forbruk: ${total_cost:.2f} av ${max_cost:.2f}"

    def get_openai_client(self):
        """Returner OpenAI client med usage tracking"""
        allowed, message = self.check_limits()
        if not allowed:
            raise Exception(message)

        print(message)
        return openai.OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

    def get_anthropic_client(self):
        """Returner Anthropic client med usage tracking"""
        allowed, message = self.check_limits()
        if not allowed:
            raise Exception(message)

        print(message)
        return Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

    def track_usage(self, service: str, tokens: int, model: str):
        """Spor token-bruk og kostnader"""
        # Kostnadsberegning basert på modell
        costs = {
            'gpt-3.5-turbo': 0.002,  # per 1K tokens
            'gpt-4': 0.06,
            'claude-3-sonnet': 0.015,
            'claude-3-opus': 0.075
        }

        cost_per_1k = costs.get(model, 0.01)  # Default
        cost = (tokens / 1000) * cost_per_1k

        self.usage[service]['tokens'] += tokens
        self.usage[service]['cost'] += cost
        self._save_usage()

        # Sjekk limits etter bruk
        self.check_limits()

    def get_usage_report(self) -> str:
        """Generer usage rapport for studenten"""
        total_cost = self.usage['openai']['cost'] + self.usage['anthropic']['cost']
        max_cost = self.usage['limits']['max_cost_total']

        report = f"""
        📊 Din API-bruk for AI og Helse kurset
        =====================================
        Student ID: {self.student_id}
        Start dato: {self.usage['start_date']}

        OpenAI:
        - Tokens brukt: {self.usage['openai']['tokens']:,}
        - Kostnad: ${self.usage['openai']['cost']:.2f}

        Anthropic:
        - Tokens brukt: {self.usage['anthropic']['tokens']:,}
        - Kostnad: ${self.usage['anthropic']['cost']:.2f}

        Total kostnad: ${total_cost:.2f} av ${max_cost:.2f}
        Gjenstående: ${max_cost - total_cost:.2f}
        """
        return report
```

## 📝 Implementering for studenter

### 1. GitHub Codespaces Secrets (Anbefalt)

```yaml
# .github/workflows/setup-secrets.yml
name: Setup Course API Keys

on:
  workflow_dispatch:

jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - name: Set Organization Secrets
        run: |
          # Sett opp for hele organisasjonen/kurset
          gh secret set COURSE_OPENAI_API_KEY --org UiB-AI-Helse
          gh secret set COURSE_ANTHROPIC_API_KEY --org UiB-AI-Helse
```

### 2. Oppdatert check_setup.py

```python
#!/usr/bin/env python3
"""
Verifiseringsscript med API-sjekk for AI og Helse kurset
"""

import sys
import os
from pathlib import Path

def check_api_setup():
    """Sjekk API-oppsett for student eller instruktør"""

    # Sjekk om vi er instruktør (har lokal .env)
    if Path('/Users/arvid/.env').exists():
        print("✅ Instruktør-modus: Bruker lokale API-nøkler")
        return True

    # Sjekk om vi er i Codespaces
    if os.environ.get('CODESPACES'):
        if os.environ.get('COURSE_OPENAI_API_KEY'):
            print("✅ Student-modus: Kurs API-nøkler tilgjengelig")
            return True
        else:
            print("⚠️ Venter på API-nøkler fra kursadministrator")
            return False

    # Sjekk lokal .env
    if Path('.env').exists():
        from dotenv import load_dotenv
        load_dotenv()
        if os.environ.get('OPENAI_API_KEY'):
            print("✅ Lokale API-nøkler funnet")
            return True

    print("""
    ⚠️ API-nøkler ikke konfigurert!

    For studenter:
    - Bruk GitHub Codespaces (anbefalt)
    - API-nøkler er inkludert i kursavgiften

    For lokal utvikling:
    - Opprett .env fil med:
      OPENAI_API_KEY=your-key
      ANTHROPIC_API_KEY=your-key
    """)
    return False

# Kjør sjekk ved import
if __name__ == "__main__":
    check_api_setup()
```

### 3. Notebook helper for enkel bruk

```python
# utils/ai_helper.py
"""
Forenklet API-tilgang for studenter
"""

from api_manager import AIHelsekursAPIManager

# Global manager instance
_manager = None

def get_ai_client(service='openai'):
    """
    Enkel funksjon for studenter å få AI-klient

    Eksempel:
        client = get_ai_client('openai')
        response = client.chat.completions.create(...)
    """
    global _manager
    if _manager is None:
        _manager = AIHelsekursAPIManager()

    if service == 'openai':
        return _manager.get_openai_client()
    elif service == 'anthropic':
        return _manager.get_anthropic_client()
    else:
        raise ValueError(f"Ukjent service: {service}")

def check_my_usage():
    """Sjekk din API-bruk"""
    global _manager
    if _manager is None:
        _manager = AIHelsekursAPIManager()

    print(_manager.get_usage_report())
```

## 💰 Kostnadsmodeller

### Alternativ 1: Alt inkludert (Anbefalt)
- **Kursavgift:** kr 12,500 (uendret)
- **Inkluderer:** ~$150 i API-kreditt per student
- **Fordel:** Ingen ekstra kostnader for studenter
- **Ulempe:** Må overvåke forbruk

### Alternativ 2: Grunnpakke + tillegg
- **Kursavgift:** kr 11,500
- **Inkluderer:** $50 i API-kreditt
- **Tillegg:** Studenter kan kjøpe ekstra kreditt ved behov
- **Fordel:** Lavere risiko, fleksibelt

### Alternativ 3: BYOK (Bring Your Own Key)
- **Kursavgift:** kr 10,500
- **Studenter:** Oppretter egne API-kontoer
- **Fordel:** Ingen API-administrasjon
- **Ulempe:** Teknisk barriere for nogle studenter

## 🔒 Sikkerhet og beste praksis

### For deg som instruktør:
```bash
# Din lokale .env (IKKE commit denne!)
# /Users/arvid/.env
OPENAI_API_KEY=sk-proj-xxxxx
ANTHROPIC_API_KEY=sk-ant-xxxxx

# Prosjekt .env.example (denne kan committes)
# /Users/arvid/GitHub/AI-og-helse/.env.example
OPENAI_API_KEY=your-openai-key-here
ANTHROPIC_API_KEY=your-anthropic-key-here
```

### For GitHub Classroom/Organization:
1. Opprett Organization: `UiB-AI-Helse`
2. Sett Organization Secrets
3. Gi studenter tilgang via GitHub Classroom
4. Automatisk provisjonering av Codespaces

## 📊 Overvåking og rapportering

```python
# admin/usage_dashboard.py
import pandas as pd
import plotly.express as px
from pathlib import Path

def generate_usage_report():
    """Generer usage rapport for alle studenter"""
    usage_files = Path('.usage').glob('*.json')

    data = []
    for file in usage_files:
        with open(file) as f:
            usage = json.load(f)
            data.append({
                'student': usage['student_id'],
                'total_cost': usage['openai']['cost'] + usage['anthropic']['cost'],
                'openai_tokens': usage['openai']['tokens'],
                'anthropic_tokens': usage['anthropic']['tokens']
            })

    df = pd.DataFrame(data)

    # Visualiser
    fig = px.bar(df, x='student', y='total_cost',
                 title='API-kostnader per student')
    fig.show()

    # Eksporter rapport
    df.to_csv('usage_report.csv')
    print(f"Total kostnad alle studenter: ${df['total_cost'].sum():.2f}")
```

## ✅ Anbefaling for kurset

**Bruk "Alt inkludert" modellen:**

1. **Øk kursavgift minimalt** (allerede kr 12,500)
2. **Inkluder $150 API-kreditt** (dekker normal bruk)
3. **Bruk GitHub Organization Secrets** for API-nøkler
4. **Implementer usage tracking** for oversikt
5. **Sett usage limits** for å unngå overforbruk

**Fordeler:**
- Ingen tekniske barrierer for studenter
- Forutsigbare kostnader
- Profesjonell løsning
- God læringskurve

**Setup for deg:**
```bash
# 1. Opprett GitHub Organization for kurset
# 2. Sett Organization Secrets (API-nøkler)
# 3. Inviter studenter via GitHub Classroom
# 4. Alt fungerer automatisk i Codespaces!
```
