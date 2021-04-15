from django.db import models


class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default='', verbose_name='Task')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        #ordering = ['id']

