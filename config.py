from redis import StrictRedis


class Config(object):
    # 配置数据
    # DEBUG = True
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


class Development(Config):
    # 开发环境
    DEBUG = True


class ProductionConfig(Config):
    # 生产环境
    DEBUG = False


class TestingConfig(Config):
    # 测试环境
    DEBUG = True
    TESTING = True

config = {
    "development":Development,
    "production":ProductionConfig,
    "testing":TestingConfig
}