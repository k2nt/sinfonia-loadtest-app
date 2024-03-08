FROM python:3.11-slim as final

# PYTHONDONTWRITEBYTECODE: Disable building .pyc files
# PYTHONFAULTHANDLER: Enable traceback on errors
# PYTHONHASHSEED: Seed value for random hashes
# PYTHONUNBUFFERED: Enable unbuffered mode when writing to terminal
ENV PYTHONDONTWRITEBYTECODE=1 \  
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

# update apt-get
RUN apt-get update && apt-get install --no-install-recommends -y curl git \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

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

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./
COPY src ./src
RUN poetry install

EXPOSE 8000

CMD ["poetry", "run", "start-app"]
