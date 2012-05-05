from django.conf import settings

#---------------------------------------------------------------------------
def set_environment(request, env):
    """Set the environment to that provided
    If not valid then set to default
    """
    if env in settings.ENVIRONMENTS:
        request.session['environment'] = env
    else:
        request.session['environment'] = get_default_environment()

#---------------------------------------------------------------------------
def get_default_environment():
    """Get the default environment"""
    for env, data in settings.ENVIRONMENTS.items():
        if data.get('default'):
            return env
    raise "There is no default environment"

#---------------------------------------------------------------------------
def get_environment(request):
    if request is None:
        return get_default_environment()
    if not request.session.get('environment', False):
        request.session['environment'] = get_default_environment()
    return request.session.get('environment', None)

#---------------------------------------------------------------------------
def get_environment_data(request):
    env = get_environment(request)
    return settings.ENVIRONMENTS.get(env)

#---------------------------------------------------------------------------
def get_environment_db(request):
    """Determine/set the database to use based on environment"""
    env = get_environment_data(request)
    if env is None:
        return None
    return env.get('database', None)
