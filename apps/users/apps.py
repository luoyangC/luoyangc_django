from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'apps.users'
    verbose_name = '用户'

    def ready(self):
        import users.signals
