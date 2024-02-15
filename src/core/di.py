import logging.config

from dependency_injector import providers, containers


class AppDI(containers.DeclarativeContainer):
    """Application dependency injection container."""
    # Core

    config_dict = providers.Configuration()

    logging = providers.Resource(
        logging.config.dictConfig,
        config_dict.logging,
        )
