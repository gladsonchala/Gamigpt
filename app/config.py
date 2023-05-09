import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    DEBUG = True
    MAX_CONTENT_LENGTH = 1024 * 1024 * 10 # 10MB maximum upload size
