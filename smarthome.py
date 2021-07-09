from werkzeug.datastructures import Headers
import pywemo
import requests as r


class Plug:
    def toggle():
        url = pywemo.setup_url_for_address("192.168.0.35", None)
        device = pywemo.discovery.device_from_description(url)
        device.toggle()


def Printer():
    api = "C24CD321248647459BD2116DB6C68CCB"
    # I dont care if you take this you would have to be on my local network to hit that so go for it
    # but also if you take it then turn my lights into a rainbow or something then Ill venmo you 5$
    url = "192.168.0.22"
    if r.get("http://192.168.0.22/api/server") == 200:
        data = r.get("http://192.168.0.22/api/server", headers={
            "X-Api-Key":   api
        })
        print(data.text)


# Printer()
