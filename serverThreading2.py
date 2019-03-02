import web
from threading import Thread


urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return str(23)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
