from django.db import models
from django.contrib.auth import get_user_model


class Priority(models.Model):
    order = models.IntegerField(default=0)
    description = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.description)


class ToDo(models.Model):
    description = models.CharField(max_length=32)
    done = models.BooleanField(default=False)
    user_assigned = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    priority = models.ForeignKey(
        'Priority',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.description} ({"done" if self.done else "todo"})'
