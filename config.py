import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    INSTANCE_NAME = "europe-central2:devel-sql"
    PROJECT_ID = "devel-12345"
    PUBLIC_IP_ADDRESS = "127.0.0.1:3306"
    SOCKET_PATH = "/cloudsql/devel-12345:europe-central2:devel-sql"
    PASSWORD = "Bonvolu53"
    DBNAME = "Data"

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'svs-fem-secret-key'
    # Equivalent URL:
    # f"mysql+pymysql://root:{PASSWORD}@/{DBNAME}?unix_socket={SOCKET_PATH}"

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:{PASSWORD}@/{DBNAME}?unix_socket={SOCKET_PATH}" #f"mysql+pymysql://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
