from django.db import models
from django.core.urlresolvers import reverse


class Team(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teams_fbv:team_edit', kwargs={'pk': self.pk})