from flask import Flask
import os
import click

from app.config import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'default')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_blueprints(app)
    register_plugin(app)
    register_commands(app)

    # for key, value in app.config.items():
    #     print(f'{key}={value}')

    return app


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix="/v1")


def register_plugin(app):
    from app.models import db
    db.init_app(app)


def register_commands(app):
    from app.models import db

    @app.cli.command()
    @click.option('--drop', is_flag=True)       # is_flag=True 表明参数值可以省略
    def initdb(drop):
        """
            生成数据库表
                如果是sqlite，则 db.create_all() 函数会创建数据库文件以及数据库表
                如果是mysql，需要提前手动创建数据库，db.create_all() 函数只能创建数据库表
            使用
                flask initdb
                或
                flask initdb --drop
        """
        if drop:
            db.drop_all()
        db.create_all()
        click.echo("数据库表创建成功")
