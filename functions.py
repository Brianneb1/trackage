import urllib.request
import xml.etree.ElementTree as ET

# args: tracking_num
def usps(tracking_num):
    # verify with api
    strnum = str(tracking_num)
    requestXML = """
    <?xml verstion"1.0"?>
    <TrackRequest USERID="091NORTH7901">
        <TrackID ID="""+"\""+strnum+"\""+"""></TrackID>
    </TrackRequest>
    """
    docString = requestXML
    docString = docString.replace('\n', '').replace('\t','').replace('    ','')
    docString = urllib.parse.quote_plus(docString)

    url = "https://secure.shippingapis.com/ShippingAPI.dll?API=TrackV2&XML=" + docString
    # print(url + "\n\n")

    response = urllib.request.urlopen(url)
    if response.getcode() != 200:
        print("Error making HTTP call:")
        print(response.info())
        exit()

    contents = response.read()
    # print(contents) 

    root = ET.fromstring(contents) # look into this
    for trackid in root:
        print()
        print("" + trackid.find("TrackSummary").text)


# args: tracking_num
def ups(tracking_num):
    # verify with api

    # request status

    # print status
    return 0

# args: tracking_num
def fedex(tracking_num):
    # verify with api

    # request status

    # print status
    return 0

# args: tracking_num, service
def add_package(tracking_num, service):
    print("Adding a package. . .")
    # open .txt file

    # write tracking_num and service

    # save and close .txt file
    return 0

# args: tracking_num
def del_package(tracking_num):
    print("Deleting a package. . .")
    # open .txt file

    # find package

    # delete package

    # close .txt file
    return 0

# args: none
def track_all():
    print("Tracking all packages. . .")
    # open .txt file

    # read .txt file

    # call apis for each package and print status
    # for x in file:
    #     if(service == "usps"):
    #         usps(tracking_num)
    #     elif(service == "ups"):
    #         ups(tracking_num)
    #     elif(service == "fedex"):
    #         fedex(tracking_num)
    #     else:
    #         print("Error: Service not supported.")

    # close .txt file
    return 0

# args: tracking_num, service
def track_one(tracking_num, service):
    print("Tracking package. . .")
    # call api for package and print status
    if(service == "usps"):
        usps(tracking_num)
    elif(service == "ups"):
        ups(tracking_num)
    elif(service == "fedex"):
        fedex(tracking_num)
    else:
        print("Error: Service not supported.")
    return 0
