"""
Configuration module for the Video Editor Bot
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Bot configuration class"""
    
    # Telegram Bot Configuration
    BOT_TOKEN = os.getenv("8784253318:AAGkOy2f650Jzlr-x8XvcuaMVQmd-BBHumA")
    API_ID = int(os.getenv("API_ID", "15055049"))
    API_HASH = os.getenv("abe3f66fcd80c91e53009ba52c7b3a83")
    
    # MongoDB Configuration
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://newsudo:786780@cluster0.pbiae8a.mongodb.net/?appName=Cluster0")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "newsudo")
    
    # Channel Configuration
    LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True") == "True"
    
    # Admin Configuration
    ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "7653921320,8808274917").split(",") if x.strip()]
    
    # File Settings
    MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", "2000"))  # in MB
    DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH", "./downloads")
    UPLOAD_PATH = os.getenv("UPLOAD_PATH", "./uploads")
    
    # Feature Toggles
    ENABLE_BROADCAST = os.getenv("ENABLE_BROADCAST", "True") == "True"
    ENABLE_URL_UPLOAD = os.getenv("ENABLE_URL_UPLOAD", "True") == "True"
    ENABLE_WATERMARK = os.getenv("ENABLE_WATERMARK", "True") == "True"
    
    # Ensure directories exist
    os.makedirs(DOWNLOAD_PATH, exist_ok=True)
    os.makedirs(UPLOAD_PATH, exist_ok=True)
    os.makedirs("logs", exist_ok=True)
