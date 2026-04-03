from config_reader import settings


DEBUG = settings.DEBUG in ['true', 'True', '1', 't', 'T']
DATABASE_USER = settings.DATABASE_USER
DATABASE_PASSWORD = settings.DATABASE_PASSWORD.get_secret_value()
DATABASE_NAME = settings.DATABASE_NAME
DATABASE_URI = settings.DATABASE_URI
DATABASE_PORT = settings.DATABASE_PORT
