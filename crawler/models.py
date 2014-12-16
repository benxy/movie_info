from django.db import models

import datetime


class Destination(models.Model):
    """
    TODO: Describe this model
    """
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=1024)
    last_search_date = models.DateTimeField(auto_now=True, default=datetime.datetime.now)

    def __unicode__(self):
        return "Name:%s - Path:%s" % (self.name, self.path)

    def __str__(self):
        return self.__unicode__()
