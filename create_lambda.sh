#!/bin/bash
set -e

# Get Virtualenv Directory Path
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
if [ -z "$VIRTUAL_ENV_DIR" ]; then
    VIRTUAL_ENV_DIR="$SCRIPT_DIR/venv"
fi

echo "Using virtualenv located in : $VIRTUAL_ENV_DIR"
echo "Script directory: $SCRIPT_DIR"
echo "Creating zip using python file: $1"

# Create backup of zip if it exists
if [ -f $SCRIPT_DIR/$1.zip ]; then
    mv $SCRIPT_DIR/$1.zip $SCRIPT_DIR/$1.zip.backup
fi

# Add virtualenv libs in new zip file
cd $VIRTUAL_ENV_DIR/lib/python3.8/site-packages
zip -r9 $SCRIPT_DIR/$1.zip *
cd $SCRIPT_DIR/lambdas

# Add python code in zip file
zip -r9 $SCRIPT_DIR/$1.zip $1.py
