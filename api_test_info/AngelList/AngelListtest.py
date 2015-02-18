import SecretKeys 
from angellist import AngelList
import sys

access_token = SecretKeys.token
print access_token



angelapi = AngelList(access_token)

results = angelapi.jobs({'method':'GET', 'query':'python'})

print results

# https://api.angelco/1/jobs