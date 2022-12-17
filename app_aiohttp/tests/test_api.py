import requests
from app_aiohttp.tests.config import API_URL


def test_get_owner(create_user):
    new_user = create_user
    response = requests.get(f"{API_URL}/users/{new_user['id']}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['email'] == new_user['email']


def test_get_user_not_exist():
    response = requests.get(f"{API_URL}/users/5555")
    assert response.status_code == 404
    assert response.json() == {'status': 'error', 'description': 'user not found'}


def test_create_user():
    user_data = {
        'email': 'POST_mail@ur.rr',
        'password': 'POST_pass'
    }
    response = requests.post(f"{API_URL}/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()['email'] == user_data['email']


def test_patch_user(create_user):
    patch_user_data = {'email': 'PATCH_mail@ur.rr'}
    response = requests.patch(f"{API_URL}/users/{create_user['id']}", json=patch_user_data)
    assert response.status_code == 200
    assert response.json()['email'] == patch_user_data['email']

    response = requests.get(f"{API_URL}/users/{create_user['id']}")
    assert response.status_code == 200
    assert response.json()['email'] == patch_user_data['email']


def test_delete_user(create_user):
    response = requests.delete(f"{API_URL}/users/{create_user['id']}")
    assert response.status_code == 200
    assert response.json() == {'status': 'deleted'}

    response = requests.get(f"{API_URL}/users/{create_user['id']}")
    assert response.status_code == 404


def test_get_adv(create_adv):
    new_adv = create_adv
    response = requests.get(f"{API_URL}/advertisements/{new_adv['id']}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['title'] == new_adv['title']


def test_get_adv_not_exist():
    response = requests.get(f"{API_URL}/advertisements/5555")
    assert response.status_code == 404
    assert response.json() == {'status': 'error', 'description': 'advertisement not found'}


def test_create_adv():
    adv_data = {
        'title': 'TITLE_POST',
        'text': 'TEXT_POST',
        'owner_id': 1
    }
    response = requests.post(f"{API_URL}/advertisements/", json=adv_data)
    assert response.status_code == 200
    assert response.json()['title'] == adv_data['title']


def test_patch_adv(create_adv):
    patch_adv_data = {'title': 'PATCH_title', 'text': 'PATCH_text'}
    response = requests.patch(f"{API_URL}/advertisements/{create_adv['id']}", json=patch_adv_data)
    assert response.status_code == 200
    assert response.json()['title'] == patch_adv_data['title']

    response = requests.get(f"{API_URL}/advertisements/{create_adv['id']}")
    assert response.status_code == 200
    assert response.json()['title'] == patch_adv_data['title']


def test_delete_advertisement(create_adv):
    response = requests.delete(f"{API_URL}/advertisements/{create_adv['id']}")
    assert response.status_code == 200
    assert response.json() == {'status': 'deleted'}

    response = requests.get(f"{API_URL}/advertisements/{create_adv['id']}")
    assert response.status_code == 404

