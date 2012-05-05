import unittest

from django.conf import settings
from django.test.client import RequestFactory

from core import utils

#===============================================================================
class EnvironmentTest(unittest.TestCase):

    DEFAULT_ENV = 'dev'

    #---------------------------------------------------------------------------
    def setUp(self):
        """Set up request param to use"""
        self.request = RequestFactory
        setattr(self.request, 'session', {})
        self.request.session['environment'] = self.DEFAULT_ENV

    #---------------------------------------------------------------------------
    def test_set_env(self):
        """Test setting the environment"""
        utils.set_environment(self.request, 'qa')
        self.assertEqual('qa', self.request.session.get('environment', False))

    #---------------------------------------------------------------------------
    def test_get_env(self):
        """Test getting the environment"""
        env = utils.get_environment(self.request)
        self.assertEqual(self.DEFAULT_ENV, env)

    #---------------------------------------------------------------------------
    def test_get_env_data(self):
        """Test getting the environment information"""
        env_data = utils.get_environment_data(self.request)
        self.assertEqual(
            settings.ENVIRONMENTS.get(self.DEFAULT_ENV),
            env_data
        )

    #---------------------------------------------------------------------------
    def test_get_default_env(self):
        """Test getting the default environment"""
        default_env = utils.get_default_environment()
        self.assertEqual(self.DEFAULT_ENV, default_env)

    #---------------------------------------------------------------------------
    def test_get_env_db(self):
        """Test getting the environment database"""
        db = utils.get_environment_db(self.request)
        self.assertEqual(self.DEFAULT_ENV, db)

        # change environment
        utils.set_environment(self.request, 'qa')
        db = utils.get_environment_db(self.request)
        self.assertEqual('qa', db)