import requests
import json
owner_log='ileonkina'
owner_pass='19tustuuira89'
host='https://api.github.com/'
org_name='TestInternOrg'
def del_from_org(user):
	reqq = 'orgs/%s/members/%s' % (org_name,user)
	url = host + reqq
	try:
		r = requests.delete(url,auth = (owner_log,owner_pass))
	except r.status_code != 200 or r.status_code != 204:
		return "Error "+ r.headers['status']
	else:
		return "Delete successful"

def add_to_team(user,team_id):
	reqq = 'teams/%s/members/%s' % (team_id,user)
	url = host + reqq
	try:
		r = requests.put(url,auth = (owner_log,owner_pass),data = '{"login":"%s"}' % user)
	except r.status_code != 200 or r.status_code != 204:
		return "Error "+ r.headers['status']
	else:
		return "%s was added to team" % user

def create_team(team_name,permission,repo_name):
	reqq = 'orgs/%s/teams' % org_name
	url = host + reqq
	try:
		r = requests.post(url,auth = (owner_log,owner_pass),data = '{"name":"%s", "repo_names":["%s/%s"], "permission":"%s"}' % (team_name,org_name,repo_name,permission))
	except r.status_code != 200 or r.status_code != 204:
		return "Error "+ r.headers['status']
	else:
		return "%s was created" % team_name

