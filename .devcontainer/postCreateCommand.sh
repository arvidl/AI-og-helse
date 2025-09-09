#!/bin/bash
#
# .devcontainer/postCreateCommand.sh
#
echo "🏥 Setter opp AI og Helse miljø..."

# Oppgrader pip
pip install --upgrade pip

# Installer requirements
pip install -r requirements.txt

# Konfigurer Jupyter
jupyter nbextension enable --py widgetsnbextension

# Last ned eksempeldata
python -m utils.download_sample_data

# Kjør tester
python -m pytest tests/ -v

# Sett opp pre-commit hooks
pre-commit install

echo "✅ Miljøet er klart! Velkommen til AI og Helse kurset!"
echo "📚 Start med å åpne README.md for å komme i gang"
