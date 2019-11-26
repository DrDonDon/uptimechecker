import requests

ad_url = "https://beta.amphoradata.com/healthz"



def get_isup():
    r = requests.get(ad_url)

    return (r.status_code == 200 and len(r.content) == 0)

if (get_isup()):
    print("It's up!")
else:
    print("It ain't up")
