#server logic
from pprint import pprint
from twisted.application.internet import TCPServer
from twisted.application.service import Application
from twisted.web.resource import Resource
from twisted.web.server import Site

#business logic
import json
import base64

PORT = 8686


class FormPage(Resource):
    def render_GET(self, request):
        return ''

    def render_POST(self, request):
        newdata = request.content.getvalue()

        json_dict = json.loads(newdata)
        # Parse json dict
        if json_dict.has_key("img_raw") :
            img = open("img.jpg", "wb")
            img.write(base64.b64decode(json_dict["img_raw"]))
            img.close()
 
        print json_dict["img_raw"]
        return ''

root = Resource()
root.putChild("form", FormPage())
application = Application("Http Enpoint for App")
TCPServer(8000, Site(root)).setServiceParent(application)
