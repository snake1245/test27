from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    # 配置数据
    DEBUG = True
    # 配置数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1/information25"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
# 将数据库与app关联 初始化数据库
db = SQLAlchemy(app)
# 导入配置
app.config.from_object(Config)


@app.route("/")
def index():
    return "helloworld"

if __name__ == '__main__':
    app.run()