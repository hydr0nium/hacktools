import argparse


def parse_arguments():
  parser = argparse.ArgumentParser(prog="mimir", usage="%(prog)s [command]")
  parser._positionals.title = "Available Commands"

  sub_parser = parser.add_subparsers(dest='command', required=True)
  sub_parser.metavar = ""
  init_install_parser(sub_parser)
  init_search_parser(sub_parser)
  init_tldr_parser(sub_parser)
  init_cve_parser(sub_parser)
  init_lol_parser(sub_parser)
  init_gtfo_parser(sub_parser)
  init_help_parser(sub_parser)
  return parser

def init_install_parser(sub_parser: argparse._SubParsersAction):
  install_parser = sub_parser.add_parser('install', help="Install a pentesting / hacking tool")
  install_parser._positionals.title = 'Arguments'
  return install_parser

def init_search_parser(sub_parser):
  search_parser = sub_parser.add_parser('search', help="Search-engine like hacking tool search")
  search_parser._positionals.title = 'Arguments'
  return search_parser

def init_tldr_parser(sub_parser: argparse._SubParsersAction):
  tldr_parser = sub_parser.add_parser('tldr', help="Get a short usage description of a tool")
  tldr_parser._positionals.title = 'Arguments'
  tldr_parser.add_argument('executable', help='The binary / executable that you would like to know how to use')
  return tldr_parser

def init_lol_parser(sub_parser):
  lol_parser = sub_parser.add_parser('lol', help="Get living of the land (Windows) help")
  lol_parser._positionals.title = 'Arguments'
  return lol_parser

def init_gtfo_parser(sub_parser):
  gtfo_parser = sub_parser.add_parser('gtfo', help="Get living of the land (Linux) help")
  gtfo_parser._positionals.title = 'Arguments'
  gtfo_parser.add_argument('executable', help='The binary / executable that you would like to know how to abuse')
  return gtfo_parser

def init_cve_parser(sub_parser: argparse._SubParsersAction):
  cve_parser = sub_parser.add_parser("cve", help="Get some information on the specific CVE")
  cve_parser._positionals.title = 'Arguments'
  cve_parser.add_argument('cve', help='Get a short NVD description of the CVE', metavar='CVE-XXXX-XXXX')
  return cve_parser

def init_help_parser(sub_parser: argparse._SubParsersAction):
  help_parser = sub_parser.add_parser("help", help="Show help")
  help_parser._positionals.title = 'Arguments'
  return help_parser