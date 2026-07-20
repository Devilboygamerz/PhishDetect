import requests
import base64
import time

VT_URL = "https://www.virustotal.com/api/v3/urls"


def submit_url(url, api_key):
    headers = {
        "x-apikey": api_key
    }

    data = {
        "url": url
    }

    response = requests.post(VT_URL, headers=headers, data=data)

    if response.status_code != 200:
        raise Exception(f"VirusTotal Error: {response.status_code}")

    return response.json()["data"]["id"]


def get_report(url, api_key):
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")

    headers = {
        "x-apikey": api_key
    }

    response = requests.get(
        f"https://www.virustotal.com/api/v3/urls/{url_id}",
        headers=headers
    )

    if response.status_code != 200:
        raise Exception(f"VirusTotal Error: {response.status_code}")

    return response.json()
