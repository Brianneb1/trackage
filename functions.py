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
        print("Status: " + trackid.find("TrackSummary").text)
        print()


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
def add_package(tracking_num, service, desc):
    print("Adding a package. . .")

    # open .txt file
    plist = open("tracking.txt", "a")

    # append tracking_num, service, and description
    line = str(tracking_num)+","+service+","+desc+"\n"
    plist.write(line)

    # save and close .txt file
    plist.close()
    print("Package added.")
    return 0

# args: description
def del_package(description):
    print("Deleting a package. . .")

    # open .txt file
    plist = open("tracking.txt", "r")

    # find package
    read_plist = []
    for x in plist:
        split_line = x.split(",")
        tn = split_line[0]
        service = split_line[1]
        desc = split_line[2].strip()
        read_plist.append([tn,service,desc])
    plist.close()

    # delete package
    new_plist = open("tracking.txt", "w")
    for item in read_plist:
        if item[2] != description:
            line = item[0]+","+item[1]+","+item[2]+"\n"
            new_plist.write(line)

    # close .txt file
    new_plist.close()
    print("Package deleted.")
    return 0

# args: none
def track_all():
    print("Tracking all packages. . .")
    print()

    # open .txt file
    plist = open("tracking.txt", "r")
    pdict = {}

    # read .txt file and create dict of packages {tn: service}
    for x in plist:
        split_line = x.split(",")
        tn = split_line[0]
        service = split_line[1]
        desc = split_line[2].strip()
        pdict[tn] = (service, desc)

    # call apis for each package and print status
    for tn, info in pdict.items():  
        print("Description:", info[1]) 
        if(info[0] == "usps"):
            usps(tn)
        elif(info[0] == "ups"):
            ups(tn)
        elif(info[0] == "fedex"):
            fedex(tn)
        else:
            print("Error: Service not supported.")

    # close .txt file
    plist.close()
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
