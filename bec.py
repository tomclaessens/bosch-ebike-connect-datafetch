import json
import random
import requests

class BoschEbikeConnect:
    data = {}
    config = {}
    session = {}
    token = ''

    def __init__(self):
        self.read_configuration()
        self.start_session()
        self.fetch_login_token()
        self.fetch_statistics()
        
    def read_configuration(self):
        with open("config.json") as json_data:
            self.config = json.load(json_data)

    def start_session(self):
        self.session = requests.Session()

    def fetch_login_token(self):
        payload = {
            'username': self.config['BOSCH_EBIKE_CONNECT_CREDENTIALS']['username'],
            'password': self.config['BOSCH_EBIKE_CONNECT_CREDENTIALS']['password'],
            'rememberme': 'true'
        }

        self.session.post(self.config['BOSCH_EBIKE_CONNECT_PORTAL']['login_url'], json=payload)
        self.token = self.session.cookies['REMEMBER']

    def fetch_statistics(self):
        headers = {
            'cookie': 'REMEMBER=' + self.token,
            'referer': 'https://www.ebike-connect.com/dashboard',
            'user-agent': str(random.random())[3:],
            'authority': 'www.ebike-connect.com',
            'protect-from': 'CSRF'
        }

        self.data = self.session.get(self.config['BOSCH_EBIKE_CONNECT_PORTAL']['statistics_url'], headers=headers).json()

    def get_statistics(self):
        return self.data