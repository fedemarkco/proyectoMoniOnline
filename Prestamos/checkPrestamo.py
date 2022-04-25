import requests


def checkStatus(dni):
    url = "https://api.moni.com.ar/api/v4/scoring/pre-score/%s" % dni

    headers = {"credential": "ZGpzOTAzaWZuc2Zpb25kZnNubm5u"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
