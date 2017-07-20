from django.db import models

class Fish(models.Model):
    name = models.CharField(max_length=255, default='')

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = 'Fish'
        verbose_name_plural = 'Fishes'
        app_label = "api"

class Person(models.Model):
    name = models.CharField(max_length=255, default='')
    position = models.CharField(max_length=255, default='')
    salary = models.CharField(max_length=255, default='')
    start_date = models.CharField(max_length=255, default='')
    office = models.CharField(max_length=255, default='')
    extn = models.CharField(max_length=255, default='')

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        app_label = "api"
