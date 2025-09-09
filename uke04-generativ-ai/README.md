# Uke 4: Generativ AI og Store Språkmodeller (AI 2.0)

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
   - Se: [Visualisering av Transformers](https://www.youtube.com/watch?v=...)
   - Øv: Prompt-oppgaver i `prompts/`

## 🏃 Hurtigstart

```python
# Test at alt fungerer
from transformers import pipeline

# Last inn norsk språkmodell
generator = pipeline("text-generation", model="NbAiLab/nb-gpt-j-6B")

# Generer tekst
prompt = "Pasienten presenterer symptomer på"
result = generator(prompt, max_length=50)
print(result[0]['generated_text'])
```

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
- [Anthropic Claude Best Practices](https://docs.anthropic.com/claude/docs)
- [Prompts for Healthcare](prompts/)

## ❓ Ofte stilte spørsmål

**Q: Trenger jeg API-nøkler?**
A: Nei, disse er inkludert i kurset via miljøvariabler.

**Q: Kan jeg bruke norsk i prompts?**
A: Ja! Moderne LLM håndterer norsk godt.

## 📅 Veiledning

- **Tirsdag kl 14-16:** Live gjennomgang (Teams)
- **Torsdag kl 10-11:** Spørretimen (frivillig)

---

*Neste uke: [Multimodal AI og moderne arkitekturer →](../uke05-multimodal-ai/)*
