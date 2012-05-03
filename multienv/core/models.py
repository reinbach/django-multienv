from django.db import models

import utils

class EnvironmentManager(models.Manager):
    ENV = utils.get_default_environment()
    
    def get_query_set(self):
        return super(EnvirommentManager, self).get_query_set(
            using=utils.get_environment_db(self.ENV)
        )

class Environment(models.Model):
    objects = EnvironmentManager()

    def save(self, request=None, *args, **kws):
        if request is not None:
            self.ENV = utils.get_environment(request)
        super(Environment, self).save(using=utils.get_environment_db(self.ENV))

    def set_environment(self, env):
        self.ENV = env
