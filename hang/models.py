# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User

class Phrases(models.Models):
    phrase = models.CharField(max_length=200)

class Top_scores(models.Models):
    name_text = models.ForeignKey(User)
    phrase = models.ForeignKey(Phrases)
    top_score = models.IntegerField(default=0)