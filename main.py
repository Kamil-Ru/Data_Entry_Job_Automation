from zillow import Zillow
from google_docs import Google_Docs

data_from_zillow = Zillow().get_data()

for i in data_from_zillow.values():
    google = Google_Docs()
    google.send_data(address=i['Address'], prize=i['Prize'], url=i['URL'])