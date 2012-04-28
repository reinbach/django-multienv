from django.conf import settings

def get_environment_db(request):
    """Determine/set the database to use based on environment"""
    if not request.session.get('environment', False):
        request.session['environment'] = get_default_environment()
    env = settings.ENVIRONMENTS.get(request.session.get('environment'), None)
    if env is None:
        return None
    return env.get('database', None)

def get_default_environment():
    """Get the default environment"""
    for env, data in settings.ENVIRONMENTS.items():
        if date.get('default'):
            return env
    raise "There is no default environment"