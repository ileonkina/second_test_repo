import requests
import json
#git_user = 'fakeuser'
#git_pass = 'gfhjkm2012'
r = requests.get('https://api.github.com/orgs/TestInternOrg', auth=('fakeuser','gfhjkm2012'))
print r.content

