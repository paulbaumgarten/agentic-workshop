FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    curl \
    git \
    build-essential \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install OpenCode via official installer
RUN curl -fsSL https://opencode.ai/install | bash

# Add OpenCode to PATH
ENV PATH="/root/.opencode/bin:${PATH}"

# Set working directory
WORKDIR /workspace

# Install Python dependencies globally
RUN pip install --no-cache-dir \
    flask \
    psycopg2-binary \
    sqlalchemy \
    python-dotenv

CMD ["sleep", "infinity"]
