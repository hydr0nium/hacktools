from commands.commands import parse_arguments
from config import load_config
import commands.install
import commands.search
import commands.tldr
import commands.lol
import commands.cve
import commands.gtfo

parser = parse_arguments()
args = parser.parse_args()
config = load_config()

match args.command:
	case "install":
		commands.install.main(args, config)
	case "search":
		commands.search.main(args, config)
	case "tldr":
		commands.tldr.main(args, config)
	case "lol":
		commands.lol.main(args, config)
	case "gtfo":
		commands.gtfo.main(args, config)
	case "cve":
		commands.cve.main(args, config)
	case "help":
		parser.print_help()
	
  
	