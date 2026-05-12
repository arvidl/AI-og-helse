# Verktøy og praktiske guider

Denne siden er en kort støtte til lokal kjøring, Colab-kjøring og trygg bruk av generative AI-verktøy i kurset.

## API-nøkler

Flere uke04-notebooks kan kjøres uten API-nøkler, men live-demonstrasjoner blir rikere med en eller flere av disse:

- `GEMINI_API_KEY` eller `GOOGLE_API_KEY` for Google Gemini
- `OPENAI_API_KEY` for OpenAI/GPT
- `ANTHROPIC_API_KEY` eller `CLAUDE_API_KEY` for Anthropic/Claude

Lokalt kan nøklene ligge i en `.env`-fil:

```text
GEMINI_API_KEY=...
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
```

I Google Colab legges nøklene inn via **Secrets** i venstremenyen. Del aldri nøklene i notebook-output, skjermbilder eller commits.

## Prompt-sjekkliste for helse

En god helsefaglig prompt bør vanligvis angi:

1. **Rolle og oppgave:** hva modellen skal hjelpe med.
2. **Målgruppe:** pasient, helsepersonell, leder, student eller utvikler.
3. **Kontekst:** relevant, anonymisert informasjon.
4. **Avgrensning:** hva modellen ikke skal gjøre.
5. **Svarformat:** punktliste, tabell, SOAP, JSON eller kort tekst.
6. **Usikkerhet:** be modellen skille fakta, antakelser og manglende informasjon.
7. **Sikkerhet:** be om eskalering til helsepersonell ved røde flagg.

## Strukturert output

Når et svar skal brukes videre i kode eller dokumentasjon, er strukturert output tryggere enn fri tekst. Be for eksempel om:

```json
{
  "sammendrag": "...",
  "usikkerhet": ["..."],
  "mangler": ["..."],
  "anbefalt_menneskelig_kontroll": true
}
```

Valider alltid formatet i vanlig kode før du bruker innholdet videre.

## Modellvalg og fallback

Modellnavn, kvoter og tilgang endres raskt. For undervisning er det nyttig å:

- støtte minst én rimelig/gratis modell der det er mulig
- ha demo-modus når API ikke er tilgjengelig
- logge modellnavn og tidspunkt for kjøring
- sammenligne svar fra flere modeller når poenget er modellforskjeller

## Fra uke04 til uke05

Uke04 handler mest om prompts og API-kall. Uke05 bygger videre med agentiske mønstre:

- **Tool calling:** modellen foreslår et verktøykall, mens kode utfører handlingen.
- **RAG:** relevante dokumentbiter hentes først og gis som kontekst.
- **Logging og evaluering:** prompt, svar, modellnavn og vurdering lagres slik at systemet kan etterprøves.

I helse bør slike mønstre alltid kombineres med personvern, tilgangsstyring, validering og menneskelig kontroll.

## Minimumslogg for agentiske demoer

For undervisningsdemoer er en enkel logg ofte nok. For mer praksisnære systemer må logging vurderes sammen med personvern og tilgangsstyring.

En pedagogisk minimumslogg kan inneholde:

```json
{
  "oppgave": "kort beskrivelse",
  "modell": "modellnavn",
  "verktøy": ["kunnskapsoppslag"],
  "kontekst_kilde": ["syntetisk prosedyre eller lokal demo-kilde"],
  "menneskelig_kontroll": "påkrevd før klinisk bruk",
  "evaluering": {
    "format_ok": true,
    "mangler_kjent": ["ikke validert klinisk"],
    "risikonivå": "lav/moderat/høy"
  }
}
```

Ikke logg identifiserbare pasientopplysninger i åpne demoer.

## Agentisk AI: enkel sikkerhetssjekk

Før et agentisk system brukes utenfor undervisning, bør minst disse spørsmålene være besvart:

1. Hva får systemet lov til å gjøre selv?
2. Hvilke verktøy kan det bruke?
3. Hvilke data får det lese?
4. Hvordan stoppes feil verktøyvalg eller feil kontekst?
5. Hva logges, og hvem kan se loggen?
6. Hvem godkjenner forslag før de påvirker pasient, dokumentasjon eller prioritering?
