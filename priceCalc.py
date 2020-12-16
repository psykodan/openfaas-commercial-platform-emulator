import os
import time
import json
import requests
from requests.auth import HTTPBasicAuth

import platforms
platform1 = platforms.AWS()
platform2 = platforms.Google()
platform3 = platforms.Azure()
platform4 = platforms.IBM()

expression1 = "http://192.168.1.3:3000/api/datasources/proxy/1/api/v1/query_range?query=scalar(%20sum(%20gateway_function_invocation_total%20%7B%20%20code%3D%22200%22%7D%20))&start={0}&end={0}&step=1".format(int(time.time()))
expression2 = "http://192.168.1.3:3000/api/datasources/proxy/1/api/v1/query_range?query=scalar(%20sum(%20gateway_functions_seconds_sum%20))&start={0}&end={0}&step=1".format(int(time.time()))

res = requests.get(expression1,auth=HTTPBasicAuth('admin','admin'))
out = res.json()
request = int(out["data"]["result"][0]["values"][0][1])

res = requests.get(expression2,auth=HTTPBasicAuth('admin','admin'))
out = res.json()
time = float(out["data"]["result"][0]["values"][0][1])*1000

print(platform1.calculatePrice(request,time,128))
print(platform2.calculatePrice(request,time,128))
print(platform3.calculatePrice(request,time,128))
print(platform4.calculatePrice(request,time,128))
    

