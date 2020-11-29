# in terminal go this file directory -> cd code
# now run in terminal -> pytest -s -v test_api.py

import json
import requests

my_domain = 'istiaque1151512123456a.com'


class TestRESTAPI:
    def test_signIn(self):
        global site_id
        global accessToken
        api_url = "https://api2.omnikick.com/api/v1/signin"
        headers = {"content-type": "application/json;charset=UTF-8"}
        data = json.dumps({"email": "istiaque@aaroza.com", "password": "123456"})
        resp = requests.post(api_url, data=data, headers=headers)
        my_dict = json.loads(resp.text)
        accessToken = my_dict['accessToken']
        for i in range(len(my_dict['user']['sites'])):
            if my_domain == my_dict['user']['sites'][i]['domain']:
                site_id = my_dict['user']['sites'][i]['_id']
                break
        assert resp.status_code is 200

    def test_create_broadcast(self):
        api_url = "https://api2.omnikick.com/api/v1/sites/" + site_id + "/broadcasts"
        headers = {"content-type": "application/json;charset=UTF-8", "x-access-token": accessToken}
        data = json.dumps({"name": "create from api"})
        resp = requests.post(api_url, data=data, headers=headers)
        assert resp.status_code is 201

    def test_get_broadcast(self):
        global broadcast_id
        api_url = "https://api2.omnikick.com/api/v1/sites/" + site_id + "/broadcasts?status=draft"
        headers = {"x-access-token": accessToken}
        resp = requests.get(api_url, headers=headers)
        my_dict = json.loads(resp.text)
        broadcast_id = my_dict['data'][0]['_id']
        assert resp.status_code is 200

    def test_delete_broadcast(self):
        api_url = "https://api2.omnikick.com/api/v1/sites/" + site_id + "/broadcasts/" + broadcast_id
        headers = {"x-access-token": accessToken}
        resp = requests.delete(api_url, headers=headers)
        assert resp.status_code is 204
