# Import the argparse library
import argparse
from functions import add_package, del_package, track_all, track_one

# Create the parser
parser = argparse.ArgumentParser(prog='trackage', description='Track your packages')

FUNCTION_MAP = {'add_package' : add_package,
                'delete_package' : del_package,
                'track_all' : track_all,
                'track_one' : track_one}

# Add the arguments
parser.add_argument('command', choices=FUNCTION_MAP.keys(), 
                        help='Enter one of the following commands: /nadd_package (arguments: tracking_number, shipping_service) /ndelete_package (arguments: tracking_number)/ntrack_all (arguments: none)/ntrack_one (arguments: tracking_number shipping_service')
# optional arguments depending on command
parser.add_argument('tracking_number',
                       metavar='tracking_number',
                       type=int,
                       help='The tracking number of package to be tracked',
                       required=False)
parser.add_argument('service',
                        metavar='shipping_service',
                        type=str,
                        help='The service shipping the package (usps, ups, fedex)',
                        required=False)

# Execute the parse_args() method
args = parser.parse_args()

# Execute correct function based on input command
func = FUNCTION_MAP[args.command]
if(func == add_package):
    func(args.tracking_number, args.shipping_service)
elif(func == del_package):
    func(args.tracking_number)
elif(func == track_all):
    func()
elif(func == track_one):
    func(args.tracking_number, args.shipping_service)

# For testing
input = args.tracking_number
print(input)