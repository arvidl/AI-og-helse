# Uke 3: Dyplæring og Konvolusjonelle Nevrale Nettverk

## 🎯 Ukens Læringsmål

Etter denne uken skal du:
- **Forstå** hvordan konvolusjonelle nevrale nettverk (CNN) fungerer
- **Bygge** og **trene** en CNN-modell fra bunnen av
- **Evaluere** modellens ytelse med metrikker og visualisering
- **Bruke** forklarbar AI (Grad-CAM) for å forstå modellens beslutninger
- **Sammenligne** naturlige og medisinske bilder for AI-analyse
- **Kjenne til** moderne verktøy som fastMONAI for medisinsk AI

## �� Innhold

### Notebooks

#### Blomsterklassifikasjon (Grunnleggende CNN)
1. **[02a_cnn_bildeklassifikasjon.ipynb](02a_cnn_bildeklassifikasjon.ipynb)** - Miljøoppsett, datasett og CNN-arkitektur
2. **[02b_cnn_trening.ipynb](02b_cnn_trening.ipynb)** - Trening og lagring av modell
3. **[02c_cnn_testing.ipynb](02c_cnn_testing.ipynb)** - Testing, evaluering og Grad-CAM
4. **[02d_cnn_konklusjon.ipynb](02d_cnn_konklusjon.ipynb)** - Oppsummering og veien videre

#### Medisinsk Bildeanalyse
5. **[03_medisinsk_bildeklassifikasjon_MR.ipynb](03_medisinsk_bildeklassifikasjon_MR.ipynb)** - MRI-bildeanalyse og demens-deteksjon

#### Ansiktsuttrykk og Emosjoner
6. **[04a_ansiktsutrykk_klassifikasjon.ipynb](04a_ansiktsutrykk_klassifikasjon.ipynb)** - Emosjonsklassifikasjon del 1
7. **[04b_ansiktsutrykk_klassifikasjon.ipynb](04b_ansiktsutrykk_klassifikasjon.ipynb)** - Emosjonsklassifikasjon del 2
8. **[04c_ansiktsutrykk_klassifikasjon.ipynb](04c_ansiktsutrykk_klassifikasjon.ipynb)** - Emosjonsklassifikasjon del 3

### Oppgaver
- **Praktisk øvelse**: Bygg og tren din egen CNN-modell
- **Eksperimentering**: Test ulike hyperparametere og arkitekturer
- **Refleksjon**: Sammenlign naturlige vs medisinske bilder
- **Forklarbar AI**: Analyser modellens beslutninger med Grad-CAM
- **Medisinsk AI**: Utforsk MRI-bildeanalyse og demens-deteksjon
- **Emosjonsanalyse**: Test ansiktsuttrykk-klassifikasjon

## 🚀 Hurtigstart

```python
# Sjekk at PyTorch fungerer
import torch
print(f"PyTorch versjon: {torch.__version__}")
print(f"CUDA tilgjengelig: {torch.cuda.is_available()}")
print(f"MPS tilgjengelig: {torch.backends.mps.is_available()}")
print("🎉 Klar for CNN-trening!")
```

## 📖 Lesestoff

### Nyttig
- **CNN-grunnleggende**: [Convolutional Neural Networks - 3Blue1Brown](https://www.youtube.com/watch?v=aircAruvnKk)
- **Medisinsk AI**: [Deep Learning for Medical Imaging - Nature]()
- **Forklarbar AI**: [Grad-CAM: Visual Explanations - arXiv](https://arxiv.org/abs/1610.02391)
- **fastMONAI**: [Bergen-basert medisinsk AI](https://fastmonai.no/)

### Kjekt å vite
- **Attention Mechanisms**: [Attention is all you need - Vaswani et al.](https://arxiv.org/abs/1706.03762)
- **Medisinsk bildeanalyse**: [MONAI - Medical Open Network for AI](https://monai.io/)
- **Etikk i medisinsk AI**: [Ethical challenges ... PLOS Digit Health, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11977975/)

## 💭 Refleksjonsspørsmål

1. Hvordan skiller CNN seg fra tradisjonelle nevrale nettverk?
2. Hvorfor er konvolusjonelle lag effektive for bildeanalyse?
3. Hvilke utfordringer ser du med AI i medisinsk bildeanalyse?
4. Hvordan kan forklarbar AI styrke tilliten til medisinske AI-systemer?
5. Hva er forskjellen mellom naturlige og medisinske bilder for AI?
6. Hvordan kan emosjonsanalyse hjelpe i helsevesenet?
7. Hvilke etiske utfordringer ser du med ansiktsuttrykk-analyse?

## 👩‍🏫 Diskutere med andre eller en AI sparringspartner?

- **Tekniske spørsmål**: Diskuter CNN-arkitektur og hyperparametere
- **Medisinske applikasjoner**: Hvilke sykdommer kan CNN hjelpe med å diagnostisere?
- **Etiske utfordringer**: Hvordan sikre rettferdighet i medisinsk AI?
- **Fremtidige muligheter**: Hvor ser du AI i medisin om 10 år?
- **Emosjonsanalyse**: Hvordan kan AI hjelpe med mental helse?

## ✅ Sjekkliste

- [ ] Les gjennom alle 8 notebooks i rekkefølge
- [ ] Kjør notebooks på Google Colab eller lokalt
- [ ] Tren din egen CNN-modell på blomsterdata
- [ ] Eksperimenter med ulike hyperparametere
- [ ] Test Grad-CAM på dine egne bilder
- [ ] Reflekter over sammenligningen natur vs medisin
- [ ] Utforsk MRI-bildeanalyse og demens-deteksjon
- [ ] Test ansiktsuttrykk-klassifikasjon
- [ ] Utforsk fastMONAI for medisinsk AI
- [ ] Forberede til uke04-generativ-ai

## 🔗 Relaterte ressurser

- **3Blue1Brown**: [Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- **PyTorch Tutorials**: [Deep Learning with PyTorch](https://pytorch.org/tutorials/)
- **Medisinsk AI**: [AI in Medicine - Stanford](https://aimi.stanford.edu/)
- **Norsk AI**: [fastMONAI - Bergen](https://fastmonai.no/)

## 🎓 Veien videre

Etter denne uken er du klar for:
- **Uke 4**: Generativ AI og transformer-arkitektur
- **Uke 5**: Multimodal AI (tekst, bilde, lyd)
- **Uke 6**: Klinisk praksis og implementering
- **Uke 7**: Velferdsteknologi og brukeropplevelse
- **Uke 8**: Etikk, regulering og implementering