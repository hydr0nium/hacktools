
import requests
import bs4


BASE_URL = "https://gtfobins.github.io/gtfobins/"

def main(args, config):
	r = requests.get(BASE_URL + args.executable)
	parsed_html = bs4.BeautifulSoup(r.text, 'html.parser').get_text()
	if "Page not found" in parsed_html:
		print("Not executable found on GTFOBins with that name")
	else:
		print(parsed_html)
		title = args.executable
	
	
	