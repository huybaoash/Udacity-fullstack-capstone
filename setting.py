import os
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv('HEROKU_POSTGRESQL_BROWN_URL')
if db_url and db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')


auth0_domain = os.getenv('AUTH0_DOMAIN')
api_audience = os.getenv('API_AUDIENCE')
