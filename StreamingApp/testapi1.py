# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values
from django.conf import settings

if __name__ == "__main__":
    load_dotenv()

    # accessing and printing value
    print("****************************")
    print(os.getenv("SECRET_KEY"))
    print("response.text")
    print(settings.cyrus)
    print("response.text")