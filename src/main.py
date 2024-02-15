import uvicorn
from fastapi import FastAPI


def app_factory() -> FastAPI:
    """Create FastAPI application."""
    app = FastAPI()
    return app


def start_app():
    """Build and run FastAPI application."""
    uvicorn.run(
        app=app_factory(),
        port=8000,
        )


if __name__ == "__main__":
    start_app()
