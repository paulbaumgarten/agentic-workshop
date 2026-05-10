FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    curl \
    git \
    build-essential \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install OpenCode as root and move binary system-wide
RUN curl -fsSL https://opencode.ai/install | bash && \
    mv /root/.opencode/bin/opencode /usr/local/bin/opencode && \
    chmod +x /usr/local/bin/opencode

# Set working directory
WORKDIR /workspace

# Install Python dependencies globally
RUN pip install --no-cache-dir \
    flask \
    psycopg2-binary \
    sqlalchemy \
    python-dotenv

CMD ["sleep", "infinity"]
