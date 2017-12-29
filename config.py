import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = os.urandom(24)
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost/users"

	
class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = "Add RDS ip later"
	
config = {
	"Development": DevelopmentConfig,
	"Production": ProductionConfig
}
