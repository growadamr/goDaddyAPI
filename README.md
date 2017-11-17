
Only used in Ubuntu blend distros, but anything that can run 'dig +short' should be fine. 

For now best if run in a screen session and left alone, will be made into a service later.

domainName = 'YOUR_DOMAIN_NAME_HERE'

ssoKey = 'YOUR_SSO_KEY_FROM_GODADDY'

Change those values in the script. Runs every 60 minutes by default, but can be edited to whatever amount of time you need
in seconds on line 43.

No special requirements needed, built for Python 2.7, but you all know what you are doing to make it 3.X.
