# 🏥 AI og Helse 

**Åpen variant** av et avansert kurs i kunstig intelligens for medisinere og personell i helse- og omsorgssektoren.

[![Åpne kursnettsiden](https://img.shields.io/badge/Kursnettside-AI%20og%20Helse-7d3c98?style=for-the-badge)](https://arvidl.github.io/AI-og-helse/)

> [!TIP] 
> Start på kursnettsiden for en inngang til ukeoversikt, ressurser og videre lenker til notebooks:
> [Åpne kursnettsiden](https://arvidl.github.io/AI-og-helse/)

> [!TIP]
> Forelesningsversjonen forligger også som [Google Slides](https://docs.google.com/presentation/d/e/2PACX-1vSzWu6-_2T9G9SopUObXy_tn_t1qxzXMe9PZeFBnOMN-xUtAJNZujn5ZGJ_x11zSq4jKVP_i8z6AfuU/pub?start=false&loop=false&delayms=3000) <br>
> Relatert presentasjon: HVL's THO802 Implementering av e-helse ["KI i helse"](https://docs.google.com/presentation/d/e/2PACX-1vSgNis1ri7ZyaB6PMe4X3vVTY7BYanVDdktyB196LogRuNj01fMuY-zIbs508ieuPhzucy4FFlTnRPT/pub?start=false&loop=false&delayms=3000)  (2 x 45 min)<br>
> eller gå via [kursnettsiden med QR-kode](https://arvidl.github.io/AI-og-helse/).


## 📚 Kursstruktur

- **Del 1 (Uke 1-6):** AI-fundamentet - fra AI 1.0 til AI 2.0
- **Del 2 (Uke 7-8):** Anvendelse og ansvar i medisin, helse og omsorg

### Kurskart: fra grunnlag til ansvarlig implementering

Kurset følger en tydelig rød tråd fra grunnleggende begreper til mer avanserte metoder. I uke 1 legges det konseptuelle og historiske grunnlaget. Uke 2 tar for seg klassisk maskinlæring, med vekt på hvordan modeller lærer fra data og hvordan de bør vurderes i praksis. I uke 3 utvides perspektivet til dyplæring, særlig for bilder, signaler og komplekse mønstre.

I uke 4 åpnes feltet mot generativ KI, språkmodeller, multimodale systemer og API-bruk. Uke 5 bygger videre på dette ved å vise hvordan slike modeller kan inngå i agentiske arbeidsflyter med verktøybruk, RAG, logging og menneskelig kontroll. Uke 6 tar opp hva som kreves før modellene kan nærme seg klinisk praksis: validering, kalibrering, terskler, vurdering av subgrupper, monitorering og tilpasning til arbeidsflyt.

I uke 7 utvides perspektivet til hjem, omsorg og velferdsteknologi, der sensorer, varsling og beslutningsstøtte må vurderes i møte med reelle tjenester. Uke 8 avslutter læringsløpet med ansvarlig implementering og sentrale temaer som personvern, bias/fairness, regulering, etikk, dokumentasjon og trustworthy AI.


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

### Hvordan kurset kan brukes
"... på svømmekurs bør man oppholde seg mye i bassenget ..."
- Det anbefales å "gå i bassenget" (= eksperimentere med notebooks)
- For noen i målgruppen kan et realistisk læringsutbytte oppnås ved kun å **lese**, **inspisere** og **kontemplere** tekst, kode, figurer og referanser direkte i GitHub-repositoriet (https://github.com/arvidl/AI-og-helse), altså "holde seg på land ...", kombinert med bruk av en AI-sparringspartner

## 📂 Repo-struktur

```
AI-og-helse/
├── uke01-introduksjon/          # Introduksjon til AI
├── uke02-klassisk-ml/           # Klassisk maskinlæring
├── uke03-dyplæring/             # Dyplæring og nevrale nettverk
├── uke04-generativ-ai/          # Generativ AI, foundation models og multimodalitet
├── uke05-agentisk-ai/           # Agentisk AI i helse og omsorg
├── uke06-klinisk-praksis/       # Klinisk praksis, beslutningsstøtte og validering
├── uke07-velferdsteknologi/     # Sensorer, beslutningsstøtte og trygg teknologi
├── uke08-etikk-implementering/  # Etikk, bias/fairness, GDPR, MDR og trustworthy AI
├── ressurser/                   # Ordliste, verktøy og artikler
├── utils/                       # Hjelpefunksjoner
├── intro_openai_anthropic.ipynb # API-introduksjon og nøkkelhåndtering
├── environment.yml              # Standard lokalt miljø
├── environment_cuda.yml         # NVIDIA/CUDA-variant for Linux/Windows
└── requirements.txt             # Pip-avhengigheter
```

## 📚 Notebok-oversikt med Colab-badges

### Uke 1: Introduksjon til AI
| Notebok | Beskrivelse | Colab |
|---------|-------------|-------|
| `00-velkommen.ipynb` | Velkommen og kursoversikt | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke01-introduksjon/00-velkommen.ipynb) |
| `01-test-meg.ipynb` | Test av miljø og pakker | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke01-introduksjon/01-test-meg.ipynb) |
| `02-hva-er-ai.ipynb` | Hva er kunstig intelligens? | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke01-introduksjon/02-hva-er-ai.ipynb) |
| `03-ai-historie-helse.ipynb` | AI-historie i helsevesenet | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke01-introduksjon/03-ai-historie-helse.ipynb) |
| `04-ai-ml-dl-forskjeller.ipynb` | AI, ML og dyplæring | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke01-introduksjon/04-ai-ml-dl-forskjeller.ipynb) |
| `05-regelbaserte-systemer.ipynb` | Regelbaserte systemer | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke01-introduksjon/05-regelbaserte-systemer.ipynb) |
| `99-oppsett-miljø.ipynb` | Miljøoppsett guide | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke01-introduksjon/99-oppsett-miljø.ipynb) |

### Uke 2: Klassisk maskinlæring
| Notebok | Beskrivelse | Colab |
|---------|-------------|-------|
| `01-klassisk-ml-101.ipynb` | Grunnleggende maskinlæring | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke02-klassisk-ml/01-klassisk-ml-101.ipynb) |
| `02-fra-symptom-til-diagnose.ipynb` | Fra symptom til diagnose | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke02-klassisk-ml/02-fra-symptom-til-diagnose.ipynb) |

### Uke 3: Dyplæring og nevrale nettverk
| Notebok | Beskrivelse | Colab |
|---------|-------------|-------|
| `01a_nn_intro.ipynb` | Nevrale nettverk i menneske og maskin<br> - grunnleggende teori | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke03-dyplæring/01a_nn_intro.ipynb) |
| `01b_læring_i_nn.ipynb` | Læring i nevrale nettverk<br> - i menneske og i maskin| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke03-dyplæring/01b_læring_i_nn.ipynb) |
| `01c_UCI_heart_disease_klassifikasjon.ipynb` | Hjertesykdom-klassifikasjon<br> (bruk av åpne data fra UCI)| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke03-dyplæring/01c_UCI_heart_disease_klassifikasjon.ipynb) |
| `01d_EKG_arytmi_klassifikasjon.ipynb` | Hjertearytmi-klassifikasjon med CNN<br>(bruk av åpne EKG data fra PhysioNet) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke03-dyplæring/01d_EKG_arytmi_klassifikasjon.ipynb) |
| `02a_cnn_bildeklassifikasjon.ipynb` | CNN bildeklassifikasjon (5 blomsterarter) - intro <br> (bruk av åpne data  fra Kaggle) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke03-dyplæring/02a_cnn_bildeklassifikasjon.ipynb) |
| `02b_cnn_trening.ipynb` | CNN trening | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke03-dyplæring/02b_cnn_trening.ipynb) |
| `02c_cnn_testing.ipynb` | CNN testing | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke03-dyplæring/02c_cnn_testing.ipynb) |
| `02d_cnn_konklusjon.ipynb` | CNN konklusjon | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke03-dyplæring/02d_cnn_konklusjon.ipynb) |
| `03_medisinsk_bildeklassifikasjon_MR.ipynb` | Medisinsk MR-bildeklassifikasjon - demens<br> (bruk av åpne data fra OASIS) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke03-dyplæring/03_medisinsk_bildeklassifikasjon_MR.ipynb) |
| `04a_ansiktsutrykk_klassifikasjon.ipynb` | Emosjonelle ansiktsutrykk - del 1 (bygging)<br>(bruk av åpne data fra FER2013)| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke03-dyplæring/04a_ansiktsutrykk_klassifikasjon.ipynb) |
| `04b_ansiktsutrykk_klassifikasjon.ipynb` | Emosjonelle ansiktsutrykk - del 2 (trening) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke03-dyplæring/04b_ansiktsutrykk_klassifikasjon.ipynb) |
| `04c_ansiktsutrykk_klassifikasjon.ipynb` | Emosjonelle ansiktsutrykk - del 3 (evaluering)| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke03-dyplæring/04c_ansiktsutrykk_klassifikasjon.ipynb) |

### Uke 4 og 5: Moderne AI i praksis

Uke 4 gir en innføring i generativ AI, foundation models og multimodalitet. Uke 5 bygger videre på dette og viser hvordan slike modeller kan inngå i agentiske systemer med verktøybruk, arbeidsflyt og helsefaglige anvendelser.

Uke 6 tar stafettpinnen videre fra demo til klinisk praksis: selv gode LLM-, RAG- og agenteksempler må vurderes gjennom validering, kalibrering, terskelvalg, subgruppeanalyse, monitorering og menneskelig arbeidsflyt før de kan nærme seg pasientnær bruk.

Uke 7 flytter disse kravene fra klinisk praksis til hjem, omsorg og velferdsteknologi, der sensorer, varsler, robotikk og beslutningsstøtte må vurderes mot falske alarmer, brukerautonomi, tjenestearbeidsflyt og ansvar.

Uke 8 samler hele kjeden i ansvarlig implementering: personvern, dataminimering, bias/fairness, regulering, etiske dilemmaer, ansvar og trustworthy AI.

### Uke 4: Generativ AI, foundation models og multimodalitet
| Notebok | Beskrivelse | Colab |
|---------|-------------|-------|
| `01_transformer_arkitektur.ipynb` | Transformer-arkitektur | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke04-generativ-ai/01_transformer_arkitektur.ipynb) |
| `02_llm_grunnleggende.ipynb` | LLM grunnleggende | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke04-generativ-ai/02_llm_grunnleggende.ipynb) |
| `03_prompt_engineering.ipynb` | Prompt engineering | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke04-generativ-ai/03_prompt_engineering.ipynb) |
| `04_chatgpt_claude_api.ipynb` | ChatGPT og Claude API | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke04-generativ-ai/04_chatgpt_claude_api.ipynb) |
| `10_bilde_tekst_clip_zero_shot_blomster.ipynb` | CLIP zero-shot på blomster (bilde + tekst) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke04-generativ-ai/10_bilde_tekst_clip_zero_shot_blomster.ipynb) |
| `oppgaver/prompt_workshop.ipynb` | Workshop: anvendt prompt-øving for helseoppgaver | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke04-generativ-ai/oppgaver/prompt_workshop.ipynb) |

### Uke 5: Agentisk AI
| Notebok | Beskrivelse | Colab |
|---------|-------------|-------|
| `01_chatbot_workflow_agent.ipynb` | Chatbot, workflow og agent: begreper og enkle eksempler | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke05-agentisk-ai/01_chatbot_workflow_agent.ipynb) |
| `02_agentisk_ai_i_helse.ipynb` | Agentisk AI i helse: verktøybruk, RAG, minne, case og sikkerhet | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke05-agentisk-ai/02_agentisk_ai_i_helse.ipynb) |
| `03_crewai_fordypning_rehabilitering.ipynb` | Frivillig fordypning: CrewAI i rehabilitering med syntetisk case og tverrfaglige roller (Gemini-nøkkel for operativ demo) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke05-agentisk-ai/03_crewai_fordypning_rehabilitering.ipynb) |
| `04_agentisk_ai_perspektiver.ipynb` | Perspektiver: agentisk AI, logging, styring, lokale modeller og menneskelig kontroll | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke05-agentisk-ai/04_agentisk_ai_perspektiver.ipynb) |

### Uke 6: Klinisk praksis
| Notebok | Beskrivelse | Colab |
|---------|-------------|-------|
| `01_risikomodell_logistisk_regresjon_kalibrering_shap.ipynb` | Syntetisk risikomodell: diskriminering, kalibrering, SHAP og klinisk tolkning | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke06-klinisk-praksis/01_risikomodell_logistisk_regresjon_kalibrering_shap.ipynb) |
| `02_klinisk_beslutningsstøtte_terskler_og_avveininger.ipynb` | Fra risikoanslag til terskler, handlinger og kliniske avveininger | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke06-klinisk-praksis/02_klinisk_beslutningsstøtte_terskler_og_avveininger.ipynb) |
| `03_validering_generalisering_og_subgrupper.ipynb` | Ekstern validering, distribusjonsskifte, subgrupper og generaliserbarhet | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke06-klinisk-praksis/03_validering_generalisering_og_subgrupper.ipynb) |
| `04_fra_modell_til_klinisk_arbeidsflyt.ipynb` | Overgangen fra AI-demo til klinisk arbeidsflyt, monitorering og menneskelig kontroll | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke06-klinisk-praksis/04_fra_modell_til_klinisk_arbeidsflyt.ipynb) |

### Uke 7: Velferdsteknologi
| Notebok | Beskrivelse | Colab |
|---------|-------------|-------|
| `01_robotnavigasjon_i_rutenett_med_astar.ipynb` | A* rutefinning som teknisk demo for trygg robotnavigasjon | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke07-velferdsteknologi/01_robotnavigasjon_i_rutenett_med_astar.ipynb) |
| `02_sensorer_aktivitet_og_hendelsesforståelse.ipynb` | Syntetiske sensordata: aktivitet, avvik, kontekst og falske alarmer | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke07-velferdsteknologi/02_sensorer_aktivitet_og_hendelsesforståelse.ipynb) |
| `03_beslutningsstøtte_i_hjem_og_omsorg.ipynb` | Varsling, prioritering, alarmtretthet og ansvar i hjem/omsorg | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke07-velferdsteknologi/03_beslutningsstøtte_i_hjem_og_omsorg.ipynb) |
| `04_sikkerhet_etikk_og_menneske_maskin_samspill.ipynb` | Trygg tjenesteimplementering, autonomi, personvern og menneskelig kontroll | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke07-velferdsteknologi/04_sikkerhet_etikk_og_menneske_maskin_samspill.ipynb) |

### Uke 8: Etikk og implementering
| Notebok | Beskrivelse | Colab |
|---------|-------------|-------|
| `01_gdpr_personvern.ipynb` | GDPR, personvern, rettslig grunnlag, samtykke og dataminimering | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke08-etikk-implementering/01_gdpr_personvern.ipynb) |
| `02_bias_rettferdighet.ipynb` | Bias, fairness, ulik ytelse og rettferdighet på tvers av grupper | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke08-etikk-implementering/02_bias_rettferdighet.ipynb) |
| `03_ce_mdr_regulering.ipynb` | CE-merking, MDR, SaMD, AI Act, dokumentasjon og ansvar | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke08-etikk-implementering/03_ce_mdr_regulering.ipynb) |
| `04_ai_etikk_i_medisinen.ipynb` | Kliniske dilemmaer, etiske prinsipper, ansvar og menneskelig kontroll | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke08-etikk-implementering/04_ai_etikk_i_medisinen.ipynb) |
| `05_trustworthy_ai_i_helse.ipynb` | Trustworthy AI: robusthet, usikkerhet, validering, monitorering og drift | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke08-etikk-implementering/05_trustworthy_ai_i_helse.ipynb) |

### Andre notebooks
| Notebok | Beskrivelse | Colab |
|---------|-------------|-------|
| `intro_openai_anthropic.ipynb` | OpenAI og Anthropic introduksjon | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/intro_openai_anthropic.ipynb) |

## 💻 Teknologi

- **Python 3.12+**
- **Jupyter Notebooks** for interaktiv læring
- **Google Colab** for skybasert notebook-kjøring og eksperimentering
- **AI-verktøy:** OpenAI (gpt-), Anthropic (claude-), Scikit-learn, PyTorch, ...


## 🛠️ Teknisk støtte

- **GitHub Issues:** [Rapporter problemer](https://github.com/arvidl/AI-og-helse/issues)
- **Diskusjoner:** kollegaer, medstudenter, AI-sparringspartner(e)


## 📖 Læringsressurser

- [Ordliste](ressurser/ordliste.md)
- [Verktøyguider](ressurser/verktoy/)
- [Artikkelsamling](ressurser/artikler/)
- [Google Colab-oppsett](COLAB_SETUP.md)
- [Colab-kompatibilitetssjekkliste](COLAB_COMPATIBILITY_CHECKLIST.md)
- [Kaggle-data og API-tilgang](kaggle_data_tilgang.md)


## 👥 Målgruppe

- Helsepersonell (leger, sykepleiere, radiografer, terapeuter, psykologer)
- Ansatte i omsorgstjenesten (deler av kurset)
- Ledere i helse og omsorg (deler av kurset)
- IT- og digitaliseringsansvarlige (deler av kurset)
- Kvalitets- og utviklingsrådgivere (deler av kurset)

## 📅 Praktisk informasjon

- **Varighet:** 8 uker 
- **Arbeidsomfang:** 10-12 timer per uke
- **Læringsspråk (i Jupyter-notebooks):** Norsk (+ engelske fagtermer, for eksempel "notebooks")


## 📄 Lisens

Repoet er lisensiert under [MIT-lisensen](LICENSE). Copyright (c) 2026 Arvid Lundervold.

## 🙏 Bidragsytere

- Arvid Lundervold
- [Hvordan bidra](CONTRIBUTING.md)


### 🛠️ Hvordan kurset er laget og hvilke ressurser som er brukt

- Domenekunnskap, et godt nettverk av fagfeller ([nær](https://www.sciencedirect.com/science/article/pii/S0939388918301181?via%3Dihub) og [fjern](http://en.jnl.ac.cn/article/185.html)) og entusiasme for feltet
- Bruk av AI-kodeeditoren [Cursor](https://cursor.com/get-started) Ultra
- Utviklet på en MacBook Pro M4 Max
- Diverse lisenser og tjenester (GitHub, OpenAI, Anthropic, Perplexity, Google)
- Omtrent 40 timeverk for basisdelen


------

## 🚀 Kom i gang


### Bruk Google Colab (enkleste alternativ)

Gå til [repoets README på GitHub](https://github.com/arvidl/AI-og-helse/blob/main/README.md) og finn aktuell uke, fra `uke01-` til `uke08-`.

For eksempel: [uke01-introduksjon](https://github.com/arvidl/AI-og-helse/tree/main/uke01-introduksjon)

1. For hver notebook, trykk på [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/AI-og-helse/blob/main/uke01-introduksjon/00-velkommen.ipynb)
2. Notebooken vises da i din nettleser
3. Aksepter at den ikke er autorisert av Google ("Run anyway")
4. Lær deg bruk av Python og [Jupyter Notebooks](https://colab.research.google.com/github/jckantor/CBE30338/blob/master/docs/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.ipynb) i Google Colab ([FAQ](https://research.google.com/colaboratory/faq.html))


### For lokal utvikling - uv (anbefalt for Mac/Linux/PC uten CUDA)

[`uv`](https://docs.astral.sh/uv/) er anbefalt lokal løsning for vanlig notebook-kjøring på egen maskin. Det gir rask oppretting av virtuelt miljø, rask installasjon av pip-avhengigheter og fungerer godt sammen med `requirements.txt`.

```bash
# Klon repository
git clone https://github.com/arvidl/AI-og-helse.git
cd AI-og-helse

# Opprett virtuelt miljø med Python 3.12
uv venv --python 3.12

# Aktiver miljøet
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate   # Windows

# Installer avhengigheter
uv pip install -r requirements.txt

# Installer Jupyter kernel
python -m ipykernel install --user --name ai-helse-uv --display-name "Python 3.12 (AI-Helse uv)"

# Verifiser installasjon
python check_setup.py
```

[`CrewAI`](https://docs.crewai.com) er nå inkludert i standardmiljøet for det frivillige fordypningssporet i uke 05, blant annet notebooken `uke05-agentisk-ai/03_crewai_fordypning_rehabilitering.ipynb`.

**CUDA/NVIDIA-unntak: bruk conda**

Hvis du skal kjøre tunge dyplæringsnotebooks lokalt med NVIDIA-GPU og CUDA på Linux/Windows, bruk conda-miljøet i `environment_cuda.yml`. Dette er mer robust for CUDA-spesifikke binærpakker enn et rent `uv`/pip-miljø.

```bash
# Opprett CUDA-miljø fra `environment_cuda.yml`
conda env create -f environment_cuda.yml

# Aktiver miljøet
conda activate ai-helse-cuda

# Installer Jupyter kernel
python -m ipykernel install --user --name ai-helse-cuda --display-name "Python 3.12 (AI-Helse CUDA)"

# Verifiser installasjon
python check_setup.py
```

**Alternativ: conda uten CUDA**

Hvis du allerede bruker conda og ønsker et conda-basert CPU-/Mac-miljø, kan du fortsatt bruke `environment.yml`.

```bash
conda env create -f environment.yml
conda activate ai-helse
python -m ipykernel install --user --name ai-helse --display-name "Python 3.12 (AI-Helse)"
python check_setup.py
```

**Alternativ: vanlig pip/venv**

Dette fungerer også, men `uv` er normalt raskere og enklere å gjenskape.

```bash
python3.12 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate   # Windows
pip install --upgrade pip
pip install -r requirements.txt

# Verifiser installasjon
python check_setup.py
```

**For Cursor-brukere**
1. Åpne prosjektet i Cursor
2. Cursor vil normalt oppdage `.venv` automatisk
3. Velg "Python 3.12 (AI-Helse uv)" som interpreter/kernel
4. Alternativt: Cmd/Ctrl+Shift+P → "Python: Select Interpreter" → `.venv`


## API-nøkler for lokal kjøring


### NB

Hver kursdeltaker må selv skaffe, lagre og bruke sine egne API-nøkler.

Her er en enkel måte å gjøre det på:

---

#### 1. Skaff egne API-nøkler

Hver deltaker må selv registrere seg:

* **OpenAI:** [platform.openai.com](https://platform.openai.com/)
* **Google Gemini:** [aistudio.google.com](https://aistudio.google.com/app/apikey)
* **Anthropic:** [console.anthropic.com](https://console.anthropic.com/)

OpenAI og Anthropic krever normalt at man legger inn kort/betalingsinfo. Gemini kan ofte brukes med gratis kvote, men kvoter og modelltilgang kan endres over tid.

---

#### 2. Hvordan lagre nøklene trygt

Du kan velge én av to enkle metoder:

**a) `.env`-fil (anbefalt)**

1. Lag en fil i samme mappe som notebooken med navnet `.env`
2. Legg inn:

   ```
   OPENAI_API_KEY=sk-xxxx
   GEMINI_API_KEY=xxxx
   # Alternativt navn som også støttes i uke04:
   GOOGLE_API_KEY=xxxx
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
   gemini_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
   anthropic_key = os.getenv("ANTHROPIC_API_KEY")
   ```

**b) Direkte miljøvariabler (mer "avansert")**

* I terminal (før du starter Jupyter):

  ```bash
  export OPENAI_API_KEY="sk-xxxx"
  export GEMINI_API_KEY="xxxx"
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

**Google Gemini:**

```python
from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"))
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hei fra Gemini!"
)
print(response.text)
```

#### NB
* Husk, ikke dele noen egne nøkler i kursmaterialet – hver deltaker har ansvar for sine.
* Der det kan være aktuelt, har vi lagt inn et sjekksteg i notebooken som gir en feilmelding hvis nøkkel mangler:

  ```python
  if not openai_key or not anthropic_key:
      raise ValueError("Mangler API-nøkkel. Sett den i .env-filen først!")
  ```


## API-nøkler for kjøring i skyen

Dette gjelder kun for **Google Colab**.

For nærmere beskrivelse, se notebooken [`intro_openai_anthropic.ipynb`](./intro_openai_anthropic.ipynb).



---

#### Oppsummering

* Deltakere skaffer **egne nøkler** fra OpenAI, Google Gemini og/eller Anthropic.
* Nøklene lagres lokalt i `.env` eller som miljøvariabler dersom du kjører lokalt.
* Dersom du kjører i Google Colab, må du konsultere [`intro_openai_anthropic.ipynb`](./intro_openai_anthropic.ipynb).
* Aktuelle Notebooks er ferdig satt opp til å hente nøkler og bruke dem.

---





**Lykke til med kurset!** 🎓
