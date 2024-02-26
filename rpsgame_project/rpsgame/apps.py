from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RpsgameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rpsgame'
    verbose_name = _('rpsgame')
