from django.db import models
from django.core.urlresolvers import reverse

class  Url(models.Model):
    main_url = models.CharField(max_length=220,)
    new_url = models.CharField(max_length=30,)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
