from flask import Flask
from config import config
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis

# 将数据库与app关联 先初始化扩展的对象然后再调用init_app的方法去初始化
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    # 导入配置
    app.config.from_object(config[config_name])
    # 使用init_app初始化
    db.init_app(app)
    # 初始化redis的存储对象
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST,port=config[config_name].REDIS_PORT)
    # 开启项目的保护
    CSRFProtect(app)
    # 初始化session的保存位置
    Session(app)
    return app