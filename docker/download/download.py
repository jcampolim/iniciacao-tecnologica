import gdown

output = 'app/inversores.xlsx'

url = "https://docs.google.com/spreadsheets/d/1PbLDQ6eU3djOkD9fCivWv2EEnrMYI9gJ/edit?usp=drive_link&ouid=102459930919522971975&rtpof=true&sd=true"
gdown.download(url=url, output=output, fuzzy=True)
