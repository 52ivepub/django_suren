from django.db import models

class ToDoItem(models.Model):

    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = 'Todo Item'
        ordering = ("id", )
        # verbose_name_plural = 'ModelNames'

    title = models.CharField(max_length=250)
    done = models.BooleanField(default=False, )


    def __str__(self):
        return self.title


