from django.db import models

class WinLossCount(models.Model):
    win_count = models.IntegerField(default=0)
    loss_count = models.IntegerField(default=0)
