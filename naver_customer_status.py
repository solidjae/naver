import http.client
import json
import parsing_customer_status
import naver_token
from dotenv import load_dotenv
import os


def get_customer_status():
    
    load_dotenv()

    client_id = os.getenv('client_id')
    client_secret = os.getenv('client_secret')

    token = naver_token.get_token(client_id, client_secret)

    conn = http.client.HTTPSConnection("api.commerce.naver.com")
    headers = {'Authorization': token}
    conn.request("GET", "/external/v1/customer-data/customer-status/account/statistics?startDate=2023-01-01&endDate=2024-01-01", headers=headers)

    response = conn.getresponse()
    data = response.read().decode("utf-8")

    # Parse the JSON data
    json_data = json.loads(data)

    # Prettify the JSON data
    pretty_data = json.dumps(json_data, indent=4, sort_keys=True)

    # Print the prettified data
    print(pretty_data)

get_customer_status()
