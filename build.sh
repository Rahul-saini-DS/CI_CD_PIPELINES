#!/bin/bash

# "set -e" tells the script to stop immediately if any command fails
set -e

echo "--- STARTING BUILD SCRIPT ---"

echo "1. Setting up Backend..."
# We check if pip is available, then install requirements
if [ -f api/requirements.txt ]; then
    pip install -r api/requirements.txt
else
    echo "Warning: No api/requirements.txt found."
fi

echo "2. Setting up Frontend..."
# Install Node dependencies
npm install

echo "3. Building React App..."
# Build the production version of the frontend
npm run build

echo "--- BUILD SUCCESSFUL ---"
