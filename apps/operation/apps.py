from django.apps import AppConfig


class OperationConfig(AppConfig):
    name = 'operation'
    verbose_name = '操作'

    def ready(self):
        import operation.signals
