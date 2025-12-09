FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy ONLY the aurum package
COPY aurum/ ./aurum/

# Ensure instance folder exists
RUN mkdir -p aurum/instance

# Flask env
ENV FLASK_APP=aurum.app:create_app
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["sh", "-c", "python -m aurum.init_db && flask run"]
