import requests
import json
login = 'ileonkina'
passw = '19tustuuira89'
host = 'https://api.github.com/'
org_name = 'TestInternOrg'

def del_from_org(user):
	reqq = 'orgs/%s/members/%s' % (org_name,user)
	url = host + reqq
	r = requests.delete(url,auth = (login,passw))
	if r.status_code != 204:
		res = "Error "+ r.headers['status']
	else:
		res = "Delete successful"
	return res

def add_to_team(user,team_name):
	team_id = str(search_id_team(team_name))
	if team_id == "Team not found":
		return "Team not found"
	reqq = 'teams/%s/members/%s' % (team_id,user)
	url = host + reqq
	r = requests.put(url,auth = (login,passw),data = '{"login":"%s"}' % user)
	if r.status_code != 204:
		res = "Error "+ r.headers['status']
	else:
		res = "%s was added to team" % user
	return res

def search_id_team(team_name):
    reqq = 'orgs/%s/teams' % (org_name)
    url = host + reqq
    r = requests.get(url, auth = (login,passw))
    cont = json.loads(r.content)
    i = 0
    while 1:
        try:
            if cont[i]['name'] == team_name:
                break
            i += 1
        except IndexError:
            return "Team not found"
    return cont[i]['id'] 

def create_team(team_name,permission,repo_name):
	reqq = 'orgs/%s/teams' % org_name
	url = host + reqq
	r = requests.post(url,auth = (login,passw),data = '{"name":"%s", "repo_names":["%s/%s"], "permission":"%s"}' % (team_name,org_name,repo_name,permission))
	if r.status_code != 201:
		res = "Error "+ r.headers['status']
	else:
		res = "%s was created" % team_name
	return res

def create_repo(repo_name,descrip): #withot private
    #tmp=private
    #if (tmp<>"true"):
    # if (tmp<>"false"):
    # print "Second parametr could be 'true' or 'false'"
    # else:
    reqq='orgs/%s/repos' % (org_name)
    url = host + reqq
    r = requests.post(url, auth=(login,passw),data = '{"name":"%s","description":"%s"}' % (repo_name,descrip))
    if r.status_code == 201:
        res = "Done! Repo %s created" % repo_name
        # creating 3 teams
        create_team(repo_name,'pull',repo_name)
        create_team(repo_name+'-guests','push',repo_name)
        create_team(repo_name+'-owners','admin',repo_name)
  
    else:
        res = "Error "+ r.headers['status']
    return res
