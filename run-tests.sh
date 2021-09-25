#!/bin/bash
# Main script to run tests

echo "Loading environment"
source environment-setup.sh

echo "Loading Python"
source venv/bin/activate

echo "Running unittest:"
echo "Checking if your environment looks good"
python -m unittest -v tests/integration-toolkit/test-environment.py
