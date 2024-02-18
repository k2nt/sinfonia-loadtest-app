# Stage 1: Build stage
FROM python:3.11-slim as base

# PYTHONDONTWRITEBYTECODE: Disable building .pyc files
# PYTHONFAULTHANDLER: Enable traceback on errors
# PYTHONHASHSEED: Seed value for random hashes
# PYTHONUNBUFFERED: Enable unbuffered mode when writing to terminal
ENV PYTHONDONTWRITEBYTECODE=1 \  
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

# Update apt-get and install kubectl
RUN apt-get update && apt-get install --no-install-recommends -y curl git \
 && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
 && curl -LO "https://dl.k8s.io/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl" \
 && chmod +x kubectl && mv kubectl /usr/local/bin/kubectl

# PIP_DEFAULT_TIMEOUT: Cancels pip jobs running longer that specified value [unit: seconds]
# PIP_DISABLE_PIP_VERSION_CHECK: Disable pip version check
# PIP_NO_CACHE_DIR: Disable pip caching
# POETRY_VERSION: Poetry version
# POETRY_NO_INTERACTION: Run Poetry un non-interactive mode
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.7.0 \
    POETRY_NO_INTERACTION=1

WORKDIR /src

FROM base as builder

RUN pip install "poetry==$POETRY_VERSION" \
 && python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install --no-deps -r /dev/stdin

COPY src ./src
COPY tests ./tests
RUN poetry build && /venv/bin/pip install dist/*.whl
