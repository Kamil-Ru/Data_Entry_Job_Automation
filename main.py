import pprint

from zillow import Zillow
from google_docs import Google_Docs

data_from_zillow = Zillow().get_data()

print(type(data_from_zillow))
google = Google_Docs()

for i in data_from_zillow.values():

    #google.send_data(address=i['Address'], prize=i['Prize'], url=i['URL'])


