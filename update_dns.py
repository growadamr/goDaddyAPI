import requests, os, time, json

def doIT():
    while True:
        # Get current external IP
        try:
            mIP = os.popen('dig +short myip.opendns.com @resolver1.opendns.com')
            myExtIP = mIP.readline().strip()
            if myExtIP == '':
                print 'Unable to determine external IP, make sure that "myip.opendns.com" is reachable from your host'
                break
            print 'Current external IP is:', myExtIP
        except:
            print 'Unable to determine external IP, make sure that "myip.opendns.com" is reachable from your host'

        # Find what my domain IP DNS records are
        # Replace with your domain name as a string ex: 'google.com', 'speedtest.net', 'github.com'
        domainName = 'YOUR_DOMAIN_NAME_HERE'
        uri = 'https://api.godaddy.com/v1/domains/' +domainName +'/records/A'
        # Replace with your SSO key from Go Daddy as a string
        ssoKey = 'YOUR_SSO_KEY_FROM_GODADDY'
        headers = {'Authorization': 'sso-key '+ssoKey}
        gdAPI_call = requests.get(uri, headers=headers)
        gdAPI = json.loads(gdAPI_call.text)
        try:
            gdIP = gdAPI[0]['data']
            print 'Current A record IP is:', gdIP
        # Handles errors in SSO key and domain
        except:
            print 'Information not found at Go Daddy, are you sure your domain and sso key are set correctly?'
            break


        # Check if external and DNS IP are the same
        # If Current external and A records match, do nothing
        if myExtIP == gdIP:
            print 'Nothing to change' +'\n'
        # If they do not match, push the current IP to the API for change.
        else:
            print 'Changing', gdIP, 'to', myExtIP, 'at the Go Daddy API', '\n'
            result = requests.put(uri, headers=headers, json=[{"name": "@", "data": myExtIP, "ttl": 600}])
        # Change time value to how often you want it to run
        time.sleep(3600)
doIT()
