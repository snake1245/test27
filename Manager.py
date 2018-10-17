from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis


class Config(object):
    # 配置数据
    DEBUG = True
    # 配置数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1/information25"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

app = Flask(__name__)

# 导入配置
app.config.from_object(Config)
# 将数据库与app关联 初始化数据库
db = SQLAlchemy(app)
# 初始化redis的存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
# 开启项目的保护
CSRFProtect(app)


@app.route("/")
def index():
    return "helloworld"

if __name__ == '__main__':
    app.run()