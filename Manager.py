import logging

from flask import session
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from info import db,create_app


app = create_app("development")
# 创建命令行manager方法
manager = Manager(app)
# 创建迁移命令
migrate = Migrate(app,db)
# 把迁移命令加入到manager中
manager.add_command("db",MigrateCommand)


@app.route("/")
def index():
    # session["name"] = "itheima"
    # 打印日志
    logging.debug("测试debug")
    logging.warning("测试warning")
    logging.error("测试error")
    logging.fatal("测试fatal")
    return "helloworld"

if __name__ == '__main__':
    manager.run()