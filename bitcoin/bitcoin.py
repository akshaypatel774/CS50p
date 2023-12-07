import requests
import sys

try:
    n = float(sys.argv[1])

except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")

try:
    a = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    value = a.json()
    rate = float(value['bpi']['USD']['rate'].replace(',', ''))
    amount = rate*n
    print(f"${amount:,.4f}")
except requests.RequestException:
    pass