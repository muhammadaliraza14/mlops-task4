# Step 1: Selecting base python environment
FROM python:3.8-slim AS base

# Set the working directory in the container
WORKDIR /app

# Step 2: Creating directory and copying all content from repo into the created directory
COPY . /app

# Step 3: Installation of packages
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Final stage
FROM base AS final

# Expose port 80 for Flask app
EXPOSE 80

# Set environment variables
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
