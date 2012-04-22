class EnvironmentRouter(object):
    """A router that determines database to use by environment session setting"""

    # def db_for_read(self, model, **hints):
    #     """Point all reads for an environment to specific environment database"""
    #     pass

    # def db_for_write(self, model, **hints):
    #     """Point all writes for an environment to specific environment database"""
    #     pass

    # def allow_syncdb(self, db, model):
    #     "Non environment models allow syncing"
    #     print "model: ", model._meta.app_label
    #     if hasattr(model._meta, 'prevent_dbsync'):
    #         return False
    #     return True