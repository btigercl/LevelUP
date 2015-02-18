from .. import SecretKeys 
from angellist import AngelList

access_token = token
angelapi = AngelList(access_token)

results = angelapi.jobs({'method':'GET', 'query':'pyton'})

print results