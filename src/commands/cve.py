import requests
import re
import bs4

BASE_URL = "https://nvd.nist.gov/vuln/detail/"

def main(args, config):
	pattern = r"(?i)cve-\d\d\d\d-\d\d\d\d"
	if re.match(pattern=pattern, string=args.cve):
		r = requests.get(BASE_URL + args.cve)
		html = bs4.BeautifulSoup(r.text, 'html.parser')
		title = "\n\033[4m" + args.cve.upper() + ":\033[0m"
		description = html.find('p', {'data-testid': 'vuln-description'}).get_text()
		see_more = "\nSee more: " + BASE_URL + args.cve
		print(title)
		print(description)
		print(see_more)
	