# Setup virtual environment and install dependencies
setup:
    python -m venv .venv
    . .venv/bin/activate && pip install --upgrade pip
    . .venv/bin/activate && pip install -r requirements.txt

# Train the machine learning model
train:
    python iris_dataset.py

# Run the Flask app
run:
    . .venv/bin/activate && python app.py

# Clean up
clean:
    rm -rf .venv
