import requests
import json

client_id = r'a2638d37938b44449662924cf6a2af87'
client_secret = r'e4309999702c5c5aa394d05fb22c32452c804f07f235aa718ec4bf21a21427aa'

auth_data = {
    'grant_type'    : 'client_credentials',
    'client_id'     : client_id,
    'client_secret' : client_secret,
    'scope'         : 'read_content read_financial_data read_product_data read_user_profile'
}

# create session instance
session = requests.Session()

# make a POST to retrieve access_token
auth_request = session.post('https://idfs.gs.com/as/token.oauth2', data = auth_data)
access_token_dict = json.loads(auth_request.text)
access_token = access_token_dict['access_token']

# update session headers
session.headers.update({'Authorization':'Bearer '+ access_token})

# test API connectivity
request_url = 'https://api.marquee.gs.com/v1/data/USCANFPP_MINI/query'
request_query = {
                    "startDate": "2017-01-15",
                    "endDate":"2018-01-15"
               }
request = session.post(url=request_url, json=request_query)
results = json.loads(request.text)
with open("data.json", "w") as data:
    data.write(json.dumps(results, indent=4))