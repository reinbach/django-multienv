from django.db import models

import utils

#===============================================================================
class Environment(models.Model):
    ENV_DB = utils.get_environment_db(None)

    class Meta:
        abstract = True
        managed = False

    #---------------------------------------------------------------------------
    def save(self, request=None, *args, **kws):
        if request is not None:
            self.ENV_DB = utils.get_environment_db(request)
        super(Environment, self).save(using=self.ENV_DB)
