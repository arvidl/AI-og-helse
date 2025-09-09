#!/bin/bash
# Kjør dette scriptet for å opprette mappestrukturen
# bash setup_structure.sh

echo "📁 Oppretter mappestruktur for AI og Helse kurset..."

# Hovedmapper for hver uke
for i in {01..10}; do
    case $i in
        01) navn="introduksjon" ;;
        02) navn="klassisk-ml" ;;
        03) navn="dyp-laering" ;;
        04) navn="generativ-ai" ;;
        05) navn="multimodal-ai" ;;
        06) navn="klinisk-praksis" ;;
        07) navn="velferdsteknologi" ;;
        08) navn="etikk-implementering" ;;
        09) navn="fysisk-samling" ;;
        10) navn="eksamen" ;;
    esac

    mkdir -p "uke$i-$navn"
    mkdir -p "uke$i-$navn/oppgaver"
    mkdir -p "uke$i-$navn/ressurser"

    # Opprett README for hver uke
    echo "# Uke $i: $(echo $navn | sed 's/-/ /g' | sed 's/\b\(.\)/\u\1/g')" > "uke$i-$navn/README.md"
    echo "" >> "uke$i-$navn/README.md"
    echo "## Læringsmål" >> "uke$i-$navn/README.md"
    echo "" >> "uke$i-$navn/README.md"
    echo "## Innhold" >> "uke$i-$navn/README.md"
    echo "" >> "uke$i-$navn/README.md"
    echo "## Oppgaver" >> "uke$i-$navn/README.md"
done

# Andre mapper
mkdir -p .devcontainer
mkdir -p prosjekt/eksempler
mkdir -p prosjekt/maler
mkdir -p utils
mkdir -p data/synthetic
mkdir -p data/samples
mkdir -p ressurser/artikler
mkdir -p ressurser/videoer
mkdir -p ressurser/verktoy

echo "✅ Mappestruktur opprettet!"
