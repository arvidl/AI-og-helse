import json
import nbformat

# Last inn json-data (fra fil som er formatert som en notebook)
with open("input.json", "r", encoding="utf-8") as f:
    notebook_json = json.load(f)

# Lag Jupyter notebook-objekt
nb = nbformat.from_dict(notebook_json)

# Lagre som .ipynb
with open("output.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)
