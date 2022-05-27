class Config(object):
	"""
	Configuration base, for all environments.
	"""
	DEBUG = False
	TESTING = False
	


class ProductionConfig(Config):
	# SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'
	# SQLALCHEMY_TRACK_MODIFICATIONS = False
    pass

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True