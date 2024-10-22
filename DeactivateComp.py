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
    
    # Деактивация кампании
    campaign_id = "10237777"
    url_deactivate = f"https://api-performance.ozon.ru/api/client/campaign/{campaign_id}/deactivate"
    headers_deactivate = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data_deactivate = {}

    response_deactivate = requests.post(url_deactivate, headers=headers_deactivate, data=json.dumps(data_deactivate))

    if response_deactivate.status_code == 200:
        campaign_info = response_deactivate.json()
        print("Campaign Deactivated:")
        print(json.dumps(campaign_info, indent=4))
    else:
        print(f"Failed to deactivate campaign: {response_deactivate.status_code}")
        print(response_deactivate.text)
else:
    print(f"Failed to get token: {response.status_code}")
    print(response.text)