#!/bin/bash
set -e

echo "🚀 Setting up AI og Helse environment for Codespaces..."

# Detect if we're in Codespaces or local
if [ -n "$CODESPACES" ]; then
    echo "📍 Running in GitHub Codespaces (Linux)"
    ENV_FILE="environment-codespaces.yml"
else
    echo "📍 Running locally"
    ENV_FILE="environment.yml"
fi

# Use environment-codespaces.yml if it exists, otherwise fall back to environment.yml
if [ ! -f "$ENV_FILE" ] && [ -f "environment.yml" ]; then
    ENV_FILE="environment.yml"
    echo "⚠️ Using environment.yml (may need adjustments for Linux)"
fi

# Update conda/mamba
echo "📦 Updating conda..."
conda update -n base -c defaults conda -y

# Try to use mamba for faster solving (if available)
if command -v mamba &> /dev/null; then
    CONDA_CMD="mamba"
    echo "🚀 Using mamba for faster environment creation"
else
    CONDA_CMD="conda"
    echo "📦 Using conda (consider installing mamba for faster setup)"
fi

# Create environment
echo "🔧 Creating conda environment from $ENV_FILE..."
$CONDA_CMD env create -f $ENV_FILE --force || {
    echo "⚠️ Some packages failed to install, trying with relaxed constraints..."
    # Create a basic environment first
    conda create -n ai-helse python=3.12 -y
    conda activate ai-helse
    # Install what we can from conda
    conda install -c conda-forge -c defaults -y \
        numpy pandas matplotlib seaborn plotly \
        scikit-learn jupyter jupyterlab ipykernel \
        python-dotenv pyyaml tqdm || true
    # Install the rest with pip
    pip install -r requirements.txt || true
}

# Activate environment
source /opt/conda/etc/profile.d/conda.sh
conda activate ai-helse

# Install Jupyter kernel
echo "📓 Installing Jupyter kernel..."
python -m ipykernel install --user --name ai-helse --display-name "Python 3.12 (AI-Helse)"

# Verify critical packages
echo "🔍 Verifying installation..."
python -c "
import sys
print(f'Python: {sys.version}')
try:
    import numpy
    print(f'✅ NumPy: {numpy.__version__}')
except: print('❌ NumPy not installed')
try:
    import pandas
    print(f'✅ Pandas: {pandas.__version__}')
except: print('❌ Pandas not installed')
try:
    import sklearn
    print(f'✅ Scikit-learn: {sklearn.__version__}')
except: print('❌ Scikit-learn not installed')
try:
    import torch
    print(f'✅ PyTorch: {torch.__version__}')
except: print('⚠️ PyTorch not installed (optional)')
try:
    import openai
    print(f'✅ OpenAI: {openai.__version__}')
except: print('❌ OpenAI not installed')
"

# Set up activation for new terminals
echo "conda activate ai-helse" >> ~/.bashrc

echo "✅ Setup complete!"
echo "🎉 Environment 'ai-helse' is ready to use"
echo ""
echo "To start Jupyter Lab, run: jupyter lab"
