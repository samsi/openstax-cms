from django.db import models

class ProgressTracker(models.Model):
    account_id = models.IntegerField()
    progress = models.IntegerField()

    def __str__(self):
        return self.account_id
