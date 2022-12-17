from aiohttp import web
from views_aiohttp import UsersViews, AdvViews
from models import engine, Base, UserAio, Session
from middlewares import session_middleware

app_aiohttp = web.Application(middlewares=[session_middleware])

async def orm_context(app_aiohttp: web.Application):
    print('start')
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()
    print('end')

app_aiohttp.cleanup_ctx.append(orm_context)
app_aiohttp.add_routes(
        [
            web.get('/users/{user_id:\d+}', UsersViews),
            web.post('/users/', UsersViews),
            web.patch('/users/{user_id:\d+}', UsersViews),
            web.delete('/users/{user_id:\d+}', UsersViews),
            web.get('/advertisements/{adv_id:\d+}', AdvViews),
            web.post('/advertisements/', AdvViews),
            web.patch('/advertisements/{adv_id:\d+}', AdvViews),
            web.delete('/advertisements/{adv_id:\d+}', AdvViews)
        ]
    )


if __name__ == '__main__':
    web.run_app(app_aiohttp)
