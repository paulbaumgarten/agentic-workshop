FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    curl \
    git \
    build-essential

# Install Node (required for OpenCode CLI if npm-based)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

# Install OpenCode CLI globally
RUN npm install -g opencode-cli

# Set working directory
WORKDIR /workspace

# Install common Python packages globally
RUN pip install --no-cache-dir \
    flask \
    psycopg2-binary \
    sqlalchemy \
    python-dotenv

CMD ["sleep", "infinity"]
