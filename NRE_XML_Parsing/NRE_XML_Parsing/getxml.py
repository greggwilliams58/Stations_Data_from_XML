import requests


def getnrexml(userid,password):
    """
    This accesses the NR open data API to request a token and then request NRE station data.

    Parameters:
    userid:     an email of an account-holder the NR Open Data service
    password:   a password of an account holder of the NR Open Data service
    
    Returns
    xmldata:    a string containing the XML NRE Stations data.
    """

    print("getting the API token...\n")
    APItokenresponse = requesttoken(userid,password)
    APItoken = APItokenresponse.get("token")

    print("extracting the XML data now \n")
    xmldata = extractNREXML(userid,password,APItoken)
    return xmldata


def requesttoken(email,password):
    """
    This accesses the NR open data API to request a token

    Parameters:
    userid:             an email of an account-holder the NR Open Data service
    password:           a password of an account holder of the NR Open Data service
    
    Returns
    response.json() :    json formatted data, containing the required API token
    """

    url = ' https://opendata.nationalrail.co.uk/authenticate'
    payload = 'username='+email+'&password='+password
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False, timeout=3600)

    return response.json()


def extractNREXML(userid,password,APItoken):
    """
    This accesses the NR open data API to request a string containing the NRE Stations information in XML format.

    Parameters:
    userid:             a string containing an email of an account-holder the NR Open Data service
    password:           a string containing a password of an account holder of the NR Open Data service
    API Token           JSON-formatted data containing a required API token
    
    Returns
    response.text :     a string containing XML formatted data
    """


    url = 'https://opendata.nationalrail.co.uk/api/staticfeeds/4.0/stations'
    payload = userid +'&password=' + password
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Auth-Token': APItoken
}
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=3600)
    return response.text
