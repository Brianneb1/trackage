# Import the argparse library
import argparse
from functions import add_package, del_package, track_all, track_one

# Create the parser
parser = argparse.ArgumentParser(prog='trackage', description='Track your packages')

FUNCTION_MAP = {'add' : add_package,
                'delete' : del_package,
                'track_all' : track_all,
                'track_one' : track_one}

# Add the arguments
parser.add_argument('command', choices=FUNCTION_MAP.keys(), 
                        help='Enter one of the following commands: add (arguments: tracking_number, shipping_service), delete (arguments: tracking_number), track_all (arguments: none), track_one (arguments: tracking_number shipping_service')
# optional arguments depending on command
parser.add_argument('-tn',
                       metavar='tracking_number',
                       type=int,
                       help='The tracking number of package to be tracked')
parser.add_argument('-s',
                        metavar='shipping_service',
                        type=str,
                        help='The service shipping the package (usps, ups, fedex)')
parser.add_argument('-d',
                        metavar='description',
                        type=str,
                        help='A description of the package')

# Execute the parse_args() method
args = parser.parse_args()

# Execute correct function based on input command
func = FUNCTION_MAP[args.command]
if(func == add_package):
    if args.tn == None:
        print("Please include -tn tracking_number")
    if args.s == None:
        print("Please include -s shipping_service")
    if args.d == None:
        print("Please include -d description")
    if args.tn != None and args.s != None and args.d != None: 
        func(args.tn, args.s, args.d)
elif(func == del_package):
    if args.d == None:
        print("Please include -d description")
    else:
        func(args.d)
elif(func == track_all):
    func()
elif(func == track_one):
    if args.s == None:
        print("Please include -s shipping_service")
    else: 
        func(args.tn, args.s)

