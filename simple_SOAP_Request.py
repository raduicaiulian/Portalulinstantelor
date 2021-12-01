#!/usr/bin/python3

import requests
url="http://portalquery.just.ro/query.asmx"
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}
body = """
POST /query.asmx HTTP/1.1
Host: portalquery.just.ro
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "portalquery.just.ro/HelloWorld"

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <HelloWorld xmlns="portalquery.just.ro" />
  </soap:Body>
</soap:Envelope>
"""
response = requests.post(url,data=body,headers=headers)
print(response.content)
