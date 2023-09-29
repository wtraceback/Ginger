from app import create_app

app = create_app()

if __name__ == '__main__':
    # 通过 url_map 可以查看整个 flask 中的路由信息
    print(app.url_map)
    app.run(debug=True)
