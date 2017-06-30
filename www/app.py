#!/usr/bin/env python3
#encoding=utf-8

#日志输出
import logging;logging.basicConfig(level=logging.INFO)

import asyncio

from aiohttp import web

def index(request):
	return web.Response(body=b'<h1>hello,world<h1>',content_type="text/html")

async def init(loop):
	app=web.Application(loop=loop)
	#将index当作家页面获得
	app.router.add_route('GET','/',index)
	#创建一个服务器端口
	srv=await loop.create_server(app.make_handler(),'127.0.0.1',9000)
	#日志文件
	logging.info('server started at http://127.0.0.1:9000')
	return srv

#创建一个EventLoop对象，协程将在这里面运行
loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()