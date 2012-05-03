import unittest

from django.test.client import RequestFactory

from core import utils

#===============================================================================
class EnvironmentTest(unittest.TestCase):

    #---------------------------------------------------------------------------
    def setUp(self):
        """Set up request param to use"""
        self.request = RequestFactory
        setattr(self.request, 'session', {})
        self.request.session['environment'] = 'dev'

    #---------------------------------------------------------------------------
    def test_set_env(self):
        """Test setting the environment"""
        utils.set_environment(self.request, 'qa')
        self.assertEqual('qa', self.request.session.get('environment', False))

    #---------------------------------------------------------------------------
    def test_get_env(self):
        """Test getting the environment"""
        env = utils.get_environment(self.request)
        self.assertEqual('dev', env)

    #---------------------------------------------------------------------------
    def test_get_default_env(self):
        """Test getting the default environment"""
        default_env = utils.get_default_environment()
        self.assertEqual('dev', default_env)

    #---------------------------------------------------------------------------
    def test_get_env_db(self):
        """Test getting the environment database"""
        db = utils.get_environment_db('dev')
        self.assertEqual('multienv_dev', db)