from django.db import models
from base.models import AbstractCommonModel
# Create your models here.


class TaskLabel(AbstractCommonModel):
    label = models.CharField(max_length=100)

    def __unicode__(self):
        return self.label

    def __str__(self):
        return self.__unicode__()


class Task(AbstractCommonModel):
    name = models.CharField(max_length=100)
    label = models.ForeignKey(TaskLabel,on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return "{0}-{1}".format(self.label,self.name)


