import requests
import json

# Получение токена
url = "https://api-performance.ozon.ru/api/client/token"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
data = {
    "client_id": "42694746-1729579553646@advertising.performance.ozon.ru",
    "client_secret": "SBEijvWXDxq8F3WYdT5swudLO4Dy-Y5Xxul_BO-ti-5iYwRbgDKt2p59NcQSnZlcUnbxqVzDgtcucMLA3Q",
    "grant_type": "client_credentials"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    token = response.json().get("access_token")
    print(f"Access Token: {token}")
    
    # Активация кампании
    campaign_id = "10237777"
    url_activate = f"https://api-performance.ozon.ru/api/client/campaign/{campaign_id}/activate"
    headers_activate = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data_activate = {}

    response_activate = requests.post(url_activate, headers=headers_activate, data=json.dumps(data_activate))

    if response_activate.status_code == 200:
        campaign_info = response_activate.json()
        print("Campaign Activated:")
        print(json.dumps(campaign_info, indent=4))
    else:
        print(f"Failed to activate campaign: {response_activate.status_code}")
        print(response_activate.text)
else:
    print(f"Failed to get token: {response.status_code}")
    print(response.text)