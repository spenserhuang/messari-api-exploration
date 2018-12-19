# IMPORT LIBRARIES
import json
import csv
from six.moves import urllib


# CREATING LIST OF TICKERS
assets_url = f"https://data.messari.io/api/v1/assets"
assets_bytes = urllib.request.urlopen(assets_url).read()
assets_json = assets_bytes.decode('utf8').replace("'", '"')
assets_dict = json.loads(assets_json)

ticker_list = []

for asset in assets_dict["data"]:
    if (asset["symbol"] == "mkr") or (asset["symbol"] == "vet") or (asset["symbol"] == "ark") or (asset["symbol"] == "nxt") or (asset["symbol"] == "icn") or (asset["symbol"] == "dcn") or (asset["symbol"] == "gxs"):
        pass
    else:
        ticker_list.append(asset["symbol"])



# STORE METRICS & PROFILES FOR EACH TICKER
assets_details_list = []

for ticker in ticker_list:
    # ASSETS METRICS
    metrics_url = (f"https://data.messari.io/api/v1/assets/{ticker}/metrics")
    metrics_bytes = urllib.request.urlopen(metrics_url).read()
    metrics_json = metrics_bytes.decode('utf8')
    metrics_dict = json.loads(metrics_json)

    metrics_data = metrics_dict["data"]
    del metrics_data["symbol"]
    del metrics_data["market_data"]
    del metrics_data["blockchain_stats_last_24_hours"]

    # PROFILE METRICS
    profile_url = (f"https://data.messari.io/api/v1/assets/{ticker}/profile")
    profile_bytes = urllib.request.urlopen(profile_url).read()
    profile_json = profile_bytes.decode('utf8')
    profile_dict = json.loads(profile_json)

    profile_full_data = profile_dict["data"]
    profile_data = {}
    profile_data["token_distribution"] = profile_full_data["token_distribution"]
    del profile_data["token_distribution"]["description"]

    # COMBINING METRICS & PROFILE
    full_data = {}
    full_data["symbol"] = ticker
    full_data["metrics"] = metrics_data
    full_data["profile"] = profile_data
    assets_details_list.append(full_data)


# WRITE TO JSON
json = json.dumps(assets_details_list)
f = open("assets_info.json","w")
f.write(json)
f.close()
