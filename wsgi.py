import os
from dotenv import load_dotenv

# 加载环境变量 - gunicorn 服务器运行时需要的配置
# flask 内置的开发服务器不需要，因为 python-dotenv 会自动导入
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


from app import create_app

app = create_app()


if __name__ == '__main__':
    # 通过 url_map 可以查看整个 flask 中的路由信息
    print(app.url_map)
    app.run(debug=True)
