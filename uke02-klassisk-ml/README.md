# Uke 02: klassisk ml

## 🎯 Læringsmål

### 🧠 Grunnleggende forståelse
- **Forstå** hva maskinlæring er og hvordan det relaterer til klinisk erfaring og beslutningstagning
- **Skille** mellom supervised og unsupervised learning med konkrete helseeksempler
- **Gjenkjenne** hvordan beslutningstrær følger klinisk resonnering ("hvis-så" logikk)
- **Identifisere** når maskinlæring kan være nyttig vs. problematisk i helsevesenet

### 🔧 Tekniske ferdigheter
- **Bruke** Python og scikit-learn for grunnleggende maskinlæring
- **Implementere** enkle ML-modeller (beslutningstrær og Random Forest) for medisinsk prediksjon
- **Forberede** data for maskinlæring (feature engineering og kategoriske variabler)
- **Visualisere** modellresultater og beslutningstrær på en tolkbar måte

### 📊 Evaluering og validering
- **Anvende** klinisk relevante evalueringsmetrikker (sensitivitet, spesifisitet, PPV, NPV)
- **Tolke** confusion matrix og ROC-kurver i medisinsk kontekst
- **Vurdere** når høy nøyaktighet ikke nødvendigvis er klinisk nyttig
- **Balansere** false positive vs. false negative basert på klinisk alvorlighet

### 🏥 Klinisk anvendelse
- **Bygge** et komplett diabetesprediksjonssystem fra symptomer til behandlingsanbefaling
- **Identifisere** viktige risikofaktorer gjennom feature importance analyse
- **Oppdage** skjulte pasientgrupper ved hjelp av clustering (unsupervised learning)
- **Sammenligne** ulike modellers prestasjon for samme kliniske problem

### 🤔 Kritisk tenkning
- **Evaluere** styrker og svakheter ved klassisk maskinlæring i klinisk praksis
- **Diskutere** etiske og sikkerhetsmessige aspekter ved AI-baserte beslutningsstøttesystemer
- **Vurdere** når tradisjonelle kliniske retningslinjer er bedre enn ML-modeller
- **Reflektere** over hvordan AI kan supplere (ikke erstatte) klinisk ekspertise

### 🎓 Læringsutbytte
Etter uke 2 skal du kunne:
- ✅ **Forklare** maskinlæring til kolleger uten teknisk bakgrunn
- ✅ **Bygge** en enkel prediksjonsmodell for helserelaterte problemer
- ✅ **Evaluere** ML-modeller med fokus på klinisk nytte, ikke bare teknisk nøyaktighet
- ✅ **Identifisere** anvendelsesområder for klassisk ML i ditt fagområde
- ✅ **Diskutere** kvalitetsmetrikker som er relevante for helsevesenet
- ✅ **Forberede** deg på mer avanserte AI-teknikker i senere uker

## 📚 Innhold

### 📖 Notebook 1: [`01-klassisk-ml-101.ipynb`](01-klassisk-ml-101.ipynb) 
**Introduksjon til maskinlæring for helsepersonell (20-30 minutter)**

- **Del 1:** Hva er maskinlæring egentlig?
  - Analogi til klinisk erfaring og mønstertenkjening
  - Forskjell mellom menneskebasert og maskinbasert læring
  
- **Del 2:** To hovedtyper maskinlæring
  - Supervised learning ("med fasit") - eksempler fra medisin
  - Unsupervised learning ("uten fasit") - pasientgruppering og mønsteroppdagelse
  
- **Del 3:** Beslutningstrær - maskinens "kliniske resonnering"
  - Hvordan AI følger hvis-så logikk
  - Sammenligning med kliniske retningslinjer
  
- **Del 4:** Grunnleggende Python (kun det nødvendige!)
  - Variabler, lister og enkle operasjoner
  - If-setninger og grunnleggende programmering
  
- **Del 5:** Mini-eksempel med ekte data
  - Pasienttabell og enkle analyser
  - Introduksjon til evaluering av modeller

### 🏥 Notebook 2: [`02-fra-symptom-til-diagnose.ipynb`](02-fra-symptom-til-diagnose.ipynb)
**Praktisk diabetesprediksjon (60-90 minutter)**

- **Del 1:** Case-studie - Tidlig oppdagelse av diabetes type 2
  - Generering av realistisk syntetisk pasientdata (1000 pasienter)
  - Utforskende dataanalyse og risikofaktor-visualisering
  
- **Del 2:** Bygge prediktive modeller
  - Data-forberedelse og feature engineering
  - Implementering av beslutningstre
  - Feature importance analyse
  
- **Del 3:** Modell-evaluering med klinisk fokus
  - Confusion matrix og klinisk tolkning
  - Sensitivitet, spesifisitet, PPV og NPV
  - ROC-kurver og AUC-scores
  
- **Del 4:** Random Forest - robust tilnærming
  - Sammenligning av modellytelse
  - Når kompleksitet gir mervardi
  
- **Del 5:** Unsupervised learning - pasientgrupper
  - K-means clustering for risikostratifisering
  - Identifisering av pasientgrupper (lav/moderat/høy risiko)
  - Klinisk tolkning av cluster-karakteristikker

---

## 🎯 Oppgaver

### 📝 Hovedoppgaver

#### 1. **Refleksjonsoppgave: Konseptuell forståelse** 
*Etter gjennomgang av begge notebooks*
- Besvar 16 refleksjonsspørsmål som dekker:
  - Konseptuelle sammenhenger (tradisjonell vs. ML-basert diagnostikk)
  - Modellforståelse og tolkbarhet
  - Klinisk evaluering og metrikker
  - Implementering i helsevesenet
  - Kritisk tenkning og begrensninger
- **Ressurs:** `ressurser/02-refleksjoner.md` (inkluderer forslag til besvarelser)


### 🔬 Utforskende oppgaver

#### 2. **Egen dataanalyse**
- Modifiser diabetesdatasettet med egne parametre
- Test ulike risikofaktorer og deres påvirkning på modellytelse
- Eksperimenter med ulike evalueringsmetrikker

#### 3. **Klinisk case-studie**
- Velg et helseproblem fra ditt eget fagområde
- Identifiser relevante prediktorer og utfall
- Skissér hvordan en ML-tilnærming kunne implementeres

#### 4. **Etisk refleksjon**
- Analyser potensielle etiske utfordringer ved AI i ditt fagområde
- Diskuter bias, transparens og pasientautonomi
- Foreslå retningslinjer for ansvarlig AI-bruk

### 📊 Valgfrie verktøy-oppgaver

#### 5. **Visualisering og kommunikasjon**
- Lag presentasjon som forklarer ML-konsepter til kolleger
- Utvikle intuitive visualiseringer av modellresultater
- Øv på å oversette tekniske resultater til klinisk språk

#### 6. **Utvidet modellering**
- Prøv andre ML-algoritmer (logistisk regresjon, SVM)
- Implementer cross-validation for robust evaluering
- Utforsk feature selection teknikker

---

## ⏰ Anbefalt progresjon

### 📅 Dag 1: Grunnlag
- Gjennomfør `01-klassisk-ml-101.ipynb`
- Les gjennom refleksjonsspørsmålene

### 📅 Dag 2-3: Praksis
- Arbeide gjennom `02-fra-symptom-til-diagnose.ipynb`
- Begynn på refleksjonsoppgaven

### 📅 Dag 4: Anvendelse
- Fullfør refleksjonsoppgaven
- Prøv prompt engineering workshop
- Velg en utforskende oppgave basert på interesse

### 📅 Dag 5: Integrasjon
- Diskuter læring med kolleger
- Identifiser anvendelser i eget fagområde
- Forbered deg på neste ukes emner
