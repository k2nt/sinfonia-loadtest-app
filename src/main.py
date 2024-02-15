import uvicorn
from fastapi import FastAPI

from dependency_injector.wiring import Provide, inject

from src.core.di import AppDI

import src.lib.http as a


a.is_success_status_code(200)


def app_factory() -> FastAPI:
    """Create FastAPI application."""
    app = FastAPI()
    return app


def build():
    """Build dependencies."""
    # Dependency injection
    
    app_di = AppDI()
    app_di.config_dict.from_yaml("src/config.yml")
    app_di.init_resources()
    
    # only inject into Service layer
    # this is to obey Clean Architecture, where Views are state-agnostic.
    app_di.wire(
        modules=[
            __name__
            ]
        )


@inject
def start(
        config_dict = Provide[AppDI.config_dict]
):
    """Build and launch FastAPI application."""
    uvicorn.run(
        app=app_factory(),
        port=config_dict['app']['port'],
        )
    
    
def start_app():
    """Launch application."""
    build()
    start()


if __name__ == "__main__":
    start_app()
