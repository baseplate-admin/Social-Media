from django.db import models


class StatisticsModel(models.Model):
    avatar_fetch_count = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return f"Total avatar fetched = {str(self.avatar_fetch_count)} |"
