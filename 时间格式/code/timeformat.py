# -*- coding:utf-8 -*-
import sys
from datetime import datetime
from workflow import Workflow

reload(sys)
sys.setdefaultencoding('utf-8')


def main(wf):
    now = datetime.now()
    format_arr = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d", "%m-%d %H:%M", "%H:%M:%S", "%H:%M"]

    for format in format_arr:
        result = now.strftime(format)

        wf.add_item(title=result,subtitle=format,icon='icon.png',arg=result,valid=True)
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))