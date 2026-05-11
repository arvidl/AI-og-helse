# Colab Compatibility Checklist

This is the repo-based compatibility snapshot for all notebooks in `AI-og-helse`.

Every notebook now starts with a tagged Colab contract cell and a tagged bootstrap cell:

- `ai-og-helse-colab-contract`: Colab badge, recommended runtime, expected runtime and requirements.
- `ai-og-helse-colab-bootstrap`: `IN_COLAB` detection, minimal notebook-specific package installation, and shared helpers for Colab Secrets / local environment variables.

This checklist confirms that the notebooks have a consistent Colab entry path. It is still not a guarantee that every notebook has been fully executed end-to-end in a fresh Colab runtime.

## Status Legend

- **Ready:** Should run in Colab with no external credentials or prepared artifacts.
- **Manual setup:** Opens and bootstraps in Colab, but requires secrets, external data, Google Drive, uploaded files, model artifacts or GPU selection.
- **Utility:** Helper notebook rather than a primary course notebook.

## Ready

- [x] `uke01-introduksjon/00-velkommen.ipynb` - CPU, synthetic/inline data. Verified locally and in Colab by course maintainer, 2026-05-11.
- [x] `uke01-introduksjon/01-test-meg.ipynb` - CPU, installs `transformers` if missing. Verified locally and in Colab by course maintainer, 2026-05-11.
- [x] `uke01-introduksjon/02-hva-er-ai.ipynb` - CPU, synthetic/inline data. Verified locally and in Colab by course maintainer, 2026-05-11.
- [x] `uke01-introduksjon/03-ai-historie-helse.ipynb` - CPU, synthetic/inline data. Verified locally and in Colab by course maintainer, 2026-05-11.
- [x] `uke01-introduksjon/04-ai-ml-dl-forskjeller.ipynb` - CPU, synthetic/inline data. Verified locally and in Colab by course maintainer, 2026-05-11.
- [x] `uke01-introduksjon/05-regelbaserte-systemer.ipynb` - CPU, synthetic/inline data. Verified locally and in Colab by course maintainer, 2026-05-11.
- [x] `uke02-klassisk-ml/01-klassisk-ml-101.ipynb` - CPU, synthetic/inline data.
- [x] `uke02-klassisk-ml/02-fra-symptom-til-diagnose.ipynb` - CPU, synthetic data.
- [x] `uke03-dyplæring/01a_nn_intro.ipynb` - CPU, conceptual/demo notebook.
- [x] `uke03-dyplæring/01b_læring_i_nn.ipynb` - CPU, optional accelerator.
- [x] `uke03-dyplæring/01c_UCI_heart_disease_klassifikasjon.ipynb` - CPU, small open dataset workflow.
- [x] `uke03-dyplæring/02a_cnn_bildeklassifikasjon.ipynb` - CPU/GPU optional, setup cell standardized.
- [x] `uke03-dyplæring/02d_cnn_konklusjon.ipynb` - CPU, summary/conclusion notebook.
- [x] `uke04-generativ-ai/01_transformer_arkitektur.ipynb` - CPU, conceptual/demo notebook.
- [x] `uke04-generativ-ai/02_llm_grunnleggende.ipynb` - CPU, installs `tiktoken` if missing.
- [x] `uke05-agentisk-ai/01_chatbot_workflow_agent.ipynb` - CPU, synthetic examples.
- [x] `uke05-agentisk-ai/02_agentisk_ai_i_helse.ipynb` - CPU, synthetic examples.
- [x] `uke05-agentisk-ai/04_agentisk_ai_perspektiver.ipynb` - CPU, reflection/perspective notebook.
- [x] `uke06-klinisk-praksis/01_risikomodell_logistisk_regresjon_kalibrering_shap.ipynb` - CPU, installs `shap` if missing.
- [x] `uke06-klinisk-praksis/02_klinisk_beslutningsstøtte_terskler_og_avveininger.ipynb` - CPU, synthetic data.
- [x] `uke06-klinisk-praksis/03_validering_generalisering_og_subgrupper.ipynb` - CPU, synthetic data.
- [x] `uke06-klinisk-praksis/04_fra_modell_til_klinisk_arbeidsflyt.ipynb` - CPU, synthetic/inline data.
- [x] `uke07-velferdsteknologi/01_robotnavigasjon_i_rutenett_med_astar.ipynb` - CPU, simulated grid data.
- [x] `uke07-velferdsteknologi/02_sensorer_aktivitet_og_hendelsesforståelse.ipynb` - CPU, simulated sensor data.
- [x] `uke07-velferdsteknologi/03_beslutningsstøtte_i_hjem_og_omsorg.ipynb` - CPU, simulated data.
- [x] `uke07-velferdsteknologi/04_sikkerhet_etikk_og_menneske_maskin_samspill.ipynb` - CPU, synthetic/inline data.
- [x] `uke08-etikk-implementering/01_gdpr_personvern.ipynb` - CPU, synthetic/inline data.
- [x] `uke08-etikk-implementering/02_bias_rettferdighet.ipynb` - CPU, synthetic/inline data.
- [x] `uke08-etikk-implementering/03_ce_mdr_regulering.ipynb` - CPU, synthetic/inline data.
- [x] `uke08-etikk-implementering/04_ai_etikk_i_medisinen.ipynb` - CPU, synthetic/inline data.
- [x] `uke08-etikk-implementering/05_trustworthy_ai_i_helse.ipynb` - CPU, synthetic/inline data.

## Manual Setup

- [x] `intro_openai_anthropic.ipynb` - requires `OPENAI_API_KEY` and `ANTHROPIC_API_KEY` in Colab Secrets or local environment.
- [x] `uke01-introduksjon/99-oppsett-miljø.ipynb` - environment guide; Colab works, but the notebook is partly explanatory. Verified locally and in Colab by course maintainer, 2026-05-11.
- [x] `uke03-dyplæring/01d_EKG_arytmi_klassifikasjon.ipynb` - requires PhysioNet MIT-BIH data; installs `wfdb` if missing.
- [x] `uke03-dyplæring/02b_cnn_trening.ipynb` - requires prepared image data; GPU recommended.
- [x] `uke03-dyplæring/02c_cnn_testing.ipynb` - requires trained model artifacts from the previous notebook.
- [x] `uke03-dyplæring/03_medisinsk_bildeklassifikasjon_MR.ipynb` - downloads OASIS via `nilearn`; runtime and data download can be heavy.
- [x] `uke03-dyplæring/04a_ansiktsutrykk_klassifikasjon.ipynb` - requires Kaggle credentials for FER2013; GPU recommended.
- [x] `uke03-dyplæring/04b_ansiktsutrykk_klassifikasjon.ipynb` - requires Kaggle credentials and/or Google Drive model artifacts; GPU recommended.
- [x] `uke03-dyplæring/04c_ansiktsutrykk_klassifikasjon.ipynb` - requires Kaggle credentials and a saved model artifact.
- [x] `uke04-generativ-ai/03_prompt_engineering.ipynb` - live model calls require `GEMINI_API_KEY`/`GOOGLE_API_KEY`; OpenAI/Anthropic optional.
- [x] `uke04-generativ-ai/04_chatgpt_claude_api.ipynb` - live model calls require one or more provider API keys.
- [x] `uke04-generativ-ai/10_bilde_tekst_clip_zero_shot_blomster.ipynb` - downloads model weights; GPU optional.
- [x] `uke04-generativ-ai/oppgaver/prompt_workshop.ipynb` - live mode requires `OPENAI_API_KEY`; can be read without.
- [x] `uke05-agentisk-ai/03_crewai_fordypning_rehabilitering.ipynb` - requires `GOOGLE_API_KEY` or `GEMINI_API_KEY`; installs `crewai` if missing.

## Utility

- [x] `utils/imgur-opplasting.ipynb` - helper notebook, not a primary course notebook; may still require local path adaptation.

## Maintenance Notes

- [x] Add a consistent Colab contract and bootstrap cell to every notebook.
- [x] Standardize secrets pattern: Colab Secrets via `userdata.get(...)`; environment variables / `.env` locally.
- [x] Standardize package installation pattern: only notebook-specific packages are installed in Colab.
- [x] Mark API/data/GPU requirements at the top of every notebook.
- [x] Clear outputs that contained local machine paths.
- [ ] Run every notebook end-to-end in a fresh Colab runtime.
- [ ] For heavy data notebooks, decide whether to add small downloadable teaching fixtures to reduce manual setup.
- [ ] Keep this checklist in sync when adding or substantially refactoring notebooks.
