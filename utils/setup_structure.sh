#!/bin/bash
# Kjør dette scriptet for å opprette mappestrukturen
# bash setup_structure.sh

echo "📁 Oppretter mappestruktur for AI og Helse kurset..."

# Hovedmapper for hver uke - bruk array for å få riktig formatering
echo "📂 Oppretter nye ukemapper med riktige navn..."

# Definer ukene som array
declare -a uker=(
    "01:introduksjon"
    "02:klassisk-ml"
    "03:dyplæring"
    "04:generativ-ai"
    "05:agentisk-ai"
    "06:klinisk-praksis"
    "07:velferdsteknologi"
    "08:etikk-implementering"
)

# Iterer gjennom array
for uke in "${uker[@]}"; do
    nummer="${uke%%:*}"
    navn="${uke##*:}"
    
    echo "  Oppretter uke$nummer-$navn"
    mkdir -p "uke$nummer-$navn"

    # Opprett README for hver uke
    tittel=$(echo $navn | sed 's/-/ /g' | sed 's/\b\(.\)/\u\1/g')
    echo "# Uke $nummer: $tittel" > "uke$nummer-$navn/README.md"
    echo "" >> "uke$nummer-$navn/README.md"
    echo "## Læringsmål" >> "uke$nummer-$navn/README.md"
    echo "" >> "uke$nummer-$navn/README.md"
    echo "## Innhold" >> "uke$nummer-$navn/README.md"
    echo "" >> "uke$nummer-$navn/README.md"
    echo "## Oppgaver" >> "uke$nummer-$navn/README.md"
done

# Andre mapper
echo "📁 Oppretter øvrige mapper..."
mkdir -p .devcontainer
mkdir -p utils
mkdir -p ressurser/artikler
mkdir -p ressurser/verktoy

