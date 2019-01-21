import logging
import os
import gzip
from logging.handlers import TimedRotatingFileHandler

DEBUG = os.getenv('FLASK_ENV') == 'development'
HOST = os.getenv('APPLICATION_HOST', '127.0.0.1')
PORT = int(os.getenv('APPLICATION_PORT', '5000'))

POSTGRES = {
    'user': os.getenv('APPLICATION_POSTGRES_USER', 'postgres'),
    'pw': os.getenv('APPLICATION_POSTGRES_PW', ''),
    'host': os.getenv('APPLICATION_POSTGRES_HOST', '127.0.0.1'),
    'port': os.getenv('APPLICATION_POSTGRES_PORT', '5432'),
    'db': os.getenv('APPLICATION_POSTGRES_DB', 'postgres')
}
DB_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

SECRET_KEY = os.getenv('SECRET_KEY', b'3OVQ\xb6\x12\xe1w\xf8z\x8eK4Y\x8c\x0f\x078\x08\xe1\x18\x07\x00\x11')

SQLALCHEMY_POOL_SIZE = os.getenv('SQLALCHEMY_POOL_SIZE', 20)
SQLALCHEMY_MAX_OVERFLOW = os.getenv('SQLALCHEMY_MAX_OVERFLOW', 100)


class GZipRotator:
    def __call__(self, source, dest):
        os.rename(source, dest)
        f_in = open(dest, 'rb')
        f_out = gzip.open("%s.gz" % dest, 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()
        os.remove(dest)

GzipRotatorHandler = TimedRotatingFileHandler(
    filename=os.getenv('SERVICE_LOG','vpn-monitor.log'),
    when="midnight",
    backupCount=os.getenv('MAX_LOGFILE_CNT',30)
)

GzipRotatorHandler.rotator = GZipRotator()


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[GzipRotatorHandler]
)
