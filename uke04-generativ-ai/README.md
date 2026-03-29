# Uke 4: Generativ AI og store språkmodeller

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
   - Les: [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
   - Øv: Prompt-oppgaver i [`prompts/`](./prompts)

## 🏃 Hurtigstart

```python
import os

print("OPENAI_API_KEY finnes:", bool(os.getenv("OPENAI_API_KEY")))
print("ANTHROPIC_API_KEY finnes:", bool(os.getenv("ANTHROPIC_API_KEY")))
```

For API-notebookene trenger du egne nøkler. Se toppnivå-`README.md` og `../intro_openai_anthropic.ipynb` for oppsett lokalt og i Colab.

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
- [Anthropic Documentation](https://docs.anthropic.com/)
- [Prompts for Healthcare](prompts/)

## ❓ Ofte stilte spørsmål

**Q: Trenger jeg API-nøkler?**
A: Ja, for notebookene som faktisk bruker OpenAI- eller Anthropic-API-er. Flere av eksemplene kan likevel leses og delvis prøves uten nøkler.

**Q: Kan jeg bruke norsk i prompts?**
A: Ja! Moderne LLM håndterer norsk godt.

**Q: Kan jeg bruke dette i Colab?**
A: Ja, men API-notebookene krever manuell nøkkeloppsett. Se `../COLAB_SETUP.md` og `../COLAB_COMPATIBILITY_CHECKLIST.md`.

## 📅 Veiledning

- **Tirsdag kl 14-16:** Live gjennomgang (Teams)
- **Torsdag kl 10-11:** Spørretimen (frivillig)

---

*Neste uke: [Multimodal AI og moderne arkitekturer →](../uke05-multimodal-ai/)*



## 📁 **Struktur Uke 4 oppsummert:**

### **Hovedfiler:**
1. **README.md** - Ukens oversikt med læringsmål og hurtigstart
2. **01_transformer_arkitektur.ipynb** - Grunnleggende forståelse av attention og transformers
3. **02_llm_grunnleggende.ipynb** - Tokens, temperature, og hvordan LLM fungerer
4. **03_prompt_engineering.ipynb** - Praktiske teknikker for effektive prompts
5. **04_chatgpt_claude_api.ipynb** - API-integrasjon med feilhåndtering og caching

### **Prompt-eksempler (prompts/):**
- **kliniske_notater.txt** - SOAP-notater, epikriser, kvalitetssikring
- **pasientsamtale.txt** - Anamnese, empati, vanskelige samtaler
- **journalsammendrag.txt** - Ulike typer sammendrag for journaler

### **Workshop (oppgaver/):**
- **prompt_workshop.ipynb** - Interaktive øvelser med progressiv vanskelighetsgrad

## 🎯 **Pedagogiske høydepunkter:**

### **Praktisk fokus:**
- Alle eksempler er helserelaterte
- Kode som faktisk kan kjøres (med eller uten API)
- Gradvis progresjon fra enkelt til avansert

### **Sikkerhet innebygd:**
- Etiske retningslinjer i hver notebook
- Sikkerhetsinstruksjoner i prompts
- Diskusjon av begrensninger

### **Interaktivt:**
- Workshop med "fyll inn selv" seksjoner
- Sammenligning av ulike tilnærminger
- Edge case testing



<!--

# --------- UKE 4 PLAN ----


Perfekt! Jeg har laget et komplett minimalistisk utkast for **Uke 04: Generativ AI** med alle filene du ba om. Her er en oversikt:

## 📁 **Struktur opprettet:**

### **Hovedfiler:**
1. **README.md** - Ukens oversikt med læringsmål og hurtigstart
2. **01_transformer_arkitektur.ipynb** - Grunnleggende forståelse av attention og transformers
3. **02_llm_grunnleggende.ipynb** - Tokens, temperature, og hvordan LLM fungerer
4. **03_prompt_engineering.ipynb** - Praktiske teknikker for effektive prompts
5. **04_chatgpt_claude_api.ipynb** - API-integrasjon med feilhåndtering og caching

### **Prompt-eksempler (prompts/):**
- **kliniske_notater.txt** - SOAP-notater, epikriser, kvalitetssikring
- **pasientsamtale.txt** - Anamnese, empati, vanskelige samtaler
- **journalsammendrag.txt** - Ulike typer sammendrag for journaler

### **Workshop (oppgaver/):**
- **prompt_workshop.ipynb** - Interaktive øvelser med progressiv vanskelighetsgrad

## 🎯 **Pedagogiske høydepunkter:**

### **Praktisk fokus:**
- Alle eksempler er helserelaterte
- Kode som faktisk kan kjøres (med eller uten API)
- Gradvis progresjon fra enkelt til avansert

### **Sikkerhet innebygd:**
- Etiske retningslinjer i hver notebook
- Sikkerhetsinstruksjoner i prompts
- Diskusjon av begrensninger

### **Interaktivt:**
- Workshop med "fyll inn selv" seksjoner
- Sammenligning av ulike tilnærminger
- Edge case testing

## 💡 **For å bruke dette:**

```bash
# Opprett struktur i ditt repo
cd /Users/arvid/GitHub/AI-og-helse
mkdir -p uke04-generativ-ai/prompts
mkdir -p uke04-generativ-ai/oppgaver

# Kopier innholdet fra artifacts til respektive filer
# Hver seksjon i artifactet = én fil

# Test at notebooks fungerer
cd uke04-generativ-ai
jupyter lab
```

## 🔧 **Tilpasninger du kan gjøre:**

1. **Legg til faktiske API-nøkler** i `.env` for live demo
2. **Utvid prompt-eksemplene** med reelle case fra praksis  
3. **Inkluder videolenker** til forelesninger i README
4. **Legg til løsningsforslag** i separate filer

Dette gir studentene en solid, praktisk introduksjon til generativ AI med direkte relevans for helsesektoren! 🚀









# Uke 04: Generativ AI - Filer og Innhold

## 📁 uke04-generativ-ai/README.md

```markdown
# Uke 4: Generativ AI og Store Språkmodeller

## 🎯 Læringsmål
- Forstå transformer-arkitekturen og attention-mekanismer
- Mestre prompt engineering for helsefaglige oppgaver
- Bruke ChatGPT og Claude API programmatisk
- Anvende LLM for klinisk dokumentasjon

## 📚 Innhold
1. **Transformer-arkitektur** - Grunnlaget for moderne AI
2. **LLM Grunnleggende** - Hvordan språkmodeller fungerer
3. **Prompt Engineering** - Kunsten å kommunisere med AI
4. **API-integrasjon** - Praktisk bruk av ChatGPT og Claude

## 🏃 Hurtigstart
```python
# Test at alt fungerer
from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hei, er du klar?"}]
)
print(response.choices[0].message.content)
```

## ✍️ Ukens oppgaver
- [ ] Les gjennom alle notebooks
- [ ] Gjennomfør prompt workshop
- [ ] Eksperimenter med ulike prompts i `prompts/` mappen
- [ ] Reflekter over etiske aspekter ved AI i helsevesenet

## 🔗 Ressurser
- [OpenAI Documentation](https://platform.openai.com/docs)
- [Anthropic Claude Docs](https://docs.anthropic.com)
- [Attention Is All You Need (Paper)](https://arxiv.org/abs/1706.03762)
```

---

## 📓 01_transformer_arkitektur.ipynb

```python
# %% [markdown]
"""
# 🧠 Transformer-arkitekturen: Grunnlaget for moderne AI

## Læringsmål
- Forstå self-attention mekanismen
- Visualisere hvordan transformers prosesserer tekst
- Koble arkitekturen til praktisk bruk i helsevesenet
"""

# %%
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn

print("📚 Transformer-arkitektur - La oss starte!")

# %% [markdown]
"""
## Hva er Attention?

Attention lar modellen fokusere på relevante deler av inputen.
I medisinsk kontekst: Når vi leser "pasienten har diabetes", 
må AI forstå at "diabetes" er relatert til "pasienten".
"""

# %%
# Enkel demonstrasjon av attention
def simple_attention(query, keys, values):
    """
    Forenklet attention-mekanisme
    """
    # Beregn likhet mellom query og keys
    scores = np.dot(query, keys.T)
    
    # Normaliser med softmax
    weights = np.exp(scores) / np.sum(np.exp(scores))
    
    # Vektet sum av values
    output = np.dot(weights, values)
    
    return output, weights

# Eksempel: Medisinsk setning
words = ["Pasienten", "har", "alvorlig", "diabetes", "type", "2"]
word_embeddings = np.random.randn(6, 4)  # 6 ord, 4 dimensjoner

# La oss finne attention for ordet "diabetes"
query_idx = 3  # "diabetes"
query = word_embeddings[query_idx]

output, attention_weights = simple_attention(
    query, word_embeddings, word_embeddings
)

# Visualiser attention
plt.figure(figsize=(10, 3))
plt.bar(words, attention_weights)
plt.title(f'Attention-vekter for ordet "{words[query_idx]}"')
plt.ylabel('Attention-vekt')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print(f"Høyest attention: {words[np.argmax(attention_weights)]}")

# %% [markdown]
"""
## Multi-Head Attention

I praksis bruker transformers multiple attention "heads" 
som kan fokusere på ulike aspekter samtidig:
- Head 1: Grammatiske relasjoner
- Head 2: Semantiske koblinger
- Head 3: Medisinsk terminologi
"""

# %%
class SimpleTransformerBlock(nn.Module):
    """Forenklet transformer-blokk for demonstrasjon"""
    
    def __init__(self, d_model=512, n_heads=8):
        super().__init__()
        self.attention = nn.MultiheadAttention(d_model, n_heads)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.feed_forward = nn.Sequential(
            nn.Linear(d_model, 2048),
            nn.ReLU(),
            nn.Linear(2048, d_model)
        )
    
    def forward(self, x):
        # Self-attention
        attn_output, _ = self.attention(x, x, x)
        x = self.norm1(x + attn_output)
        
        # Feed-forward
        ff_output = self.feed_forward(x)
        x = self.norm2(x + ff_output)
        
        return x

# Demonstrer
model = SimpleTransformerBlock()
print(f"Transformer-blokk opprettet med {sum(p.numel() for p in model.parameters()):,} parametere")

# %% [markdown]
"""
## 💡 Praktisk betydning for helsevesenet

Transformers muliggjør:
1. **Journalsammendrag**: Automatisk oppsummering av lange journaler
2. **Diagnosestøtte**: Koble symptomer til mulige diagnoser
3. **Medisininteraksjoner**: Oppdage potensielle legemiddelinteraksjoner
4. **Pasientkommunikasjon**: Forklare medisinske termer enkelt

### Refleksjon
Hvordan kan attention-mekanismen hjelpe med å identifisere 
viktig informasjon i en pasientjournal?
"""
```

---

## 📓 02_llm_grunnleggende.ipynb

```python
# %% [markdown]
"""
# 🤖 Store Språkmodeller (LLM) - Grunnleggende konsepter

## Læringsmål
- Forstå hvordan LLM genererer tekst
- Lære om tokens og embeddings
- Utforske temperature og sampling
"""

# %%
import tiktoken
from transformers import AutoTokenizer
import numpy as np

print("🚀 LLM Grunnleggende - Fra tekst til AI-forståelse")

# %% [markdown]
"""
## Tokenisering: Hvordan AI leser tekst
"""

# %%
# Bruk OpenAI's tokenizer
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Medisinsk eksempel
tekst = "Pasienten har diabetes mellitus type 2 og hypertensjon."
tokens = encoding.encode(tekst)
token_strings = [encoding.decode([token]) for token in tokens]

print(f"Original tekst: {tekst}")
print(f"Antall tokens: {len(tokens)}")
print(f"Tokens: {token_strings}")

# Visualiser tokenisering
for i, (token, string) in enumerate(zip(tokens, token_strings)):
    print(f"Token {i}: '{string}' (ID: {token})")

# %% [markdown]
"""
## Temperature: Kontrollere kreativitet vs presisjon
"""

# %%
def simulate_generation(probs, temperature=1.0):
    """
    Simuler hvordan temperature påvirker tekstgenerering
    """
    # Juster sannsynligheter basert på temperature
    if temperature == 0:
        # Deterministisk: velg mest sannsynlige
        return np.argmax(probs)
    
    # Skaler log-probs med temperature
    log_probs = np.log(probs + 1e-10) / temperature
    # Konverter tilbake til sannsynligheter
    scaled_probs = np.exp(log_probs)
    scaled_probs = scaled_probs / np.sum(scaled_probs)
    
    # Sample fra distribusjonen
    return np.random.choice(len(probs), p=scaled_probs)

# Eksempel: Neste ord etter "Pasienten har"
mulige_ord = ["diabetes", "smerter", "feber", "hodepine", "kreft"]
sannsynligheter = [0.3, 0.25, 0.2, 0.15, 0.1]

print("Generering med ulike temperature-verdier:")
print("-" * 40)

for temp in [0.0, 0.5, 1.0, 2.0]:
    valgte_ord = []
    for _ in range(5):
        idx = simulate_generation(sannsynligheter, temp)
        valgte_ord.append(mulige_ord[idx])
    print(f"Temperature {temp}: {', '.join(valgte_ord)}")

# %% [markdown]
"""
## Kontekstvindu og begrensninger

LLMs har begrenset "hukommelse" (kontekstvindu):
- GPT-3.5: ~4,000 tokens
- GPT-4: 8,000-128,000 tokens
- Claude 3: 200,000 tokens

For medisinske journaler betyr dette at vi må:
1. Prioritere relevant informasjon
2. Dele opp lange dokumenter
3. Bruke sammendrag for historisk data
"""

# %%
# Demonstrer kontekstvindu-begrensning
def estimate_tokens(text):
    """Estimer antall tokens i tekst"""
    return len(encoding.encode(text))

# Typiske medisinske dokumenter
dokumenter = {
    "Kort konsultasjon": 200,
    "Standard journalnotat": 500,
    "Omfattende sykehistorie": 2000,
    "Full pasientjournal": 10000
}

print("Token-estimat for ulike dokumenttyper:")
print("-" * 40)
for dok_type, tokens in dokumenter.items():
    print(f"{dok_type}: ~{tokens} tokens")
    if tokens <= 4000:
        print(f"  ✅ Passer i GPT-3.5")
    elif tokens <= 8000:
        print(f"  ⚠️  Trenger GPT-4 eller deling")
    else:
        print(f"  ❌ Må deles opp eller sammendras")

# %% [markdown]
"""
## 💭 Refleksjonsoppgave

1. Hvorfor er tokenisering viktig for medisinske termer?
2. Når bør vi bruke lav vs høy temperature i kliniske applikasjoner?
3. Hvordan kan vi håndtere lange pasientjournaler med begrenset kontekstvindu?
"""
```

---

## 📓 03_prompt_engineering.ipynb

```python
# %% [markdown]
"""
# 🎯 Prompt Engineering for Helsefaglige Oppgaver

## Læringsmål
- Mestre grunnleggende prompt-teknikker
- Lære few-shot learning for medisinske caser
- Implementere chain-of-thought for komplekse vurderinger
"""

# %%
import os
from openai import OpenAI
from typing import List, Dict
import json

# Initialiser klient (bruker miljøvariabel OPENAI_API_KEY)
client = OpenAI()

print("🎯 Prompt Engineering - Kommuniser effektivt med AI")

# %% [markdown]
"""
## Grunnleggende prompt-prinsipper

1. **Vær spesifikk**: Klar kontekst og instruksjoner
2. **Gi eksempler**: Few-shot learning
3. **Strukturer output**: Be om spesifikt format
4. **Tenk stegvis**: Chain-of-thought
"""

# %%
def send_prompt(prompt: str, temperature: float = 0.7) -> str:
    """Hjelpefunksjon for å sende prompts til GPT"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Simulert respons (API ikke tilgjengelig): {e}"

# %% [markdown]
"""
## Teknikk 1: Zero-shot vs Few-shot
"""

# %%
# Zero-shot: Ingen eksempler
zero_shot_prompt = """
Klassifiser følgende symptombeskrivelse som enten 'Akutt' eller 'Ikke-akutt':

"Pasienten rapporterer brystsmerter som stråler til venstre arm, 
kortpustethet og kvalme de siste 30 minuttene."

Svar kun med klassifiseringen.
"""

# Few-shot: Med eksempler
few_shot_prompt = """
Klassifiser symptombeskrivelser som 'Akutt' eller 'Ikke-akutt'.

Eksempel 1: "Hodepine i 3 dager, forverres gradvis" → Ikke-akutt
Eksempel 2: "Plutselig kraftig hodepine, stiv nakke, feber" → Akutt
Eksempel 3: "Lett forkjølelse med rennende nese" → Ikke-akutt

Klassifiser: "Pasienten rapporterer brystsmerter som stråler til venstre arm, 
kortpustethet og kvalme de siste 30 minuttene."

Svar kun med klassifiseringen.
"""

print("Zero-shot resultat:", send_prompt(zero_shot_prompt, temperature=0))
print("Few-shot resultat:", send_prompt(few_shot_prompt, temperature=0))

# %% [markdown]
"""
## Teknikk 2: Chain-of-Thought (CoT)
"""

# %%
# Uten CoT
simple_prompt = """
En 65 år gammel mann med diabetes og hypertensjon kommer til legevakten 
med brystsmerter, svetting og kvalme. Bør han legges inn?
"""

# Med CoT
cot_prompt = """
En 65 år gammel mann med diabetes og hypertensjon kommer til legevakten 
med brystsmerter, svetting og kvalme. 

Vurder følgende steg-for-steg:
1. Identifiser risikofaktorer
2. Vurder symptomenes alvorlighetsgrad
3. Vurder sannsynlighet for hjerteinfarkt
4. Gi anbefaling om innleggelse

Vis din tankeprosess for hvert steg.
"""

print("Enkel prompt:", send_prompt(simple_prompt))
print("\n" + "="*50 + "\n")
print("Chain-of-Thought:", send_prompt(cot_prompt))

# %% [markdown]
"""
## Teknikk 3: Strukturert output
"""

# %%
structured_prompt = """
Analyser følgende pasientcase og gi svar i JSON-format:

Pasient: 45 år gammel kvinne
Symptomer: Tretthet, vekttap (5 kg siste 2 mnd), nattesvette
Historie: Røyker, ingen kjent sykdom

Svar i følgende JSON-struktur:
{
  "alvorlighetsgrad": "lav/moderat/høy",
  "mulige_diagnoser": ["diagnose1", "diagnose2", "diagnose3"],
  "anbefalte_undersøkelser": ["undersøkelse1", "undersøkelse2"],
  "hastegrad": "elektiv/urgent/akutt"
}
"""

response = send_prompt(structured_prompt, temperature=0)
print("Strukturert respons:")
print(response)

# Prøv å parse JSON (hvis faktisk API-respons)
try:
    parsed = json.loads(response)
    print("\nParset struktur:")
    for key, value in parsed.items():
        print(f"  {key}: {value}")
except:
    print("\n(Kunne ikke parse JSON - simulert respons)")

# %% [markdown]
"""
## 💡 Beste praksis for medisinske prompts

### DO's:
- ✅ Spesifiser rolle: "Du er en erfaren allmennlege..."
- ✅ Inkluder sikkerhetsinstruksjoner
- ✅ Be om begrunnelse for anbefalinger
- ✅ Spesifiser format for output

### DON'Ts:
- ❌ Stole blindt på AI for kritiske beslutninger
- ❌ Glemme å validere medisinsk informasjon
- ❌ Ignorere etiske retningslinjer
"""

# %%
# Eksempel på god medisinsk prompt
medical_prompt_template = """
Du er en medisinsk assistent som hjelper med dokumentasjon.
VIKTIG: Dine forslag er kun veiledende og må valideres av helsepersonell.

Oppgave: Lag et sammendrag av følgende konsultasjon for journalføring.

Konsultasjonsnotater:
- Pasient: {alder} år, {kjønn}
- Hovedproblem: {symptomer}
- Funn: {funn}
- Plan: {plan}

Format svaret som et strukturert journalnotat med seksjoner for:
1. Subjektivt (S)
2. Objektivt (O)
3. Vurdering (A)
4. Plan (P)

Bruk medisinsk terminologi der det er passende.
"""

# Fyll inn template
eksempel_data = {
    "alder": 58,
    "kjønn": "mann",
    "symptomer": "Brystsmerter ved anstrengelse siste 2 uker",
    "funn": "BT 145/90, puls 78 regulær, normale hjertelyder",
    "plan": "EKG, blodprøver inkl troponin, henvise kardiolog"
}

filled_prompt = medical_prompt_template.format(**eksempel_data)
print("Eksempel på journalnotat:")
print(send_prompt(filled_prompt, temperature=0.3))

# %% [markdown]
"""
## 🔬 Øvelse: Lag dine egne prompts

Prøv å lage prompts for:
1. Medisininteraksjon-sjekk
2. Pasientvennlig forklaring av diagnose
3. Triage-vurdering
4. Legemiddeldosering for barn

Tips: Start enkelt, test, og iterer!
"""
```

---

## 📓 04_chatgpt_claude_api.ipynb

```python
# %% [markdown]
"""
# 🔌 ChatGPT og Claude API - Praktisk Integrasjon

## Læringsmål
- Sette opp og bruke OpenAI og Anthropic APIs
- Implementere feilhåndtering og rate limiting
- Bygge en enkel medisinsk chatbot
"""

# %%
import os
from openai import OpenAI
from anthropic import Anthropic
import time
from typing import Optional
import json

print("🔌 API Integrasjon - Koble til ChatGPT og Claude")

# %% [markdown]
"""
## Oppsett av API-klienter
"""

# %%
class AIAssistant:
    """Wrapper-klasse for både OpenAI og Anthropic"""
    
    def __init__(self):
        # Initialiser klienter hvis API-nøkler finnes
        self.openai_client = None
        self.anthropic_client = None
        
        if os.getenv("OPENAI_API_KEY"):
            self.openai_client = OpenAI()
            print("✅ OpenAI klient initialisert")
        else:
            print("⚠️ OpenAI API-nøkkel ikke funnet")
            
        if os.getenv("ANTHROPIC_API_KEY"):
            self.anthropic_client = Anthropic()
            print("✅ Anthropic klient initialisert")
        else:
            print("⚠️ Anthropic API-nøkkel ikke funnet")
    
    def chat_gpt(self, prompt: str, model: str = "gpt-3.5-turbo", 
                 temperature: float = 0.7) -> Optional[str]:
        """Send prompt til ChatGPT"""
        if not self.openai_client:
            return "OpenAI ikke tilgjengelig - sjekk API-nøkkel"
        
        try:
            response = self.openai_client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Feil: {e}"
    
    def chat_claude(self, prompt: str, model: str = "claude-3-sonnet-20240229",
                   temperature: float = 0.7) -> Optional[str]:
        """Send prompt til Claude"""
        if not self.anthropic_client:
            return "Anthropic ikke tilgjengelig - sjekk API-nøkkel"
        
        try:
            response = self.anthropic_client.messages.create(
                model=model,
                max_tokens=1000,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Feil: {e}"

# Initialiser assistent
assistant = AIAssistant()

# %% [markdown]
"""
## Sammenlign modeller på samme oppgave
"""

# %%
# Medisinsk case for testing
medical_case = """
Forklar følgende blodprøveresultater for en pasient på en enkel måte:
- Hemoglobin: 10.2 g/dL (ref: 12-16)
- MCV: 72 fL (ref: 80-100)
- Ferritin: 8 ng/mL (ref: 15-200)

Hva kan dette indikere, og hva bør gjøres videre?
Svar på maks 100 ord, på norsk, tilpasset pasienten.
"""

print("🤖 ChatGPT svar:")
print("-" * 40)
gpt_response = assistant.chat_gpt(medical_case, temperature=0.3)
print(gpt_response)

print("\n🤖 Claude svar:")
print("-" * 40)
claude_response = assistant.chat_claude(medical_case, temperature=0.3)
print(claude_response)

# %% [markdown]
"""
## Bygge en medisinsk chatbot med kontekst
"""

# %%
class MedicalChatbot:
    """Enkel medisinsk chatbot med samtalehistorikk"""
    
    def __init__(self, model_type: str = "openai"):
        self.model_type = model_type
        self.assistant = AIAssistant()
        self.conversation_history = []
        self.system_prompt = """
        Du er en hjelpsom medisinsk assistent for helsepersonell.
        Du gir informasjon basert på beste praksis, men minner om at 
        dine svar må valideres og ikke erstatter klinisk vurdering.
        Svar på norsk, vær presis og bruk korrekt medisinsk terminologi.
        """
    
    def add_message(self, role: str, content: str):
        """Legg til melding i samtalehistorikk"""
        self.conversation_history.append({"role": role, "content": content})
    
    def chat(self, user_input: str) -> str:
        """Håndter brukerinput og generer respons"""
        self.add_message("user", user_input)
        
        # Bygg full prompt med historikk
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(self.conversation_history[-10:])  # Maks 10 siste meldinger
        
        if self.model_type == "openai" and self.assistant.openai_client:
            try:
                response = self.assistant.openai_client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    temperature=0.7
                )
                bot_response = response.choices[0].message.content
            except Exception as e:
                bot_response = f"Feil: {e}"
        else:
            # Fallback til enkel prompt hvis OpenAI ikke tilgjengelig
            bot_response = "Simulert svar: Jeg forstår spørsmålet ditt om " + user_input[:50]
        
        self.add_message("assistant", bot_response)
        return bot_response
    
    def reset(self):
        """Nullstill samtalehistorikk"""
        self.conversation_history = []

# Test chatbot
chatbot = MedicalChatbot()

print("💬 Medisinsk Chatbot Demo")
print("=" * 50)

# Simuler en samtale
questions = [
    "Hva er normale verdier for blodtrykk?",
    "Hvilke faktorer kan påvirke disse verdiene?",
    "Hvordan behandles høyt blodtrykk?"
]

for q in questions:
    print(f"\n👤 Bruker: {q}")
    response = chatbot.chat(q)
    print(f"🤖 Bot: {response}")
    time.sleep(1)  # Unngå rate limiting

# %% [markdown]
"""
## Rate limiting og feilhåndtering
"""

# %%
class RateLimitedAssistant:
    """API-klient med rate limiting og retry-logikk"""
    
    def __init__(self, requests_per_minute: int = 20):
        self.requests_per_minute = requests_per_minute
        self.min_time_between_requests = 60 / requests_per_minute
        self.last_request_time = 0
        self.client = OpenAI() if os.getenv("OPENAI_API_KEY") else None
    
    def wait_if_needed(self):
        """Vent hvis nødvendig for å respektere rate limits"""
        time_since_last = time.time() - self.last_request_time
        if time_since_last < self.min_time_between_requests:
            time.sleep(self.min_time_between_requests - time_since_last)
    
    def make_request(self, prompt: str, max_retries: int = 3) -> Optional[str]:
        """Gjør request med retry-logikk"""
        if not self.client:
            return "API ikke tilgjengelig"
        
        for attempt in range(max_retries):
            try:
                self.wait_if_needed()
                
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                
                self.last_request_time = time.time()
                return response.choices[0].message.content
                
            except Exception as e:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff
                    print(f"Feil: {e}. Venter {wait_time} sekunder...")
                    time.sleep(wait_time)
                else:
                    return f"Feil etter {max_retries} forsøk: {e}"
        
        return None

# Test rate limiting
rate_limited = RateLimitedAssistant(requests_per_minute=20)

print("🔄 Tester rate-limited requests...")
for i in range(3):
    prompt = f"Gi meg en kort definisjon av: {['Anemi', 'Hypertensjon', 'Diabetes'][i]}"
    print(f"\nRequest {i+1}: {prompt[:30]}...")
    response = rate_limited.make_request(prompt)
    print(f"Respons: {response[:100]}..." if response else "Ingen respons")

# %% [markdown]
"""
## 💾 Lagre og gjenbruke responser

For å spare API-kostnader og forbedre ytelse, 
kan vi cache responser:
"""

# %%
import hashlib
import json
from pathlib import Path

class CachedAssistant:
    """API-klient med caching av responser"""
    
    def __init__(self, cache_dir: str = "cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.assistant = AIAssistant()
    
    def get_cache_key(self, prompt: str, model: str) -> str:
        """Generer unik cache-nøkkel for prompt"""
        content = f"{model}:{prompt}"
        return hashlib.md5(content.encode()).hexdigest()
    
    def get_cached_response(self, prompt: str, model: str) -> Optional[str]:
        """Hent respons fra cache hvis den finnes"""
        cache_key = self.get_cache_key(prompt, model)
        cache_file = self.cache_dir / f"{cache_key}.json"
        
        if cache_file.exists():
            with open(cache_file, 'r') as f:
                data = json.load(f)
                print(f"📦 Hentet fra cache: {cache_key[:8]}...")
                return data['response']
        return None
    
    def save_to_cache(self, prompt: str, model: str, response: str):
        """Lagre respons i cache"""
        cache_key = self.get_cache_key(prompt, model)
        cache_file = self.cache_dir / f"{cache_key}.json"
        
        with open(cache_file, 'w') as f:
            json.dump({
                'prompt': prompt,
                'model': model,
                'response': response


# Continue ...











# Prompt-filer og Workshop Notebook

## 📄 prompts/kliniske_notater.txt

```text
# Kliniske Notater - Prompt Eksempler

## 1. SOAP-notat generering
Generer et SOAP-notat basert på følgende konsultasjon:

Pasient: 45 år gammel kvinne
Henvendelsesårsak: Hodepine og svimmelhet
Symptomer: Intermitterende hodepine siste 2 uker, svimmelhet ved rask reisning
Undersøkelse: BT 135/85, puls 72, ingen nevrologiske utfall
Tidligere sykdom: Migrene i familien
Medisiner: Paracetamol ved behov

Format:
S (Subjektivt):
O (Objektivt):
A (Assessment/Vurdering):
P (Plan):

## 2. Sammendrag av lang journal
Du er en medisinsk sekretær. Sammenfatt følgende journalnotater til et kort sammendrag på maks 150 ord:

[Lang journaltekst her - eksempel:]
15.03.2024: Pasienten kommer for kontroll av diabetes type 2. HbA1c 7.8%, opp fra 7.2% sist. 
Har sluttet med daglige turer pga knesmerter. Vekt opp 3 kg siste 3 mnd. Metformin 1000mg x2 fortsetter.
Henviser fysioterapi for kne. Ernæringsveiledning tilbudt.

22.03.2024: Telefon - spør om nye tabletter for diabetes. Informert om å vente til neste kontroll.
Fornøyd med fysioterapi.

29.03.2024: Akutt time - urinveisinfeksjon. Dysuri og frekvens. U-stix: Leukocytter+++, nitritt+.
Selexid 200mg x3 i 5 dager. Kontroll-urin om 1 uke.

## 3. Epikrise-mal
Lag en epikrise for følgende innleggelse:

Innleggelsesårsak: Akutte brystsmerter
Hoveddiagnose: NSTEMI
Bidiagnoser: Diabetes type 2, Hypertensjon
Behandling: PCI av LAD, medisinsk optimalisering
Videre plan: Kardiologisk poliklinikk om 3 mnd

Inkluder seksjoner for:
- Innleggelsesårsak
- Sykehistorie
- Funn og undersøkelser
- Behandling under innleggelse
- Medisinering ved utskrivelse
- Videre oppfølging

## 4. Kvalitetssikring av notater
Gjennomgå følgende journalnotat og:
1. Korriger eventuelle inkonsistenser
2. Sjekk medisindoseringer
3. Foreslå manglende informasjon

Notat:
"Pas 67 år m/ hjertesvikt kommer til ktr. NYHA klasse III. Bruker Enalapril 20mg x1, 
Metoprolol 50mg x2, Furosemid 40mg x1. BT 145/90, puls 88, vekt 85kg (opp 2kg fra sist). 
Ødemer begge ankler. Øker Furosemid til 80mg x2. Kontroll 2 uker."

## 5. Pasientvennlig oversettelse
Oversett følgende journaltekst til språk pasienten forstår:

"Pasienten presenterer med intermitterende claudicatio og parestesier i underekstremitetene 
bilateralt. ABI 0.7 høyre, 0.75 venstre indikerer moderat perifer karsykdom. 
Anbefaler konservativ behandling med platehemmer og statiner, samt supervised exercise therapy."

Forklar:
- Hva diagnosen betyr
- Hvorfor symptomene oppstår  
- Hva behandlingen går ut på
- Hva pasienten selv kan gjøre
```

---

## 📄 prompts/pasientsamtale.txt

```text
# Pasientsamtale - Prompt Eksempler

## 1. Strukturert anamneseopptak
Du er en erfaren lege som tar opp sykehistorie. Still relevante oppfølgingsspørsmål basert på:

Pasient sier: "Jeg har vondt i magen og føler meg kvalm"

Generer 5-7 relevante oppfølgingsspørsmål organisert etter:
- Symptomkarakteristikk (SOCRATES)
- Assosierte symptomer
- Forverrende/lindrende faktorer
- Tidligere episoder
- Røde flagg å se etter

## 2. Empati og kommunikasjon
Pasienten sier: "Jeg er så lei av å være syk hele tiden. Ingen medisin hjelper."

Gi tre alternative responser som viser:
a) Empati og validering
b) Åpne spørsmål for utforskning
c) Konkret plan fremover

## 3. Forklare diagnose
Forklar følgende diagnose til en pasient uten medisinsk bakgrunn:

Diagnose: Atrieflimmer
Pasientinfo: 68 år, kvinne, bekymret for hjertet

Inkluder:
- Hva som skjer i hjertet (bruk analogi)
- Hvorfor det oppstår
- Risiko hvis ubehandlet
- Behandlingsalternativer
- Hva pasienten kan forvente

Tone: Beroligende men ærlig

## 4. Motiverende samtale
Pasienten har diabetes type 2 og BMI 32. Har prøvd å gå ned i vekt mange ganger.

Lag en dialog som:
- Utforsker pasientens motivasjon (skala 1-10)
- Identifiserer barrierer
- Finner små, realistiske steg
- Styrker mestringstro

## 5. Vanskelige samtaler
Forbered en samtale om følgende tema:

Scenario: MR viser multiple metastaser, prognose 3-6 måneder

Strukturer samtalen:
1. Warning shot ("Jeg har fått svarene på undersøkelsene...")
2. Vurder pasientens ønske om informasjon
3. Lever beskjeden klart og tydelig
4. Stillhet og rom for reaksjon
5. Empati og støtte
6. Diskuter videre plan når pasienten er klar

## 6. Barn og ungdom
Tilpass følgende forklaring til en 10-åring:

"Du har astma, som betyr at luftrørene dine blir trange når de blir irriterte."

Bruk:
- Enkelt språk
- Analogi (f.eks. sugerør)
- Tegning/visualisering
- Forsikring om at det går bra
- Involver barnet i behandlingen

## 7. Tverrkulturell kommunikasjon
Pasienten snakker dårlig norsk. Familie er til stede som tolk.

Hvordan sikre god kommunikasjon om:
- Medisinbruk
- Oppfølging
- Alarmsymptomer
- Kulturelle hensyn

Tips for bruk av tolk og ikke-verbal kommunikasjon.
```

---

## 📄 prompts/journalsammendrag.txt

```text
# Journalsammendrag - Prompt Eksempler

## 1. Akuttjournal sammendrag
Sammenfatt følgende akuttjournal til 3-5 hovedpunkter:

02:45 - Innkommet med ambulanse, brystsmerter og dyspné
02:50 - Triage rød, EKG tatt, viser ST-elevasjon inferiort
03:00 - Morfin 5mg iv, Seloken 5mg iv, ASA 300mg po
03:15 - Til PCI-lab, stent i RCA
05:30 - Tilbake intensiv, stabil hemodynamisk
08:00 - Overført hjerteovervåkning

Sammendrag skal inneholde:
- Innleggelsesårsak
- Hovedfunn
- Behandling
- Status nå

## 2. Langtidssammendrag
Lag et sammendrag av pasientens siste 12 måneder:

Mars 2023: Diagnostisert KOLS GOLD stadium 2
Juni 2023: Innlagt exacerbasjon, antibiotika + prednisolon
September 2023: Startet LABA/LAMA kombinasjon
November 2023: Ny exacerbasjon, kort innleggelse
Januar 2024: Røykeslutt, henvist lungerehabilitering
Mars 2024: Kontroll - bedret lungefunksjon og livskvalitet

Fokuser på:
- Sykdomsutvikling
- Behandlingsrespons
- Positive endringer
- Videre plan

## 3. Tverrfaglig sammendrag
Kombiner notater fra ulike faggrupper:

LEGE: "Hjertesvikt med EF 35%, optimalisert medisinsk behandling"
SYKEPLEIER: "Tungpustet ved lett aktivitet, ødemer kommer tilbake kveldstid"
FYSIOTERAPEUT: "6-min gangtest: 220m, må pausere x2"
ERNÆRINGSFYSIOLOG: "Følger saltrestriksjon, vekt stabil"

Lag helhetlig bilde som inkluderer:
- Medisinsk status
- Funksjonsnivå
- Behandlingsplan
- Tverrfaglige tiltak

## 4. Overflyttingssammendrag
Pasient flyttes fra sykehus til kommunal rehabilitering.

Relevant info:
- Hoftebrudd operert for 5 dager siden
- Kan gå 20m med rullator
- Bor alene, 2. etasje uten heis
- Kognitiv svikt, MMSE 22/30
- Medisinliste: 8 preparater

Lag sammendrag for mottakende institusjon med:
- Funksjonsevne nå
- Hjelpebehov
- Rehabiliteringsmål
- Særlige hensyn
- Medisinering

## 5. Årskontroll-sammendrag
Diabetes type 2, årlig kontroll:

Data fra siste år:
- HbA1c: 7.2 → 6.8 → 7.0 → 6.9%
- Vekt: 92 → 89 → 88 → 89 kg
- BT: Gjennomsnitt 135/82
- Øyebunnsundersøkelse: Normal
- Fotundersøkelse: Normal sensibilitet
- U-albumin: Lett forhøyet

Lag strukturert sammendrag:
1. Måloppnåelse
2. Positive trender
3. Bekymringsområder
4. Justert behandlingsplan

## 6. Psykisk helse sammendrag
Sammenfatt 6 mnd behandling for depresjon:

- Start: PHQ-9 score 18 (moderat-alvorlig)
- Behandling: Sertralin + 8 samtaler KAT
- Nå: PHQ-9 score 7 (mild)
- Fungering: Tilbake 50% jobb, økt sosial aktivitet

Vektlegg:
- Symptomutviling
- Behandlingsrespons
- Funksjonsforbedring
- Risikofaktorer
- Videre plan

## 7. Kompleks multimorbidet
75 år gammel med:
- Hjertesvikt
- Diabetes type 2
- Nyresvikt stadium 3
- Mild kognitiv svikt
- 12 medisiner totalt

Lag prioritert sammendrag som:
- Identifiserer hovedproblem
- Vurderer interaksjoner mellom sykdommer
- Foreslår forenkling hvor mulig
- Fokuserer på livskvalitet vs. sykdomskontroll
```

---

## 📓 oppgaver/prompt_workshop.ipynb

```python
# %% [markdown]
"""
# 🎯 Prompt Workshop - Praktiske Øvelser

## Læringsmål
- Øve på å skrive effektive prompts for medisinske oppgaver
- Eksperimentere med ulike prompt-teknikker
- Evaluere og forbedre AI-responser
- Forstå begrensninger og muligheter

Dette er en interaktiv workshop hvor du skal teste og forbedre prompts!
"""

# %%
import os
from openai import OpenAI
import json
from typing import List, Dict

# Setup
client = OpenAI() if os.getenv("OPENAI_API_KEY") else None

def test_prompt(prompt: str, temperature: float = 0.7) -> str:
    """Test en prompt og returner respons"""
    if not client:
        return f"[Simulert respons for: {prompt[:50]}...]"
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Feil: {e}"

print("🎯 Prompt Workshop - La oss eksperimentere!")

# %% [markdown]
"""
## Øvelse 1: Forbedre en dårlig prompt

Her er en vag prompt. Din oppgave er å forbedre den!
"""

# %%
# Dårlig prompt
vag_prompt = "Fortell meg om diabetes"

# Test den vage prompten
print("❌ Vag prompt:")
print(test_prompt(vag_prompt))

# Din forbedrede versjon
forbedret_prompt = """
[SKRIV DIN FORBEDREDE PROMPT HER]

Tips:
- Spesifiser målgruppe
- Definer format
- Begrens omfang
- Be om struktur
"""

# Test forbedringen
print("\n✅ Forbedret prompt:")
# print(test_prompt(forbedret_prompt))

# %% [markdown]
"""
### Løsningsforslag
"""

# %%
# Eksempel på god prompt
god_prompt = """
Du er en sykepleier som forklarer til en nydiagnostisert pasient.

Forklar diabetes type 2 på en enkel måte som dekker:
1. Hva som skjer i kroppen (2-3 setninger)
2. Vanlige symptomer (punktliste)
3. Hvorfor behandling er viktig (2 setninger)
4. Tre livsstilsråd de kan starte med i dag

Bruk vennlig tone, unngå skremming, maks 150 ord totalt.
"""

print("✨ Eksempel på forbedret prompt:")
print(test_prompt(god_prompt, temperature=0.3))

# %% [markdown]
"""
## Øvelse 2: Few-shot learning for triage

Lag et few-shot prompt-system for å klassifisere hastegrad.
"""

# %%
def create_triage_prompt(symptom_beskrivelse: str) -> str:
    """
    Lag en few-shot prompt for triage-klassifisering
    
    Fyll inn eksempler nedenfor!
    """
    prompt = f"""
    Klassifiser hastegrad som RØD (øyeblikkelig), GUL (haster), eller GRØNN (kan vente).
    
    Eksempler:
    Symptomer: Brystsmerter med utstråling til arm, svetting, kvalm
    Klassifisering: RØD
    
    Symptomer: Sår hals i 3 dager, lett feber, ingen pustevansker
    Klassifisering: GRØNN
    
    [LEGG TIL MINST 2 EKSEMPLER TIL HER]
    
    Symptomer: {symptom_beskrivelse}
    Klassifisering:"""
    
    return prompt

# Test med ulike symptomer
test_symptomer = [
    "Hodepine som har vart i 2 uker, forverres om morgenen",
    "Plutselig synstap på ett øye for 20 minutter siden",
    "Kløe og utslett etter å ha spist skalldyr"
]

for symptom in test_symptomer:
    prompt = create_triage_prompt(symptom)
    print(f"\n📋 Symptom: {symptom}")
    print(f"🚦 Klassifisering: {test_prompt(prompt, temperature=0)}")

# %% [markdown]
"""
## Øvelse 3: Chain-of-Thought for differensialdiagnose

Implementer CoT for å resonere seg frem til mulige diagnoser.
"""

# %%
def differential_diagnosis_cot(case: str) -> str:
    """
    Lag en Chain-of-Thought prompt for differensialdiagnose
    """
    prompt = f"""
    Analyser følgende case steg-for-steg:
    
    {case}
    
    Følg denne tankeprosessen:
    
    1. IDENTIFISER hovedsymptomer:
       [List opp de viktigste symptomene]
    
    2. VURDER tidsforløp:
       [Akutt vs kronisk, progresjon]
    
    3. RELEVANTE risikofaktorer:
       [Alder, kjønn, historie, livsstil]
    
    4. MULIGE systemer involvert:
       [Hvilke organsystemer kan være påvirket]
    
    5. DIFFERENSIALDIAGNOSER (mest til minst sannsynlig):
       [List 3-5 mulige diagnoser med kort begrunnelse]
    
    6. RØDE FLAGG å se etter:
       [Hva ville krevd øyeblikkelig handling]
    
    Vis din resonnering for hvert steg.
    """
    
    return prompt

# Test case
case = """
45 år gammel kvinne, tidligere frisk.
Siste 3 måneder: Tretthet, 5 kg vekttap, nattesvette.
Siste uke: Hovne lymfeknuter på halsen, ingen smerter.
Ikke-røyker, moderat alkohol, ingen reiser.
"""

cot_prompt = differential_diagnosis_cot(case)
print("🔍 Differensialdiagnose med Chain-of-Thought:")
print(test_prompt(cot_prompt, temperature=0.2))

# %% [markdown]
"""
## Øvelse 4: Prompt med sikkerhetsinstruksjoner

Lag prompts som inkluderer viktige sikkerhetshensyn.
"""

# %%
def safe_medical_prompt(question: str) -> str:
    """
    Wrapper som legger til sikkerhetsinstruksjoner
    """
    safety_instructions = """
    VIKTIGE RETNINGSLINJER:
    1. Dine svar er kun veiledende og erstatter IKKE medisinsk konsultasjon
    2. Ved akutte symptomer: Alltid anbefale å kontakte lege/113
    3. Aldri gi spesifikke medisindoseringer uten legetilsyn
    4. Vær tydelig på usikkerhet og begrensninger
    5. Henvis til helsepersonell ved behov
    """
    
    prompt = f"""
    {safety_instructions}
    
    Spørsmål fra bruker: {question}
    
    Svar på en ansvarlig måte som følger retningslinjene ovenfor.
    """
    
    return prompt

# Test med potensielt problematiske spørsmål
risky_questions = [
    "Hvor mye paracetamol kan jeg ta for sterke smerter?",
    "Jeg har brystsmerter, skal jeg vente til i morgen?",
    "Kan jeg slutte med antidepressiva selv?"
]

for q in risky_questions:
    print(f"\n❓ Spørsmål: {q}")
    safe_prompt = safe_medical_prompt(q)
    print(f"✅ Trygt svar: {test_prompt(safe_prompt, temperature=0.2)}")

# %% [markdown]
"""
## Øvelse 5: Evaluere og sammenligne prompts

Lag et system for å evaluere prompt-kvalitet.
"""

# %%
def evaluate_prompts(prompts: List[str], criteria: List[str]) -> Dict:
    """
    Evaluer flere prompts mot gitte kriterier
    """
    evaluation = {}
    
    for i, prompt in enumerate(prompts, 1):
        print(f"\n📝 Evaluerer prompt {i}...")
        
        eval_prompt = f"""
        Evaluer følgende prompt på en skala 1-5 for hvert kriterium:
        
        PROMPT:
        {prompt}
        
        KRITERIER:
        {chr(10).join(f"- {c}" for c in criteria)}
        
        Gi score og kort begrunnelse for hver.
        Format: Kriterium: Score/5 - Begrunnelse
        """
        
        evaluation[f"prompt_{i}"] = test_prompt(eval_prompt, temperature=0)
    
    return evaluation

# Definer evalueringskriterier
kriterier = [
    "Klarhet og spesifisitet",
    "Medisinsk korrekthet",
    "Pasientvennlighet",
    "Sikkerhetshensyn",
    "Praktisk anvendbarhet"
]

# Test med to ulike prompts for samme oppgave
prompt_v1 = "Forklar hva antibiotika er"

prompt_v2 = """
Du er en allmennlege som forklarer til en pasient med ørebetennelse.

Forklar:
1. Hva antibiotika er (2-3 setninger, enkelt språk)
2. Hvorfor det er foreskrevet for deres tilstand
3. Viktigheten av å fullføre kuren
4. Vanlige bivirkninger å se etter

Tone: Vennlig og beroligende
Lengde: Maks 100 ord
"""

# Evaluer
resultater = evaluate_prompts([prompt_v1, prompt_v2], kriterier)
for key, value in resultater.items():
    print(f"\n{key}:")
    print(value)

# %% [markdown]
"""
## 🏆 Sluttøvelse: Lag din egen avanserte prompt

Oppgave: Design en prompt for en kompleks medisinsk oppgave du velger selv.

Krav:
1. Bruk minst 3 prompt-teknikker
2. Inkluder sikkerhetsinstruksjoner
3. Definer tydelig output-format
4. Test med edge cases
"""

# %%
# Din avanserte prompt her
min_avanserte_prompt = """
[SKRIV DIN PROMPT HER]

Ideer:
- Medisininteraksjon-sjekker
- Symptom-dagbok analyse
- Rehabiliteringsplan generator
- Ernæringsråd for spesifikke tilstander
- Mental helse screening
"""

# Test den
# resultat = test_prompt(min_avanserte_prompt)
# print(resultat)

# %% [markdown]
"""
## 📊 Oppsummering og refleksjon

### Hva har vi lært?
1. **Spesifisitet** gir bedre resultater
2. **Eksempler** (few-shot) forbedrer ytelse
3. **Struktur** i prompts gir struktur i svar
4. **Sikkerhet** må alltid inkluderes i medisinske prompts
5. **Iterasjon** er nøkkelen - test og forbedre!

### Videre eksperimentering
- Prøv samme prompt med ulik temperature
- Test på edge cases og uventede inputs
- Kombiner flere teknikker
- Sammenlign GPT-3.5, GPT-4 og Claude

### Etisk refleksjon
- Hvordan sikre at AI ikke overskrider sin kompetanse?
- Når bør AI IKKE brukes i helsevesenet?
- Hvordan bevare menneskelig tilsyn og ansvar?

**Husk:** AI er et verktøy som forsterker, ikke erstatter, klinisk kompetanse!
"""
```

-->