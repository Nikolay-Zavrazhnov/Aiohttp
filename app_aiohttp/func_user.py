import json
from aiohttp import web
from models import Session, UserAio


async def get_user(user_id: int, session: Session):
    user = await session.get(UserAio, user_id)
    if user is None:
        raise web.HTTPNotFound(text=json.dumps(
            {'status': 'error', 'description': 'user not found'}),
            content_type='application/json'
        )
    return user


def user_data_dict(user: UserAio):
    return {
        'id': user.id,
        'email': user.email,
        'create_time': user.create_time.isoformat()
    }