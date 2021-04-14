from django.db import models


class Item(models.Model):
    text = models.TextField(default='', verbose_name='Task')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        #ordering = ['id']
