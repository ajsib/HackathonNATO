import os
from dotenv import load_dotenv

load_dotenv()

# Azure OpenAI configuration
AZURE_OPENAI_CONFIG = {
    'api_key': os.getenv('AZURE_OPENAI_KEY'),
    'endpoint': os.getenv('AZURE_OPENAI_ENDPOINT')
}