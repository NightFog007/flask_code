import os 
import sys 
from testhello import app 
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'
# app.root_path属性存储程序实例所在的路径。
dev_db = prefix + os.path.join(os.path.dirname(app.root_path),'data.db')
# 数据库URL和密钥都会首先从环境变量获取。
SECRET_KEY = os.getenv('SECRET_KEY','secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI',dev_db)