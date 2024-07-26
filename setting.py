import os
from dotenv import load_dotenv

load_dotenv()
db_url = 'postgresql://capstone_j2la_user:F3jzjN8RJCcUTkXdJfmFgfxzmswLaIBs@dpg-cqhub40gph6c73capdag-a/capstone_j2la'

db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')


auth0_domain = 'dev-kyu5aghzid56evr1.us.auth0.com'
api_audience = 'capstone-udacity'
