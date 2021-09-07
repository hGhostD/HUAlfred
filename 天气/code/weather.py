# -*- coding:utf-8 -*-
import json,sys
from datetime import datetime
from workflow import Workflow, web

reload(sys)
sys.setdefaultencoding('utf-8')
# 和风天气 API_KEY
API_KEY = 'API_KEY'

def the_day(num):
    week = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    return week[num]

def main(wf):
    # geo 地理信息查询
    # https://geoapi.qweather.com/v2/city/lookup?location=shenyang&key=526909f489a8449080f460bd3d14ad2a

    query = '101070110' # 皇姑区
    url = 'https://devapi.qweather.com/v7/weather/now?location=' + query + '&key=' + API_KEY
    # params = {'location':query, 'key':API_KEY}
    #这里用了deanishe 的框架里面的web模块来请求页面,web模块类似requests库
    r = web.get(url=url)
    r.raise_for_status()
    resp = r.text
    data = json.loads(resp)

    tq = data['now']['text']
    wd = data['now']['temp']
    icon = data['now']['icon']
    title = tq + ' ' + wd + '℃'

    wf.add_item(title=title,subtitle=data['now']['obsTime'],icon='images/{}.png'.format(icon),arg=title,valid=True)
    # wf.add_item(title='1233214')

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))