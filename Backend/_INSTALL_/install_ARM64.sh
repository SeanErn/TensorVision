#!/bin/bash
echo "[INSTALL] Starting install..."
echo "[TFOD] Installing python dependencies..."
pip install --no-index --find-links pip/ -r Backend/TensorFlow/install/dependencies/pip/requirements.txt
echo "[TFOD] Done!"

echo "[TFOD] Installing apt dependencies..."
sudo apt-get install Backend/TensorFlow/install/dependencies/apt/*
echo "[TFOD] Done!"

echo "[MONGO] Installing MongoDB..."
./Backend/MongoDB/Install/install.sh

echo "[MONGO] Setting up database..."
python Backend/MongoDB/Install/setupDB.py
echo "[MONGO] Done!"

echo "[INSTALL] Install finished!"