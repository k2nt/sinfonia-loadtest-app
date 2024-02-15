from typing import Dict

import logging.config

import uvicorn
from fastapi import FastAPI

from dependency_injector.wiring import Provide, inject

from src.core.di import AppDI

from src.api.router import router


def app_factory() -> FastAPI:
    """Create FastAPI application."""
    app = FastAPI(
        app_name="Sinfonia load test",
        )
    
    app.logger = logging.getLogger()
    
    app.include_router(router)
    
    return app


def build_di():
    """Build dependency injection."""
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
def build(
        config_dict: Dict = Provide[AppDI.config_dict]
):
    """Build application dependencies."""
    # Logging

    logging.config.dictConfig(config_dict['logging'])


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
    build_di()
    build()
    start()


if __name__ == "__main__":
    start_app()
