#!/bin/bash
set -e

# Get Virtualenv Directory Path
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
if [ -z "$VIRTUAL_ENV_DIR" ]; then
    VIRTUAL_ENV_DIR="$SCRIPT_DIR/venv"
fi

echo "Using virtualenv located in : $VIRTUAL_ENV_DIR"
echo "Script directory: $SCRIPT_DIR"

# Create backup of zip if it exists
if [ -f $SCRIPT_DIR/lambda_test.zip ]; then
    mv $SCRIPT_DIR/lambda_test.zip $SCRIPT_DIR/lambda_test.zip.backup
fi

# Add virtualenv libs in new zip file
cd $VIRTUAL_ENV_DIR/lib/python3.8/site-packages
zip -r9 $SCRIPT_DIR/lambda_test.zip *
cd $SCRIPT_DIR/lambdas

# Add python code in zip file
zip -r9 $SCRIPT_DIR/lambda_test.zip lambda_test.py

# Run terraform apply
# terraform apply
