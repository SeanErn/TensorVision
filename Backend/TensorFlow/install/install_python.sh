#!/bin/bash

# Check if pyenv is installed
if ! command -v pyenv &> /dev/null
then
    # Install dependencies for pyenv
    sudo apt-get update
    echo "[APT] Installing pienv requirements..."
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev openssl git
    echo "[APT] Done!"
    echo "[APT] Installing Tensorflow requirements..."
    sudo apt-get install -y protobuf-compiler
    echo "[APT] Done!"

    # Install pyenv if not allready installed
    curl https://pyenv.run | bash

    # Add pyenv to bash so commands are available
    echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

    # Restart your shell so the path changes take effect
    exec "$SHELL"
    echo "[PIENV] Installed pienv"
else
    echo "[PIENV] pienv allready installed. Skipping..."
fi

# Check if Python 3.7.16 is installed
if ! pyenv versions --bare | grep -q '^3.7.16$'
then
    # Install Python 3.7
    pyenv install 3.7.16
else
    echo "[PIENV] Python 3.7.16 allready installed. Skipping..."
fi

# Set Python 3.7 as the global version
pyenv global 3.7.16
echo "[PIENV] Set Python to 3.7.16"

# Install pip packages
echo "[PIP] Installing dependencies from requirements.txt..."
pip install -r ${PWD}/Backend/TensorFlow/install/dependencies/pip/requirements.txt
echo "[PIP] Done!"

