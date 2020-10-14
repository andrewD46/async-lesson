import asyncio
import random

from aiohttp import web


routes = web.RouteTableDef()


@routes.get('/')
async def main(request):
    return web.Response(text="Hello!")


@routes.post('/post')
async def post(request):
    data = await request.post()
    await asyncio.sleep(random.randint(0, 5))
    sum_numbers = int(data['first_number']) + int(data['second_number'])
    return web.Response(text=f'{sum_numbers}')


app = web.Application()
app.add_routes(routes)
web.run_app(app)
