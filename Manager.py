from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from flask_session import Session


class Config(object):
    # 配置数据
    DEBUG = True
    # 设置session密钥
    SECRET_KEY = "tKAPUrf2NmMka2Vula+cdueIkJBZ0cQ+O5A0uSiyKet2YJKf"
    # 配置数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1/information25"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # redis的保存配置
    SESSION_TYPE = "redis"
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 指定session保存到redis中
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    # 设置session需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2


app = Flask(__name__)

# 导入配置
app.config.from_object(Config)
# 将数据库与app关联 初始化数据库
db = SQLAlchemy(app)
# 初始化redis的存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
# 开启项目的保护
CSRFProtect(app)
# 初始化session的保存位置
Session(app)


@app.route("/")
def index():
    session["name"] = "itheima"
    return "helloworld"

if __name__ == '__main__':
    app.run()