from django.core.urlresolvers import reverse
from django.db import models

class Quote(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=100)
    PROGRAM_CHOICES = (
            ('BCS', 'BTech'),
            ('MCS', 'MTech'),
            ('MCA', 'MCA'),
    )
    program = models.CharField(max_length=3,
                               choices = PROGRAM_CHOICES,
                               default = 'BCS')
    class_of = models.IntegerField("Enter year of passing out")
    submission_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('quotes:detail', kwargs={'pk': self.pk})
