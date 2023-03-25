from sanic import Sanic
from sanic.response import text

server = Sanic("test_api")

@server.get("/health")
async def health(request):
    return text("OK")

@server.get("/prompt")
async def prompt(request):
    return text("OK")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)