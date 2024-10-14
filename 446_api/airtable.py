# Airtable API connection
# This script works with the python SDK 
# to interact with the airtable api

# define dependencies
import os
from pyairtable import Api
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# authenticate
airtable_pat = os.getenv("AIRTABLE_PAT")
api = Api(airtable_pat)

print(airtable_pat)

# identify the table
table = api.table('appKld6zacTg1xSXJ', 'tblmwOgiUWABRijbR')
current_table = table.all()

print(current_table)