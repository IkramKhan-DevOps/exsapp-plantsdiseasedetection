import json
import requests
from requests.auth import HTTPBasicAuth


def auth(username='mark', email='mark@exarth.com', password='mark'):
    data = {
        "username": username,
        "email": email,
        "password": password
    }

    response = requests.post('https://pcuav.pythonanywhere.com/auth/login/', data=data)
    status_code = int(response.status_code)
    if status_code == 200:
        output = json.loads(response.content)
        return output['key']

    print(
        "Error In Authentication: Please check api at https://pcuav.pythonanywhere.com/auth/login/ | error code:",
        status_code
    )
    return None


def post_image(path=None):
    """ STEP1: CALLS AUTHENTICATION -------------------------------------------- """
    token = auth()
    base_url = 'https://pcuav.pythonanywhere.com/api/capture/'
    headers = {'Authorization': "Token {}".format(token)}
    data = {
        "x_axis": "2637",
        "y_axis": "3123",
    }
    """ ------------------------------------------------------------------------- """

    """ STEP2: SETTINGS API ----------------------------------------------------- """
    _path = r"C:\Users\DEEBYTE COMPUTERS\Pictures\Screen\Screenshot 2021-11-14 234009.png"

    files = {'image': open(_path, 'rb')}
    auth_response = requests.post(url=base_url, headers=headers, data=data, files=files)
    """ ------------------------------------------------------------------------- """

    """ STEP3: CHECK STATUS ----------------------------------------------------- """
    if auth_response.status_code == 201:
        print(auth_response.json())
    else:
        print("something Wrong Error Code:", auth_response.status_code)
        print(auth_response.content)
    """ ------------------------------------------------------------------------- """


if __name__ == '__main__':
    post_image()
