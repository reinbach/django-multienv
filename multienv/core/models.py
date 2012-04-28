from django.db import models

import utils

class Enviromment(models.Model):
    def save(self, env=None, *args, **kws):
        if env is None:
            env = utils.get_default_environment()
        save(usering=utils.get_environment_db(env))