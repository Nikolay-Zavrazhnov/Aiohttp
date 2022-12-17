from aiohttp import web
from models import UserAio, AdvAio
from func_user import user_data_dict, get_user
from func_adv import advertisement_data_dict, get_adv


class UsersViews(web.View):

    @property
    def session(self):
        return self.request['session']

    async def get(self):
        user_id = int(self.request.match_info['user_id'])
        user = await get_user(user_id, self.session)
        return web.json_response(
            user_data_dict(user)
        )

    async def post(self):
        user_data = await self.request.json()
        new_user = UserAio(**user_data)
        self.session.add(new_user)
        await self.session.commit()
        return web.json_response(
            user_data_dict(new_user)
        )

    async def patch(self):
        user_id = int(self.request.match_info['user_id'])
        user_patch = await self.request.json()
        user = await get_user(user_id, self.session)
        for field, value in user_patch.items():
            setattr(user, field, value)
        self.session.add(user)
        await self.session.commit()
        return web.json_response(user_data_dict(user))

    async def delete(self):
        user_id = int(self.request.match_info['user_id'])
        user = await get_user(user_id, self.session)
        await self.session.delete(user)
        await self.session.commit()
        return web.json_response(
            {
                'status': 'deleted'
            }
        )


class AdvViews(web.View):

    @property
    def session(self):
        return self.request['session']

    async def get(self):
        adv_id = int(self.request.match_info['adv_id'])
        advertisements = await get_adv(adv_id, self.session)
        return web.json_response(
            advertisement_data_dict(advertisements)
        )

    async def post(self):
        adv_data = await self.request.json()
        new_advertisement = AdvAio(**adv_data)
        self.session.add(new_advertisement)
        await self.session.commit()
        return web.json_response(
           advertisement_data_dict(new_advertisement)
        )

    async def patch(self):
        adv_id = int(self.request.match_info['adv_id'])
        adv_patch = await self.request.json()
        advertisement = await get_adv(adv_id, self.session)
        for field, value in adv_patch.items():
            setattr(advertisement, field, value)
        self.session.add(advertisement)
        await self.session.commit()
        return web.json_response(advertisement_data_dict(advertisement))

    async def delete(self):
        adv_id = int(self.request.match_info['adv_id'])
        advertisement = await get_adv(adv_id, self.session)
        await self.session.delete(advertisement)
        await self.session.commit()
        return web.json_response(
            {
                'status': 'deleted'
            }
        )