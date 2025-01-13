# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Armazem(models.Model):

    #__Armazem_FIELDS__
    id_armazem = models.IntegerField(null=True, blank=True)
    nome = models.TextField(max_length=255, null=True, blank=True)
    local = models.TextField(max_length=255, null=True, blank=True)
    capacidade = models.IntegerField(null=True, blank=True)

    #__Armazem_FIELDS__END

    class Meta:
        verbose_name        = _("Armazem")
        verbose_name_plural = _("Armazem")


class Artigo-Local(models.Model):

    #__Artigo-Local_FIELDS__
    id_armazem = models.IntegerField(null=True, blank=True)
    id_artigo = models.IntegerField(null=True, blank=True)
    id_movimento = models.IntegerField(null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)

    #__Artigo-Local_FIELDS__END

    class Meta:
        verbose_name        = _("Artigo-Local")
        verbose_name_plural = _("Artigo-Local")


class Id_Familia(models.Model):

    #__Id_Familia_FIELDS__
    id_familia = models.TextField(max_length=255, null=True, blank=True)
    descricao = models.TextField(max_length=255, null=True, blank=True)
    nome = models.TextField(max_length=255, null=True, blank=True)

    #__Id_Familia_FIELDS__END

    class Meta:
        verbose_name        = _("Id_Familia")
        verbose_name_plural = _("Id_Familia")



#__MODELS__END
