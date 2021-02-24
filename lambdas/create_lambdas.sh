#!/bin/bash
set -e

# Get Virtualenv Directory Path
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
mkdir -p output
if [ -z "$VIRTUAL_ENV_DIR" ]; then
    VIRTUAL_ENV_DIR="$SCRIPT_DIR/venv"
fi

echo "Using virtualenv located in : $VIRTUAL_ENV_DIR"
echo "Running script from directory: $SCRIPT_DIR"

# Add virtualenv libs in lambda zip files
pushd $VIRTUAL_ENV_DIR/lib/python3.8/site-packages
zip -rq9 $SCRIPT_DIR/output/confirmation_handler.zip *
zip -rq9 $SCRIPT_DIR/output/leaderboard_handler.zip *
zip -rq9 $SCRIPT_DIR/output/location_handler.zip *
zip -rq9 $SCRIPT_DIR/output/qwest_handler.zip *
zip -rq9 $SCRIPT_DIR/output/user_handler.zip *
popd

# Add subdirectories and lambda handlers to zip files
pushd $SCRIPT_DIR/src/
zip -rq9 $SCRIPT_DIR/output/confirmation_handler.zip utils
zip -r9 $SCRIPT_DIR/output/confirmation_handler.zip confirmation_handler.py

zip -rq9 $SCRIPT_DIR/output/leaderboard_handler.zip utils
zip -r9 $SCRIPT_DIR/output/leaderboard_handler.zip leaderboard_handler.py

zip -rq9 $SCRIPT_DIR/output/location_handler.zip utils
zip -r9 $SCRIPT_DIR/output/location_handler.zip location_handler.py

zip -rq9 $SCRIPT_DIR/output/qwest_handler.zip utils
zip -r9 $SCRIPT_DIR/output/qwest_handler.zip qwest_handler.py

zip -rq9 $SCRIPT_DIR/output/user_handler.zip utils
zip -rq9 $SCRIPT_DIR/output/user_handler.zip user_handler.py
popd

