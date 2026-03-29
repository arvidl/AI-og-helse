# Colab Compatibility Checklist

This is a repo-based compatibility snapshot for the notebooks in `AI-og-helse`.

It is intended as a practical maintenance checklist, not a guarantee that every notebook has been fully test-run in Google Colab. Some notebooks may still require API keys, Google Drive mounting, uploaded data, downloaded datasets, or GPU runtime selection.

## Clearly Colab-Ready

- [ ] `uke01-introduksjon/00-velkommen.ipynb`
- [ ] `uke01-introduksjon/01-test-meg.ipynb`
- [ ] `uke01-introduksjon/02-hva-er-ai.ipynb`
- [ ] `uke01-introduksjon/03-ai-historie-helse.ipynb`
- [ ] `uke01-introduksjon/04-ai-ml-dl-forskjeller.ipynb`
- [ ] `uke01-introduksjon/05-regelbaserte-systemer.ipynb`
- [ ] `uke02-klassisk-ml/01-klassisk-ml-101.ipynb`
- [ ] `uke02-klassisk-ml/02-fra-symptom-til-diagnose.ipynb`
- [ ] `uke03-dyplæring/01a_nn_intro.ipynb`
- [ ] `uke03-dyplæring/01b_læring_i_nn.ipynb`
- [ ] `uke03-dyplæring/02d_cnn_konklusjon.ipynb`
- [ ] `uke04-generativ-ai/01_transformer_arkitektur.ipynb`
- [ ] `uke04-generativ-ai/02_llm_grunnleggende.ipynb`
- [ ] `uke04-generativ-ai/03_prompt_engineering.ipynb`
- [ ] `uke06-klinisk-praksis/01_risikomodell_logistisk_regresjon_kalibrering_shap.ipynb`
- [ ] `uke07-velferdsteknologi/01_robotnavigasjon_i_rutenett_med_astar.ipynb`
- [ ] `uke08-etikk-implementering/01_gdpr_personvern.ipynb`
- [ ] `uke08-etikk-implementering/02_bias_rettferdighet.ipynb`
- [ ] `uke08-etikk-implementering/03_ce_mdr_regulering.ipynb`

## Colab-Capable With Manual Setup

- [ ] `uke01-introduksjon/99-oppsett-miljø.ipynb`
  Note: environment-setup notebook; opens in Colab, but is not naturally Colab-first.
- [ ] `uke03-dyplæring/01c_UCI_heart_disease_klassifikasjon.ipynb`
  Note: likely needs manual data/file handling.
- [ ] `uke03-dyplæring/01d_EKG_arytmi_klassifikasjon.ipynb`
  Note: depends on external PhysioNet data.
- [ ] `uke03-dyplæring/02a_cnn_bildeklassifikasjon.ipynb`
  Note: uses uploads and references Kaggle-style data flow.
- [ ] `uke03-dyplæring/02b_cnn_trening.ipynb`
  Note: likely needs prepared data, prior outputs, and often GPU runtime.
- [ ] `uke03-dyplæring/02c_cnn_testing.ipynb`
  Note: depends on trained model artifacts from earlier steps.
- [ ] `uke03-dyplæring/03_medisinsk_bildeklassifikasjon_MR.ipynb`
  Note: likely needs heavier data preparation and runtime care.
- [ ] `uke03-dyplæring/04a_ansiktsutrykk_klassifikasjon.ipynb`
  Note: part of a multi-step workflow.
- [ ] `uke03-dyplæring/04b_ansiktsutrykk_klassifikasjon.ipynb`
  Note: references Google Drive paths and saved model files.
- [ ] `uke03-dyplæring/04c_ansiktsutrykk_klassifikasjon.ipynb`
  Note: references Google Drive paths and saved model files.
- [ ] `uke04-generativ-ai/04_chatgpt_claude_api.ipynb`
  Note: requires API keys.
- [ ] `uke04-generativ-ai/oppgaver/prompt_workshop.ipynb`
  Note: can run in simulated mode, but real use needs `OPENAI_API_KEY`.
- [ ] `uke05-multimodal-ai/01_bilde_tekst_clip_zero_shot_blomster.ipynb`
  Note: likely needs heavier model/runtime setup than the simpler notebooks.
- [ ] `intro_openai_anthropic.ipynb`
  Note: Colab-aware, but requires manual secret setup.

## Local-Only Or Needs Cleanup

- [ ] `utils/imgur-opplasting.ipynb`
  Note: uses a hardcoded local path under `~/GitHub/AI-og-helse/...` and behaves like a local utility notebook.

## Maintenance Notes

- [ ] Revisit the 14 manual-setup notebooks and decide whether each should become fully Colab-ready.
- [ ] Remove hardcoded local paths where possible.
- [ ] Standardize secret handling for API-based notebooks using one documented Colab pattern.
- [ ] Standardize data-loading patterns for notebooks that currently assume local files, uploaded files, or prior training artifacts.
- [ ] Keep this checklist in sync when adding or substantially refactoring notebooks.
