from server import init_app

if __name__ == "__main__":
    web_server = init_app()
    web_server.run(debug=True)