from django.db import models

class Baby(models.Model):
    name = models.CharField(max_length=80, null=False)
    lastname = models.CharField(max_length=80, null=False)
    parent = models.ForeignKey(
        'parent.Parent',
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )

    def __str__(self):
        return 'Baby: \tname:{} {} '.format(self.name,self.lastname)
