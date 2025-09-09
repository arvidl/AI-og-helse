#!/usr/bin/env python3
"""
Verifiseringsscript for AI og Helse kurset
Sjekker at alle nødvendige pakker er installert og fungerer
"""

import sys
import warnings
warnings.filterwarnings('ignore')

def check_package(package_name, import_name=None):
    """Sjekk om en pakke er installert og kan importeres"""
    if import_name is None:
        import_name = package_name

    try:
        __import__(import_name)
        return True, f"✅ {package_name}"
    except ImportError:
        return False, f"❌ {package_name} - Installer med: pip install {package_name}"

def check_api_keys():
    """Sjekk om API-nøkler er konfigurert"""
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

    return results

def main():
    print("=" * 50)
    print("🏥 AI og Helse - Miljøsjekk")
    print("=" * 50)
    print()

    # Liste over pakker å sjekke
    packages = [
        ("numpy", None),
        ("pandas", None),
        ("scikit-learn", "sklearn"),
        ("torch", None),
        ("transformers", None),
        ("langchain", None),
        ("openai", None),
        ("anthropic", None),
        ("streamlit", None),
        ("jupyter", None),
        ("autogen", None),
    ]

    print("📦 Sjekker installerte pakker:")
    print("-" * 30)

    all_ok = True
    for package, import_name in packages:
        ok, msg = check_package(package, import_name)
        print(msg)
        if not ok:
            all_ok = False

    print()
    print("🔑 Sjekker API-nøkler:")
    print("-" * 30)
    for msg in check_api_keys():
        print(msg)

    print()
    print("=" * 50)

    if all_ok:
        print("✅ Alt ser bra ut! Du er klar til å starte kurset.")
        print("📚 Åpne 'uke01-introduksjon/README.md' for å begynne.")
    else:
        print("⚠️  Noen pakker mangler.")
        print("Kjør: pip install -r requirements.txt")

    print("=" * 50)

    # Test Jupyter
    print("\n📓 Tester Jupyter Notebook...")
    try:
        import notebook
        import jupyter
        print("✅ Jupyter er installert og klar")
        print("   Start med: jupyter notebook")
    except:
        print("❌ Jupyter ikke installert")

    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
