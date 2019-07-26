from azure import cli
from azure.cli.core import get_default_cli
import sys

sys.sterr = sys.stdout
#az vm image accept-terms --urn paloaltonetworks:vmseries1:bundle1:8.1.0
get_default_cli().invoke(['vm', "image", "accept-terms", "--urn", "paloaltonetworks:vmseries1:bundle1:8.1.0"], out_file=sys.stdout)
get_default_cli().invoke(['vm', "image", "accept-terms", "--urn", "paloaltonetworks:vmseries1:bundle1:7.1.1"], out_file=sys.stdout)
get_default_cli().invoke(['vm', "image", "accept-terms", "--urn", "paloaltonetworks:vmseries1:bundle1:8.0.0"], out_file=sys.stdout)
get_default_cli().invoke(['vm', "image", "accept-terms", "--urn", "paloaltonetworks:vmseries1:bundle1:8.0.17"], out_file=sys.stdout)
get_default_cli().invoke(['vm', "image", "accept-terms", "--urn", "paloaltonetworks:vmseries1:bundle1:9.0.1"], out_file=sys.stdout)

