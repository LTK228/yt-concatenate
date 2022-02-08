from dotenv import load_dotenv
import os

load_dotenv()                   # take environment variables from .env.
# load_dotenv(verbose=True)       # 其他模式：印出詳細資訊 (載入哪些資料)
API_KEY = os.getenv('API_KEY')
