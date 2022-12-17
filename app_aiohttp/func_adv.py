import json
from aiohttp import web
from models import Session, AdvAio


async def get_adv(adv_id: int, session: Session):
    user = await session.get(AdvAio, adv_id)
    if user is None:
        raise web.HTTPNotFound(text=json.dumps(
            {'status': 'error', 'description': 'advertisement not found'}),
            content_type='application/json'
        )
    return user


def advertisement_data_dict(advertisements: AdvAio):
    return {
        'id': advertisements.id,
        'title': advertisements.title,
        'text': advertisements.text,
        'published_at': advertisements.published_at.isoformat(),
    }
