# Uke 1: Introduksjon til Kunstig Intelligens

## 🎯 Ukens Læringsmål

Etter denne uken skal du:
- **Forstå** hva kunstig intelligens er og dens historiske utvikling
- **Skille** mellom AI, maskinlæring og dyp læring
- **Kjenne til** regelbaserte systemer og tidlige ekspertsystemer i medisin
- **Ha satt opp** ditt utviklingsmiljø i GitHub Codespaces
- **Ha kjørt** dine første AI-eksempler

## 📚 Innhold

### Notebooks
1. **[00-velkommen.ipynb](00-velkommen.ipynb)** - Kursoversikt og praktisk info
2. **[01-test-meg.ipynb](01-test-meg.ipynb)** - Test at miljøet fungerer
3. **[02-hva-er-ai.ipynb](02-hva-er-ai.ipynb)** - Grunnleggende konsepter
4. **[03-ai-historie-helse.ipynb](03-ai-historie-helse.ipynb)** - AI i helsevesenet gjennom tidene
5. **[04-ai-ml-dl-forskjeller.ipynb](04-ai-ml-dl-forskjeller.ipynb)** - Forstå begrepsjungelen
6. **[05-regelbaserte-systemer.ipynb](05-regelbaserte-systemer.ipynb)** - Bygge et enkelt ekspertsystem
7. **[06-oppsett-miljø.ipynb](06-oppsett-miljø.ipynb)** - GitHub Codespaces guide

### Oppgaver
- **Refleksjonsnotat**: AI's rolle i fremtidens helsevesen (500 ord)
- **Praktisk øvelse**: Bygg et regelbasert triagesystem
- **Quiz**: Test din forståelse av grunnbegreper

## 🚀 Hurtigstart

```python
# Sjekk at alt fungerer
import sys
print(f"Python versjon: {sys.version}")
print("🎉 Velkommen til AI og Helse!")
```



## 📖 Lesestoff

### Obligatorisk
- Kapittel 1 i "Artificial Intelligence in Medicine" (lenke i Canvas)
- [AI in Medicine: A Brief History](https://www.nature.com/articles/s41591-023-02344-1)

### Anbefalt
- [Turing Test and Medical AI](https://www.bmj.com/content/380/bmj-2022-073816)
- [From MYCIN to ChatGPT](https://academic.oup.com/jamia/article/31/3/791/7457419)

## 💭 Refleksjonsspørsmål

1. Hva er forskjellen på "smal" og "generell" AI?
2. Hvorfor feilet mange tidlige medisinske ekspertsystemer?
3. Hvilke etiske utfordringer ser du med AI i helsevesenet?
4. Hvordan kan AI støtte, ikke erstatte, helsepersonell?

## 👩‍🏫 Ukens Veiledning

- **Tirsdag kl 14-16**: Introduksjonsforelesning (Teams)
- **Torsdag kl 10-11**: Teknisk support for oppsett (frivillig)
- **Forum**: Aktiv hele uken for spørsmål

## ✅ Sjekkliste

- [ ] Les gjennom alle notebooks
- [ ] Sett opp GitHub Codespaces
- [ ] Kjør test-notebook
- [ ] Delta i minst én diskusjon i forum
- [ ] Lever refleksjonsnotat innen søndag kl 23:59

<!-- 
---

## 📓 00-velkommen.ipynb

```python
# %% [markdown]
"""
# 🎉 Velkommen til AI og Helse!

## Om dette kurset

Dette er et 5 studiepoengs kurs som gir deg praktisk kompetanse i kunstig intelligens 
for helse- og omsorgssektoren. Kurset går over 10 uker og kombinerer teori med 
hands-on erfaring.

### Hvem er jeg?
Jeg er din kursleder, og har jobbet med AI i helsevesenet i over 10 år.
Min bakgrunn inkluderer både klinisk erfaring og teknisk kompetanse.

### Hvem er dere?
La oss bli kjent! Kjør cellen nedenfor og fyll inn din info.
"""

# %%
# Interaktiv introduksjon
from datetime import datetime
import json

def introduser_deg():
    """La oss bli kjent!"""
    print("🤝 Velkommen! La oss bli kjent.")
    print("-" * 40)
    
    # Samle informasjon
    info = {}
    info['navn'] = input("Hva heter du? ")
    info['yrke'] = input("Hva jobber du med? ")
    info['erfaring_ai'] = input("Har du erfaring med AI? (ja/nei/litt) ")
    info['motivasjon'] = input("Hvorfor tar du dette kurset? ")
    info['dato'] = datetime.now().strftime("%Y-%m-%d")
    
    # Lagre til fil (valgfritt)
    with open('min_introduksjon.json', 'w') as f:
        json.dump(info, f, indent=2, ensure_ascii=False)
    
    print("\n✅ Flott! Du er nå registrert i kurset.")
    print(f"👋 Velkommen, {info['navn']}!")
    
    # Gi tilpasset velkomst
    if 'nei' in info['erfaring_ai'].lower():
        print("💡 Ingen bekymring - vi starter helt fra bunnen!")
    elif 'litt' in info['erfaring_ai'].lower():
        print("💡 Perfekt! Du har et godt utgangspunkt.")
    else:
        print("💡 Supert! Din erfaring vil berike diskusjonene.")
    
    return info

# Kjør introduksjonen
# min_info = introduser_deg()

# %% [markdown]
"""
## Kursstruktur

### 📅 10 ukers reise

| Uke | Tema | Fokus |
|-----|------|-------|
| 1-3 | **Grunnleggende AI** | Fra regelbaser til nevrale nettverk |
| 4-6 | **Moderne AI** | Generativ AI, LLM, multimodal AI |
| 7-8 | **Anvendelser** | Velferdsteknologi, robotikk, etikk |
| 9 | **Fysisk samling** | Hands-on workshop |
| 10 | **Eksamen** | Hjemmeeksamen og prosjekt |

### 📊 Vurdering
- 60% Hjemmeeksamen
- 40% Prosjektoppgave
- 3 obligatoriske refleksjonsnotater (godkjent/ikke godkjent)
"""

# %%
# Visualiser kursstrukturen
import matplotlib.pyplot as plt
import numpy as np

# Data for visualisering
uker = list(range(1, 11))
teori_prosent = [80, 70, 60, 50, 40, 40, 30, 30, 20, 10]
praksis_prosent = [20, 30, 40, 50, 60, 60, 70, 70, 80, 90]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Teori vs Praksis
ax1.fill_between(uker, teori_prosent, alpha=0.3, label='Teori', color='blue')
ax1.fill_between(uker, praksis_prosent, alpha=0.3, label='Praksis', color='green')
ax1.set_xlabel('Uke')
ax1.set_ylabel('Prosent av innhold')
ax1.set_title('Kursbalanse: Teori vs Praksis')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Temaer per uke
temaer = ['Intro', 'ML', 'DL', 'LLM', 'Multi-\nmodal', 'Klinisk', 
          'Velferds-\ntek', 'Etikk', 'Workshop', 'Eksamen']
farger = plt.cm.viridis(np.linspace(0, 1, 10))

ax2.bar(uker, [100]*10, color=farger)
ax2.set_xlabel('Uke')
ax2.set_ylabel('Fokus')
ax2.set_title('Ukentlige Temaer')
ax2.set_xticks(uker)
ax2.set_xticklabels(temaer, rotation=45, ha='right')

plt.tight_layout()
plt.show()

# %% [markdown]
"""
## 💻 Teknisk oppsett

### Hva trenger du?
1. **GitHub-konto** (gratis)
2. **Nettleser** (Chrome, Firefox, Safari, Edge)
3. **Internett** (stabilt)

### Hva trenger du IKKE?
- ❌ Installere Python lokalt
- ❌ Kraftig datamaskin
- ❌ Programmeringserfaring

Alt kjører i skyen via GitHub Codespaces! 🌥️
"""

# %%
# Sjekk system-info
import platform
import sys

def sjekk_miljø():
    """Sjekk at alt er klart"""
    print("🔍 Systemsjekk")
    print("=" * 40)
    print(f"Python versjon: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Prosessor: {platform.processor() or 'Ukjent'}")
    
    # Sjekk viktige pakker
    pakker = ['numpy', 'pandas', 'matplotlib', 'sklearn', 'torch', 'openai']
    
    print("\n📦 Pakker:")
    for pakke in pakker:
        try:
            modul = __import__(pakke)
            versjon = getattr(modul, '__version__', 'ukjent')
            print(f"✅ {pakke}: {versjon}")
        except ImportError:
            print(f"❌ {pakke}: Ikke installert")
    
    print("\n🎯 Status: Klar for kursstart!" if all(
        [__import__(p, globals(), locals(), [], 0) for p in pakker[:4]]
    ) else "\n⚠️ Noen pakker mangler - kjør setup-script")

sjekk_miljø()

# %% [markdown]
"""
## 📚 Læringsfilosofi

### Vi lærer best gjennom:
1. **Praktiske eksempler** - Reelle helsecaser
2. **Eksperimentering** - Prøv og feil er OK!
3. **Diskusjon** - Del erfaringer i forum
4. **Refleksjon** - Tenk kritisk om anvendelser

### Huskeliste for suksess:
- 🕐 Sett av 10-12 timer per uke
- 💬 Still spørsmål - ingen spørsmål er dumme
- 🤝 Samarbeid med medstudenter
- 📝 Ta notater underveis
- 🔄 Gjenta og øv på kode-eksempler

## La oss starte! 🚀
"""
```

---

## 📓 02-hva-er-ai.ipynb

```python
# %% [markdown]
"""
# 🤖 Hva er Kunstig Intelligens?

## Læringsmål
- Definere kunstig intelligens
- Forstå forskjellen på "smal" og "generell" AI
- Kjenne til Turing-testen og dens relevans
- Se praktiske eksempler på AI i hverdagen og helsevesenet
"""

# %%
print("🧠 La oss utforske hva AI egentlig er!")

# %% [markdown]
"""
## Definisjon av AI

**Kunstig intelligens (AI)** er systemer som kan:
- 🎯 Løse oppgaver som normalt krever menneskelig intelligens
- 📚 Lære fra erfaring
- 🔄 Tilpasse seg nye situasjoner
- 💭 Resonere og ta beslutninger

### Men hva betyr "intelligens"?
"""

# %%
# Interaktiv demonstrasjon: Er dette intelligent?
def er_dette_ai(beskrivelse, svar=None):
    """Vurder om noe er AI eller ikke"""
    print(f"❓ {beskrivelse}")
    bruker_svar = input("Er dette AI? (ja/nei): ").lower()
    
    if svar:
        if bruker_svar == svar:
            print("✅ Riktig!")
        else:
            print(f"🤔 Faktisk {svar}!")
    
    return bruker_svar

# Test din forståelse
eksempler = [
    ("En kalkulator som regner 2+2", "nei"),
    ("Google Maps som finner korteste vei", "ja"),
    ("Automatisk oversettelse av tekst", "ja"),
    ("En termostat som holder konstant temperatur", "nei"),
    ("Ansiktsgjenkjenning på telefonen", "ja"),
    ("En database som lagrer pasientdata", "nei")
]

print("🎮 Quiz: Er dette AI?")
print("-" * 40)
# for beskrivelse, fasit in eksempler:
#     er_dette_ai(beskrivelse, fasit)
#     print()

# %% [markdown]
"""
## Smal vs Generell AI

### 🎯 Smal AI (Narrow AI / ANI)
- Designet for spesifikke oppgaver
- All dagens AI er smal AI
- Eksempler: Sjakk-AI, bildegjenkjenning, språkoversettelse

### 🌍 Generell AI (AGI)
- Kan løse hvilken som helst intellektuell oppgave
- Menneskelignende intelligens
- Eksisterer ikke enda (og kanskje aldri?)

### 🚀 Superintelligens (ASI)
- Overgår menneskelig intelligens på alle områder
- Science fiction (foreløpig!)
"""

# %%
# Visualiser AI-spekteret
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12, 6))

# AI-typer på en tidslinje
ai_types = ['Regelbaserte\nsystemer', 'Maskinlæring', 'Dyp læring', 
            'Generativ AI', 'AGI?', 'ASI?']
years = [1960, 1980, 2010, 2020, 2040, 2060]
capabilities = [10, 20, 50, 70, 90, 100]

# Plot
ax.plot(years, capabilities, 'b-', linewidth=2)
ax.scatter(years[:4], capabilities[:4], s=100, c='green', label='Eksisterer')
ax.scatter(years[4:], capabilities[4:], s=100, c='red', alpha=0.5, label='Hypotetisk')

# Annotering
for i, (year, cap, ai_type) in enumerate(zip(years, capabilities, ai_types)):
    ax.annotate(ai_type, (year, cap), textcoords="offset points", 
                xytext=(0,10), ha='center', fontsize=10)

ax.set_xlabel('År', fontsize=12)
ax.set_ylabel('Relativ kapabilitet (%)', fontsize=12)
ax.set_title('AI-utvikling: Fra regelbasert til AGI?', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.legend()

# Marker "vi er her"
current_year = 2024
ax.axvline(x=current_year, color='orange', linestyle='--', alpha=0.7)
ax.text(current_year, 85, 'Vi er her!', rotation=90, va='bottom', color='orange')

plt.tight_layout()
plt.show()

# %% [markdown]
"""
## Turing-testen: Kan maskiner tenke?

Alan Turing (1950) foreslo en test:
- En person chatter med både menneske og maskin
- Hvis personen ikke kan skille dem → Maskinen er "intelligent"

### Relevans for helsevesenet?
"""

# %%
# Simuler en enkel Turing-test
import random

def medisinsk_turing_test():
    """Enkel demonstrasjon av Turing-test konseptet"""
    
    # Forhåndsdefinerte responser
    ai_responser = {
        "hodepine": "Basert på symptomene kan det være spenningshodepine. "
                   "Vanlige triggere inkluderer stress, dehydrering og dårlig søvn. "
                   "Ved vedvarende eller forverrede symptomer, kontakt lege.",
        "feber": "Feber er kroppens naturlige respons på infeksjon. "
                "Drikk mye væske, hvil og bruk febernedsettende ved behov. "
                "Søk lege hvis feber > 40°C eller varer > 3 dager.",
        "default": "Jeg forstår bekymringen. Basert på beskrivelsen anbefaler jeg "
                  "å observere symptomene og kontakte fastlege hvis de forverres."
    }
    
    menneske_responser = {
        "hodepine": "Åh, hodepine kan være så plagsomt! Jeg husker når jeg hadde migrene... "
                   "Har du prøvd å ligge i et mørkt rom? Det hjelper ofte meg. "
                   "Men hvis det ikke går over, bør du nok snakke med legen din.",
        "feber": "Uff, feber er aldri gøy. Sist jeg var syk drakk jeg masse te med honning. "
                "Bestemor pleide alltid å si at man må svette det ut! "
                "Men høres det høyt ut, så kanskje du skal ringe legevakten?",
        "default": "Hmm, det høres ikke bra ut. Jeg er ikke lege, men "
                  "synes du bør få det sjekket hvis du er bekymret. "
                  "Bedre å være på den sikre siden!"
    }
    
    print("🤖 TURING-TEST: Hvem svarer - AI eller menneske?")
    print("=" * 50)
    
    symptom = input("Beskriv et symptom (f.eks. 'hodepine' eller 'feber'): ").lower()
    
    # Velg tilfeldig om AI eller menneske svarer
    er_ai = random.choice([True, False])
    
    if er_ai:
        respons = ai_responser.get(symptom, ai_responser["default"])
    else:
        respons = menneske_responser.get(symptom, menneske_responser["default"])
    
    print(f"\n💬 Respons:\n{respons}")
    
    gjett = input("\n🤔 Tror du dette er AI eller menneske? ").lower()
    
    if (gjett == "ai" and er_ai) or (gjett == "menneske" and not er_ai):
        print("✅ Riktig!")
    else:
        print(f"❌ Feil! Det var {'AI' if er_ai else 'menneske'}.")
    
    print("\n💡 Legg merke til:")
    print("- AI: Mer strukturert, faktabasert, profesjonell")
    print("- Menneske: Personlige anekdoter, følelser, mindre formell")

# Kjør testen
# medisinsk_turing_test()

# %% [markdown]
"""
## AI i hverdagen og helsevesenet

### 📱 AI du bruker hver dag (ofte uten å tenke på det):
- Autocorrect og prediktiv tekst
- Spotify/Netflix anbefalinger
- Ansiktsgjenkjenning
- Spam-filter
- Google søk

### 🏥 AI i helsevesenet i dag:
"""

# %%
# Kategoriser og visualiser AI-anvendelser i helse
import pandas as pd
import matplotlib.pyplot as plt

# Data om AI-anvendelser
ai_anvendelser = pd.DataFrame({
    'Område': ['Diagnostikk', 'Behandling', 'Administrasjon', 
               'Forskning', 'Monitorering', 'Forebygging'],
    'Modenhet': [8, 6, 7, 9, 7, 5],  # Skala 1-10
    'Eksempler': [
        'Bildeanalyse (røntgen, MR)',
        'Robotkirurgi, medisinoptimering',
        'Journalføring, timeplanlegging',
        'Legemiddelutvikling, genomikk',
        'Wearables, fjernmonitorering',
        'Risikoprediksjon, helseapper'
    ]
})

# Lag subplot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Søylediagram for modenhet
colors = plt.cm.viridis(ai_anvendelser['Modenhet'] / 10)
bars = ax1.bar(ai_anvendelser['Område'], ai_anvendelser['Modenhet'], color=colors)
ax1.set_ylabel('Teknologisk modenhet (1-10)')
ax1.set_title('AI-modenhet i ulike helseområder')
ax1.set_ylim(0, 10)
ax1.grid(True, alpha=0.3, axis='y')

# Legg til verdier på søylene
for bar, verdi in zip(bars, ai_anvendelser['Modenhet']):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
             str(verdi), ha='center', va='bottom')

# Kakediagram for fordeling
sizes = [20, 15, 25, 20, 10, 10]
explode = (0.1, 0, 0, 0, 0, 0)  # Fremhev diagnostikk
ax2.pie(sizes, explode=explode, labels=ai_anvendelser['Område'], 
        autopct='%1.1f%%', startangle=90, colors=colors)
ax2.set_title('Fordeling av AI-investeringer i helse')

plt.tight_layout()
plt.show()

# Vis eksempler
print("🏥 Konkrete AI-eksempler i norsk helsevesen:")
for _, row in ai_anvendelser.iterrows():
    print(f"\n{row['Område']}:")
    print(f"  → {row['Eksempler']}")

# %% [markdown]
"""
## 🧪 Hands-on: Din første AI

La oss lage en enkel regelbasert "AI" for symptomvurdering!
"""

# %%
class EnkelSymptomAI:
    """En veldig enkel regelbasert AI for symptomvurdering"""
    
    def __init__(self):
        # Definer enkle regler
        self.symptom_regler = {
            'feber': {
                'høy': 'Kontakt lege umiddelbart',
                'moderat': 'Hvil og drikk væske, kontakt lege hvis varer > 3 dager',
                'lav': 'Observer, bruk febernedsettende ved behov'
            },
            'hodepine': {
                'plutselig_kraftig': 'Ring 113 - kan være alvorlig',
                'kronisk': 'Planlegg legetime',
                'mild': 'Hvil, drikk vann, vurder smertestillende'
            },
            'brystsmerter': {
                'med_pustebesvær': 'Ring 113 umiddelbart',
                'ved_anstrengelse': 'Kontakt lege samme dag',
                'muskulær': 'Observer, vurder smertestillende'
            }
        }
    
    def vurder(self, symptom, alvorlighet):
        """Gi enkel vurdering basert på symptom og alvorlighet"""
        symptom = symptom.lower()
        
        if symptom in self.symptom_regler:
            if alvorlighet in self.symptom_regler[symptom]:
                return self.symptom_regler[symptom][alvorlighet]
            else:
                return "Kontakt fastlege for vurdering"
        else:
            return "Symptom ikke gjenkjent - kontakt helsepersonell"
    
    def interaktiv_konsultasjon(self):
        """Kjør en interaktiv konsultasjon"""
        print("🤖 Enkel Symptom-AI")
        print("=" * 40)
        print("Tilgjengelige symptomer: feber, hodepine, brystsmerter")
        
        symptom = input("\nHva plager deg? ").lower()
        
        if symptom == 'feber':
            print("Temperatur: 1) Under 38.5  2) 38.5-39.5  3) Over 39.5")
            valg = input("Velg (1/2/3): ")
            alvorlighet = ['lav', 'moderat', 'høy'][int(valg)-1]
        elif symptom == 'hodepine':
            print("Type: 1) Mild  2) Kronisk  3) Plutselig og kraftig")
            valg = input("Velg (1/2/3): ")
            alvorlighet = ['mild', 'kronisk', 'plutselig_kraftig'][int(valg)-1]
        elif symptom == 'brystsmerter':
            print("Karakter: 1) Muskulær  2) Ved anstrengelse  3) Med pustebesvær")
            valg = input("Velg (1/2/3): ")
            alvorlighet = ['muskulær', 'ved_anstrengelse', 'med_pustebesvær'][int(valg)-1]
        else:
            alvorlighet = 'ukjent'
        
        anbefaling = self.vurder(symptom, alvorlighet)
        
        print("\n" + "="*40)
        print(f"📋 Vurdering: {anbefaling}")
        print("="*40)
        print("\n⚠️ VIKTIG: Dette er kun en demonstrasjon!")
        print("Ved reelle symptomer - kontakt alltid helsepersonell!")

# Opprett og test AI-en
min_ai = EnkelSymptomAI()

# Test med eksempler
print("📝 Test av regelbasert AI:")
print(f"Feber (høy): {min_ai.vurder('feber', 'høy')}")
print(f"Hodepine (mild): {min_ai.vurder('hodepine', 'mild')}")
print(f"Brystsmerter (med_pustebesvær): {min_ai.vurder('brystsmerter', 'med_pustebesvær')}")

# Kjør interaktiv konsultasjon
# print("\n" + "="*50)
# min_ai.interaktiv_konsultasjon()

# %% [markdown]
"""
## 💭 Refleksjon

### Styrker med dagens AI:
- ✅ Behandler store datamengder raskt
- ✅ Finner mønstre mennesker overser
- ✅ Konsistent ytelse 24/7
- ✅ Kan spesialiseres for spesifikke oppgaver

### Begrensninger:
- ❌ Mangler ekte forståelse
- ❌ Kan ikke generalisere som mennesker
- ❌ Sårbar for bias i treningsdata
- ❌ Mangler empati og mellommenneskelig forståelse

### 🤔 Diskusjonsspørsmål:
1. Kan AI noen gang erstatte en leges kliniske skjønn?
2. Hvordan sikre at AI-systemer er rettferdige?
3. Hvem har ansvaret når AI gjør feil?
"""
```

---

## 📓 03-ai-historie-helse.ipynb

```python
# %% [markdown]
"""
# 📚 AI i Helsevesenet: En Historisk Reise

## Læringsmål
- Forstå AI's utvikling i medisinsk kontekst
- Kjenne til milepæler og viktige systemer
- Lære av historiske suksesser og fiaskoer
- Se trender og fremtidsperspektiver
"""

# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

print("🕰️ La oss reise gjennom AI's historie i helsevesenet!")

# %% [markdown]
"""
## Tidslinje: Fra 1950 til i dag
"""

# %%
# Opprett historisk tidslinje
historiske_hendelser = pd.DataFrame({
    'År': [1950, 1966, 1972, 1976, 1986, 1995, 2012, 2016, 2018, 2020, 2023],
    'Hendelse': [
        'Turing Test',
        'ELIZA (terapi-chatbot)',
        'MYCIN utvikles',
        'INTERNIST-I',
        'DXplain lanseres',
        'Første robot-assisterte kirurgi',
        'Deep Learning revolusjon',
        'AlphaGo slår Go-mester',
        'FDA godkjenner AI for diabetisk retinopati',
        'COVID-19: AI for vaksine og diagnose',
        'ChatGPT og generativ AI'


# Continue

-->