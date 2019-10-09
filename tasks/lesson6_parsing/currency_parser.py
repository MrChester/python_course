import requests
from bs4 import BeautifulSoup


def get_data(url):
    response = requests.get(url).json()
    current_date = response[0]["Date"].split("T")[0]
    result = []
    for i in response:
        if i["Cur_ID"] <= 170 and ["Cur_OfficialRate"]:
            currency_price = i["Cur_OfficialRate"]
            currency_price = "{} рублей за 1 {}".format(
                currency_price, i["Cur_Name"])
            result.append(currency_price)
    return "За {} курс {}".format(current_date, ", ".join(result))


def main():
    url = "http://nbrb.by/API/ExRates/Rates?Periodicity=0"
    print(get_data(url))


if __name__ == "__main__":
    main()
