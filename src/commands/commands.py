import argparse


def parse_arguments():
	parser = argparse.ArgumentParser(prog="hacktools", usage="%(prog)s [command]")
	parser._positionals.title = "Available Commands"

	sub_parser = parser.add_subparsers(dest='command', required=True)
	sub_parser.metavar = ""
	init_install_parser(sub_parser)
	init_search_parser(sub_parser)
	init_tldr_parser(sub_parser)
	init_cve_parser(sub_parser)
	init_lol_parser(sub_parser)
	init_help_parser(sub_parser)
	return parser.parse_args()

def init_install_parser(sub_parser):
  install_parser = sub_parser.add_parser('install', help="Install a pentesting / hacking tool")
  return install_parser

def init_search_parser(sub_parser):
  search_parser = sub_parser.add_parser('search', help="Search-engine like hacking tool search")
  return search_parser

def init_tldr_parser(sub_parser):
  tldr_parser = sub_parser.add_parser('tldr', help="Get a short usage description of a tool")
  return tldr_parser

def init_lol_parser(sub_parser):
  lol_parser = sub_parser.add_parser('lol', help="Get a living of the land (lol) binary help")
  return lol_parser

def init_cve_parser(sub_parser):
  cve_parser = sub_parser.add_parser("cve", help="Get some information on the specific CVE")
  return cve_parser

def init_help_parser(sub_parser):
  help_parser = sub_parser.add_parser("help", help="Show help")
  return help_parser