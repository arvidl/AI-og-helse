# Uke 2: Klassisk Maskinlæring i Helse

## �� Ukens Læringsmål

Etter denne uken skal du:
- **Forstå** hva maskinlæring er og hvordan det relaterer til klinisk erfaring
- **Skille** mellom supervised og unsupervised learning med helseeksempler
- **Bygge** enkle ML-modeller (beslutningstrær og Random Forest) for medisinsk prediksjon
- **Evaluere** modeller med klinisk relevante metrikker (sensitivitet, spesifisitet, PPV, NPV)
- **Tolke** forvirringsmatrise og ROC-kurver i medisinsk kontekst
- **Identifisere** anvendelsesområder for klassisk ML i ditt fagområde

## 📚 Innhold

### Notebooks

#### Grunnleggende Maskinlæring
1. **[01-klassisk-ml-101.ipynb](01-klassisk-ml-101.ipynb)** - Introduksjon til maskinlæring for helsepersonell
2. **[02-fra-symptom-til-diagnose.ipynb](02-fra-symptom-til-diagnose.ipynb)** - Praktisk diabetesprediksjon

### Oppgaver
- **Refleksjonsoppgave**: 16 spørsmål om konseptuell forståelse
- **Egen dataanalyse**: Modifiser diabetesdatasettet med egne parametre
- **Klinisk case-studie**: Velg et helseproblem fra ditt fagområde
- **Etisk refleksjon**: Analyser etiske utfordringer ved AI i helse
- **Visualisering**: Lag presentasjon som forklarer ML-konsepter til kolleger

## 🚀 Hurtigstart

```python
# Sjekk at scikit-learn fungerer
import sklearn
import pandas as pd
import numpy as np
print(f"scikit-learn versjon: {sklearn.__version__}")
print(f"pandas versjon: {pd.__version__}")
print(f"numpy versjon: {np.__version__}")
print("🎉 Klar for maskinlæring!")
```

## 📖 Lesestoff

### Nyttig
- **ML-grunnleggende**: [Introduction to Machine Learning - scikit-learn](https://scikit-learn.org/stable/user_guide.html)
- **Medisinsk ML**: [Machine Learning in Medicine - Nature]()
- **Klinisk evaluering**: [Clinical Prediction Models - Steyerberg](https://link.springer.com/book/10.1007/978-3-030-16399-0)
- **Etikk i medisinsk AI**: [Ethical challenges in medical AI - PLOS Digital Health]()

### Kjekt å vite
- **Beslutningstrær**: [Decision Trees in Healthcare - CUP](https://www.cambridge.org/core/books/abs/dataguided-healthcare-decision-making/how-healthcare-decision-trees-emerge-and-function/9B4B93CFB31A330EE84132FFDE929EAA)
- **Random Forest**: [Random Forest for Medical Diagnosis]()
- **ROC-kurver**: [ROC Analysis in Medical Research]()

## �� Refleksjonsspørsmål

1. Hvordan skiller maskinlæring seg fra tradisjonell klinisk diagnostikk?
2. Hvorfor er beslutningstrær intuitive for helsepersonell?
3. Hvilke kliniske metrikker er viktigst for din spesialitet?
4. Hvordan kan unsupervised learning hjelpe med pasientgruppering?
5. Hva er forskjellen mellom sensitivitet og spesifisitet?
6. Hvordan balanserer du false positive vs false negative i klinisk praksis?
7. Hvilke etiske utfordringer ser du med AI-baserte beslutningsstøttesystemer?

## 👩‍🏫 Diskutere med andre eller en AI sparringspartner?

- **Tekniske spørsmål**: Diskuter ML-algoritmer og evalueringsmetrikker
- **Kliniske applikasjoner**: Hvilke helseproblemer kan ML hjelpe med å løse?
- **Etiske utfordringer**: Hvordan sikre rettferdighet og transparens i medisinsk AI?
- **Implementering**: Hvordan introdusere ML i klinisk praksis?
- **Evaluering**: Hvilke metrikker er viktigst for din spesialitet?

## ✅ Sjekkliste

- [ ] Les gjennom begge notebooks i rekkefølge
- [ ] Kjør notebooks på Google Colab eller lokalt
- [ ] Bygg din egen diabetesprediksjonsmodell
- [ ] Eksperimenter med ulike hyperparametere
- [ ] Test ulike evalueringsmetrikker
- [ ] Reflekter over sammenligningen tradisjonell vs ML-basert diagnostikk
- [ ] Utforsk unsupervised learning med clustering
- [ ] Fullfør refleksjonsoppgaven
- [ ] Velg en utforskende oppgave basert på interesse
- [ ] Forberede til uke03-dyplæring

## 🔗 Relaterte ressurser

- **scikit-learn**: [Machine Learning in Python](https://scikit-learn.org/stable/)
- **Pandas**: [Data Analysis Library](https://pandas.pydata.org/)
- **Matplotlib**: [Data Visualization](https://matplotlib.org/)
- **Medisinsk ML**: [Machine Learning in Medicine - Stanford](https://aimi.stanford.edu/)

## 🎓 Veien videre

Etter denne uken er du klar for:
- **Uke 3**: Dyplæring og konvolusjonelle nevrale nettverk
- **Uke 4**: Generativ AI og transformer-arkitektur
- **Uke 5**: Multimodal AI (tekst, bilde, lyd)
- **Uke 6**: Klinisk praksis og implementering
- **Uke 7**: Velferdsteknologi og brukeropplevelse
- **Uke 8**: Etikk, regulering og implementering

## ⏰ Anbefalt progresjon

### 📅 Dag 1: Grunnlag
- Gjennomfør `01-klassisk-ml-101.ipynb`
- Les gjennom refleksjonsspørsmålene

### �� Dag 2-3: Praksis
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