from django.db import models

class EmailAttachment(models.Model):
    name = models.CharField(max_length=255, default='')
    attachment = models.BinaryField()

    def __unicode__(self):
        return u'%s' % (self.id)

    class Meta:
        verbose_name = 'EmailAttachment'
        verbose_name_plural = 'EmailAttachments'
        app_label = "eemail"