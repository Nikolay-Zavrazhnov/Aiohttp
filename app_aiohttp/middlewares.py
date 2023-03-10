from aiohttp import web
from models import Session

@web.middleware
async def session_middleware(request: web.Request, handler):

    async with Session() as session:
        request['session'] = session
        return await handler(request)