from django.db.models import F
from asgiref.sync import sync_to_async
from custom.statistics.models import StatisticsModel


@sync_to_async()
def increase_avatar_count_by_one() -> None:
    model = StatisticsModel.objects.get_or_create()[0]
    model.avatar_fetch_count = F("avatar_fetch_count") + 1
    model.save()
