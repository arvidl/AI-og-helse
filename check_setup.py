#!/usr/bin/env python3
"""
Verifiseringsscript for AI og Helse kurset
Sjekker at standardmiljøet er installert og gir et raskt bilde av
valgfrie pakker som brukes i enkelte notebooks.
"""

from importlib import import_module
from importlib.metadata import PackageNotFoundError, version
import sys
import warnings
warnings.filterwarnings('ignore')

def check_package(package_name, import_name=None):
    """Sjekk om en pakke er installert og kan importeres."""
    if import_name is None:
        import_name = package_name

    try:
        import_module(import_name)
        try:
            pkg_version = version(package_name)
            return True, f"✅ {package_name} ({pkg_version})"
        except PackageNotFoundError:
            return True, f"✅ {package_name}"
    except ImportError:
        return False, f"❌ {package_name} - Installer med: pip install {package_name}"

def check_api_keys():
    """Sjekk om API-nøkler er konfigurert."""
    import os
    from dotenv import load_dotenv

    load_dotenv()

    results = []

    # Sjekk OpenAI
    if os.getenv("OPENAI_API_KEY"):
        results.append("✅ OpenAI API key funnet")
    else:
        results.append("⚠️  OpenAI API key ikke funnet (trengs for ChatGPT)")

    # Sjekk Anthropic
    if os.getenv("ANTHROPIC_API_KEY"):
        results.append("✅ Anthropic API key funnet")
    else:
        results.append("⚠️  Anthropic API key ikke funnet (trengs for Claude)")

    # Sjekk Gemini / Google
    if os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY"):
        results.append("✅ Google/Gemini API key funnet")
    else:
        results.append("⚠️  Google/Gemini API key ikke funnet (trengs for Gemini)")

    return results

def print_section(title):
    print(title)
    print("-" * len(title))

def run_checks(packages):
    all_ok = True
    for package, import_name in packages:
        ok, msg = check_package(package, import_name)
        print(msg)
        if not ok:
            all_ok = False
    return all_ok

def main():
    print("=" * 50)
    print("🏥 AI og Helse - Miljøsjekk")
    print("=" * 50)
    print()

    core_packages = [
        ("numpy", None),
        ("pandas", None),
        ("scipy", None),
        ("matplotlib", None),
        ("seaborn", None),
        ("scikit-learn", "sklearn"),
        ("torch", None),
        ("torchvision", None),
        ("opencv-python", "cv2"),
        ("pillow", "PIL"),
        ("notebook", None),
        ("ipywidgets", None),
        ("python-dotenv", "dotenv"),
        ("google-genai", "google.genai"),
        ("transformers", None),
        ("tiktoken", None),
        ("openai", None),
        ("anthropic", None),
    ]

    notebook_specific_packages = [
        ("shap", None),
        ("lime", None),
        ("faker", None),
        ("nibabel", None),
        ("nilearn", None),
        ("wfdb", None),
        ("crewai", None),
        ("torchinfo", None),
        ("torchsummary", None),
        ("kaggle", None),
    ]

    print_section("📦 Sjekker kjernepakker")
    all_ok = run_checks(core_packages)

    print()
    print_section("🧪 Sjekker pakker for utvalgte notebooks")
    optional_ok = run_checks(notebook_specific_packages)

    print()
    print_section("🔑 Sjekker API-nøkler")
    for msg in check_api_keys():
        print(msg)

    print()
    print("=" * 50)

    if all_ok:
        print("✅ Alt ser bra ut! Du er klar til å starte kurset.")
        print("📚 Åpne 'uke01-introduksjon/README.md' for å begynne.")
    else:
        print("⚠️  Én eller flere kjernepakker mangler.")
        print("Anbefalt: conda env create -f environment.yml")
        print("Alternativt: pip install -r requirements.txt")

    if not optional_ok:
        print("ℹ️  Noen valgfrie pakker mangler.")
        print("Det er vanlig hvis du ikke trenger alle fordypningsnotebooks.")

    print("=" * 50)

    print("\n📓 Tester notebook-miljø...")
    try:
        import notebook
        import ipywidgets
        print("✅ Notebook og ipywidgets er installert og klare")
        print("   Start med: jupyter lab")
    except Exception:
        print("❌ Notebook-miljøet er ikke komplett")

    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
