#!/bin/bash

# MUST BE RAN FROM PROJECT ROOT
echo "[INSTALL] Starting install..."
echo "[TFOD] Installing python dependencies..."
${PWD}/Backend/TensorFlow/install/install_python.sh

echo "[TFOD] Running install script for Tensorflow..."
python3 ${PWD}/Backend/TensorFlow/install/install.py
echo "[TFOD] Done!"

echo "[TFOD] Installing apt dependencies..."
sudo apt-get install -y ${PWD}/Backend/TensorFlow/install/dependencies/apt/*
echo "[TFOD] Done!"

echo "[MONGO] Installing MongoDB..."
${PWD}/Backend/MongoDB/Install/install.sh -x86

echo "[MONGO] Setting up database..."
python3 ${PWD}/Backend/MongoDB/Install/setupDB.py
echo "[MONGO] Done!"

echo "[INSTALL] Install finished!"