# Import the argparse library
import argparse

def add_package():
    return 0

def del_package():
    return 0

def track_all():
    return 0

def track_one():
    return 0

# Create the parser
parser = argparse.ArgumentParser(prog='trackage', description='Track your packages')

FUNCTION_MAP = {'add_package' : add_package,
                'delete_package' : del_package,
                'track_all' : track_all,
                'track_one' : track_one}

# Add the arguments
parser.add_argument('command', choices=FUNCTION_MAP.keys())
# optional arguments depending on command
parser.add_argument('tracking_number',
                       metavar='tracking_number',
                       type=int,
                       help='The tracking number of package to be tracked')
parser.add_argument('service',
                        metavar='shipping_service',
                        type=str,
                        help='The service shipping the package (USPS, UPS, FedEx)')

# Execute the parse_args() method
args = parser.parse_args()

# Execute correct function based on input command
func = FUNCTION_MAP[args.command]
func()

# Send request to API


# For testing
input = args.tracking_number
print(input)