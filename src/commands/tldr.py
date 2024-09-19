import requests

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from argparse import Namespace

def main(args: 'Namespace', config):
	r = requests.get("https://cheat.sh/" + args.executable)
	print(r.content.decode())
	print("\n\033[31;1mDisclaimer: tldr function is a wrapper for cheat.sh. For more see https://github.com/chubin/cheat.sh")
	print("\033[31;1mTo get a better experience pipe the output to the 'more' or 'less -R' command\033[0m")
	print("\033[31;1mIf your output shows control characters try a '?T' behind your search e.g. 'find?T'\033[0m")