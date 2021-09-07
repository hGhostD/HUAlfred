# -*- coding: utf-8 -*-
import requests
# 使用和风天气 api 查询地区编码
API_KEY = '和风天气 API_KEY'
query = '沈阳'
url = 'https://api.qweather.com/v7/grid-weather/3d?'
params = {'location':query.encode('utf-8'),'key':API_KEY}
resp = requests.get(url)

print(resp)
print(resp.text)
