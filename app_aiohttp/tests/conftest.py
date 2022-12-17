import datetime
import time

# from database import Base, Session, AdvModel, OwnerModel
from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app_aiohttp.models import AdvAio, UserAio, Base


engine = create_engine('postgresql://app_aio:5555@127.0.0.1:7778/app_aio')
Session = sessionmaker(bind=engine)


@fixture(scope='session', autouse=True)
def prepare_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


@fixture()
def create_user():
    with Session() as session:
        new_user = UserAio(email=f"{time.time()}@ddd.ty", password='userpass')
        session.add(new_user)
        session.commit()
        return {
            'id': new_user.id,
            'email': new_user.email,
            'create_time': new_user.create_time
        }


@fixture()
def create_adv():
    with Session() as session:
        new_adv = AdvAio(title='NEW_TITLE', text='NEW_TEXT_ADV', published_at=f"{datetime.datetime.now()}", owner_id=1)
        session.add(new_adv)
        session.commit()
        return {
            'id': new_adv.id,
            'title': new_adv.title,
            'text': new_adv.text,
            'published_at': new_adv.published_at,
            'owner_id': new_adv.owner_id,
        }
