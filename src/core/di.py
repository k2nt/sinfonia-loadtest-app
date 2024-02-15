from dependency_injector import providers, containers


class AppDI(containers.DeclarativeContainer):
    config_dict = providers.Configuration()
