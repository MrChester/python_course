import requests

def get_money():
	url = "http://nbrb.by/API/ExRates/Rates?Periodicity=0"
	response = requests.get(url).json()

	for p in list(response):
		if p["Cur_ID"] == 145 and ["Cur_OfficialRate"]:
			usd_price = p["Cur_OfficialRate"]
			usd_price = "Today for 1 BYN %s USD"%(str(usd_price))
	return usd_price

print(get_money())