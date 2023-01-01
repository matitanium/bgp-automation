import requests , json
def convert(asn):
    url = f"https://api.bgpview.io/asn/{asn}/prefixes"
    data = requests.get(url).text
    jsonvar = json.loads(data)
    print(jsonvar["data"])

convert(46313)