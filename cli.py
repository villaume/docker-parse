import json
import os
import requests
import argparse

PARSE_SERVER = 'http://localhost:1337/parse'
APP_ID = os.environ['APP_ID']
REST_API_KEY = os.environ['REST_API_KEY']
INSTALLATION_ID = os.environ['INSTALLATION_ID']
DEVICE_TOKEN = os.environ['TOKEN_ID']


def create_user():
    headers = {
      "X-Parse-Application-Id": APP_ID,
      "X-Parse-REST-API-Key": REST_API_KEY,
      "X-Parse-Revocable-Session": "1",
      "Content-Type": "application/json"
    }
    payload = {
        "username": "cooldude7",
        "password": "p_n7!-e8",
        "phone": "415-392-0202"
    }
    return requests.post(PARSE_SERVER + '/users', headers=headers,
                         data=json.dumps(payload))


def login_user():
    headers = {
      "X-Parse-Application-Id": APP_ID,
      "X-Parse-REST-API-Key": REST_API_KEY,
      "X-Parse-Revocable-Session": "1",
      "Content-Type": "application/json"
    }
    payload = {
        "username": "cooldude7",
        "password": "p_n7!-e8",
    }
    r = requests.get(PARSE_SERVER + '/login', headers=headers, params=payload)
    login_session = r.json().get('sessionToken', '')
    return login_session


def create_restricted_session(login_session):
    headers = {
      "X-Parse-Application-Id": APP_ID,
      "X-Parse-REST-API-Key": REST_API_KEY,
      "X-Parse-Session-Token": login_session,
      "Content-Type": "application/json"
    }
    payload = {
        "someNewField": 42
    }
    r = requests.post(PARSE_SERVER + '/sessions', headers=headers,
                      params=payload)

    return r.json().get('sessionToken', '')


def create_installation():
    headers = {
      "X-Parse-Application-Id": APP_ID,
      "X-Parse-REST-API-Key": REST_API_KEY,
      "Content-Type": "application/json"
    }
    payload = {
          "deviceType": "ios",
          "deviceToken": DEVICE_TOKEN,
          "channels": [
            "general"],
          "installationId": INSTALLATION_ID
        }

    r = requests.post(PARSE_SERVER + '/installations', headers=headers,
                      data=json.dumps(payload))
    return r.json()


def link_installation_to_session(session, installation_id):
    headers = {
      "X-Parse-Application-Id": APP_ID,
      "X-Parse-REST-API-Key": REST_API_KEY,
      "X-Parse-Session-Token": session,
      "X-Parse-Installation-Id": installation_id,
      "Content-Type": "application/json"
    }
    payload = {}

    return requests.put(PARSE_SERVER + '/sessions/me', headers=headers,
                        data=json.dumps(payload)).json


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", help="setup or push")
    args = parser.parse_args()

    if args.mode == 'setup':
        usr = create_user()
        login_session = login_user()
        restricted_session = create_restricted_session(login_session)
        inst = create_installation()
        link_installation_to_session(restricted_session, INSTALLATION_ID)
