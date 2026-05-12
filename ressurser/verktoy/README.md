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

## Fra uke05 til uke06

Uke05 viser at et system kan hente kontekst, bruke verktøy og foreslå neste steg. Uke06 spør hva som må være dokumentert før dette kan ligne klinisk praksis:

1. **Validering:** er systemet testet på relevante data, brukere og settinger?
2. **Kalibrering:** betyr risikoanslaget det det ser ut til å bety?
3. **Terskler:** når skal systemet anbefale handling, avventing eller eskalering?
4. **Subgrupper:** fungerer systemet rimelig likt for viktige pasientgrupper og tjenestekontekster?
5. **Arbeidsflyt:** kommer anbefalingen på et tidspunkt der en person faktisk kan handle?
6. **Monitorering:** oppdages datadrift, feil, avvik og endret ytelse etter innføring?
7. **Menneskelig kontroll:** hvem kan godkjenne, overstyre, stoppe eller rapportere systemet?

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

## Klinisk modenhetssjekk

Før en AI-løsning omtales som klinisk beslutningsstøtte, bør prosjektet minst kunne svare kort på:

1. Hvilken beslutning, prioritering eller dokumentasjonsoppgave støttes?
2. Hvilken menneskelig rolle har siste ord?
3. Hvilke data er brukt til utvikling, intern validering og ekstern validering?
4. Hvilke måltall følges: diskriminering, kalibrering, sensitivitet, spesifisitet, nytte og subgruppeytelse?
5. Hvilke terskler brukes, og hvilken handling utløser hver terskel?
6. Hvordan håndteres usikkerhet, manglende data og teknisk nedetid?
7. Hvordan logges bruk, feil og avvik uten å eksponere pasientopplysninger unødvendig?
8. Når skal systemet re-valideres, pauses eller trekkes tilbake?

## Velferdsteknologi: tjenestesjekk

For sensorer, varsling, robotikk og beslutningsstøtte i hjem/omsorg bør en teknisk demo ikke forveksles med en tjeneste. Minst disse punktene bør avklares:

1. **Bruker og formål:** hvem skal teknologien hjelpe, og med hvilket konkret problem?
2. **Autonomi og samtykke:** kan brukeren forstå, påvirke, reservere seg eller overstyre?
3. **Falske alarmer:** hvor mange unødige varsler tåler bruker, pårørende og tjeneste?
4. **Manglende alarmer:** hvilke hendelser er mest kritiske å ikke overse?
5. **Arbeidsflyt:** hvem mottar varsel, hvor raskt, og hva er forventet handling?
6. **Ansvar:** hvem eier oppfølging, feilretting, opplæring og avvikshåndtering?
7. **Monitorering:** hvilke signaler viser at systemet fungerer dårligere over tid?
8. **Personvern:** hvilke data samles inn i hjemmet, hvor lenge lagres de, og hvem har tilgang?

## Ansvarlig implementering: sluttsjekk

Uke08 samler kursets tekniske og kliniske spor. Før et AI-system flyttes fra demo, pilot eller forskningsprosjekt til reell bruk, bør teamet minst kunne dokumentere:

1. **Formål og avgrensning:** hva systemet skal gjøre, og hva det ikke skal brukes til.
2. **Personvern:** rettslig grunnlag, dataminimering, informasjonsplikt, tilgangsstyring og eventuell DPIA.
3. **Samtykke og autonomi:** når samtykke er relevant, og hvordan pasient/bruker kan informeres, reservere seg eller be om menneskelig vurdering.
4. **Bias og rettferdighet:** hvilke grupper som er undersøkt, hvilke forskjeller som finnes, og hvilke tiltak som er valgt.
5. **Regulering:** om systemet kan være medisinsk utstyr, SaMD eller høyrisiko-AI, og hvilken dokumentasjon som kreves.
6. **Menneskelig kontroll:** hvem har siste ord, hvem kan overstyre, og hvem følger opp feil.
7. **Monitorering:** hvilke ytelses-, sikkerhets-, fairness- og driftsmål følges etter innføring.
8. **Stoppregel:** når skal systemet pauses, endres, re-valideres eller trekkes tilbake.
