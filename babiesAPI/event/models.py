from django.db import models

class Event(models.Model):
    eventType = models.CharField(max_length=80, null=False)
    datetime = models.DateTimeField()
    info = models.CharField(max_length=500, null=False)
    baby = models.ForeignKey(
        'baby.Baby',
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )

    def __str__(self):
        return 'Event: \tbaby:{}\tdate:{} '.format(self.baby,self.datetime)
