from django.core.exceptions import ImproperlyConfigured
from django.apps import apps, AppConfig

class GenericAppConfig(AppConfig):
    name = 'generic'
    verbose_name = "generic app"

    def ready(self):
        """
        this method will be called after all models 
        are registered in the django app
        """
        
