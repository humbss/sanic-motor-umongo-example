from sanic import Sanic
from util.umongo_connection import connect
from api.routes import add_routes
import uvloop
import asyncio
import aiotask_context as context
from sanic_openapi import swagger_blueprint

app = Sanic()
app.blueprint(swagger_blueprint)


@app.listener('before_server_start')
async def init(sanic, loop):
    asyncio.set_event_loop(uvloop.new_event_loop())
    connect(app.config.get('dbhost'), app.config.get('dbport'), loop)


@app.middleware('request')
async def add_key(request):
    context.set('db_host', app.config.get('dbhost'))
    context.set('db_port', app.config.get('dbport'))

add_routes(app)

if __name__ == '__main__':
    server = app.create_server(
        host="0.0.0.0", port=8000, return_asyncio_server=True)
    loop = asyncio.get_event_loop()
    loop.set_task_factory(context.task_factory)
    task = asyncio.ensure_future(server)
    try:
        loop.run_forever()
    except:
        loop.stop()
