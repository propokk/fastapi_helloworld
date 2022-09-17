import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB : str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}"
    TEST_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/test_hw_db"

    AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
    AUTH0_AUDIENCE = os.getenv("AUTH0_AUDIENCE")
    AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
    AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")

    AUTH0_TEST_TOKEN = { 'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik40SEJvb2xGYl80WDE5MjhBWUlnNiJ9.eyJpc3MiOiJodHRwczovL2Rldi01bzcwenBvMi51cy5hdXRoMC5jb20vIiwic3ViIjoicFlUSUh6bzNrUVdTRHRUOUVacURRZ3BiYm5PUEJHVnRAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vMTI3LjAuMC4xOjgwMDAvbG9naW4iLCJpYXQiOjE2NjI3MzU0NjYsImV4cCI6MTY2MjgyMTg2NiwiYXpwIjoicFlUSUh6bzNrUVdTRHRUOUVacURRZ3BiYm5PUEJHVnQiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.9eQmjoVsbEB8SdngxP-8wKxGkrkVY1j6nAMNNUw9__gR2eYX0EYLi5aaTR9CQvtZFJgviarneMpCOQtMm_i2GQTn4coAIBrpjHK6kZjiOtMDq1NHG9lpGoBa1mALYCXXX4CKuYPS1ggsiV4O2se4p1qSVPa-oJm6Tt2gVuBtMpX_espWDwv9UuIvOzQEEbrOmOcfUCcAvfVKN3ztETXFtVmZqpKZ3gZh_cvAFo7ToF56X2CTKK9b5klpluPpxRlEaDnUlgFQsLtgoGJuiBrdRa0Hg2g6JXn-y9F2Wndl3eIEd9bvkmx9o1AnaqVpdwaPYtvqCQHbTlAO95LWYxVzgw" }

settings = Settings()