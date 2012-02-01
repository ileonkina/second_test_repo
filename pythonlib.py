import requests
import json
git_user = 'fakeuser'
git_pass = 'gfhjkm2012'
#r = requests.get('https://api.github.com/orgs/TestInternOrg',auth=(git_user,git_pass))
#print r.content
def delUserOrg(log,user_pass):
	try:
		r = requests.delete('https://api.github.com/orgs/TestInternOrg/members/'%log,auth=(git_user,git_pass))
		return r.content
	except:
		print "Error"
		return " "
	return " "

