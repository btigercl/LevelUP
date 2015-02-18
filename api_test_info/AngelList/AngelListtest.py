import os
from angellist import AngelList

access_token = os.environ.get("AngelList_Token")
angelapi = AngelList(access_token)

results = angelapi.jobs({'method':'GET'})

print results

# https://api.angelco/1/jobs