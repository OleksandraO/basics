import yaml

# variables
filepath1 = '../data/credentials.yml'

# functions/steps

with open(filepath1, "r") as stream:
    credentials = yaml.safe_load(stream)

print(credentials)
qa_uname1 = credentials['qa']['username']
qa_pword1 = credentials['qa']['password']
qa_uname2 = credentials['uat']['username']

qa_pword2 = credentials['qa']['password']
qa_uname3= credentials['qa']['username']
qa_pword3 = credentials['qa']['password']
uat_uname = credentials['uat']['username']
print('username for qa env', qa_uname1)
print('password for qa env', qa_pword1)

print('username for uat env', uat_uname)

# login_page.enter(qa_uname)
# login_page.enter(qa_pword)

