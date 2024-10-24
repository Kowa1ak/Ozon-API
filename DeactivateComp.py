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
    
    # Список идентификаторов кампаний
    campaign_ids = [
        "12557394", "12557366", "12557376", "12557374", "12606843", "12557372",
        "12560909", "12561739", "12557390", "12560107", "12569835", "12569894",
        "12580074", "12580113", "12593472", "12593494", "12593520", "12593875",
        "12593902", "12594059", "12547533", "12550058", "12547161", "12550099",
        "12548593", "12585641", "12585656", "12585666", "12585675"
    ]
    
    # Деактивация кампаний
    for campaign_id in campaign_ids:
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
            print(f"Campaign {campaign_id} Deactivated:")
            print(json.dumps(campaign_info, indent=4))
        else:
            print(f"Failed to deactivate campaign {campaign_id}: {response_deactivate.status_code}")
            print(response_deactivate.text)
else:
    print(f"Failed to get token: {response.status_code}")
    print(response.text)