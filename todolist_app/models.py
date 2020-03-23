from django.db import models
from django.utils.timezone import now

# Create your models here.


class Todo(models.Model):

    added_date = models.DateTimeField(default=now)
    text = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.text)

    class Meta:
        verbose_name_plural = 'Todos'
