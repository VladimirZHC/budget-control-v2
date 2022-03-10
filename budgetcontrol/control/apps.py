from django.apps import AppConfig


class ControlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'control'


# class TestsConfig(AppConfig):
#     def ready(self):
#         from simple_history.tests.models \
#             import HistoricalPollWithExtraFields

#         pre_create_historical_record.connect(
#             add_history_ip_address,
#             sender=HistoricalPollWithExtraFields
#         )