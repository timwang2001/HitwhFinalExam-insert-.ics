from ics import Calendar, Event
import re
<<<<<<< HEAD
# -*- coding: UTF-8 -*-
'''
这是我用一个python库写的
不知道为什么不好使 可能是编码问题吧
开发文档的sample放在这了
需要用的话 把main.py中的#AA.standardlized(classnum, totlist)取消注释就行
'''
=======
# 这是我直接饮用的一个Python库 据说能读写ics文件
# 反正我试了试是不好使的 是乱码..
# 开发文档的sample放在这了
>>>>>>> 09e918b2349c0d30888e0496a41cc46dbe551d8c

# c = Calendar()
# e1 = Event()
# e = Event()
# e.name = "My cool event1"
# e.begin = '2014-01-01 00:00:00'
# c.events.add(e)
# c.events
# e1.name = "My cool event2"
# e1.begin = '2014-01-02 00:00:00'
# c.events.add(e1)
# c.events
# # [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
# with open('my.ics', 'w') as my_file:
#     my_file.writelines(c)
# # and it's done !


def standardlized(path, k):
    c = Calendar()
    for r in k:
        e = Event()
        e.name = r[1]+'-'+r[3]
        clock = re.split('-', r[5])
        time = r[4]
        yy = r'[0-9]*年'
        mm = r'[0-9]*月'
        dd = r'[0-9]*日'
        y = re.findall(yy, time)[0][0:4]
        m = re.findall(mm, time)[0][0:2]
        d = re.findall(dd, time)[0][0:2]
        newdate = y+'-'+m+'-'+d+' '
        e.begin = newdate+clock[0]
        #e.end = newdate+clock[1]
        e.location = r[6]
        c.events.add(e)
        c.events
    with open(path+'a'+'.ics', 'w') as my_file:
        my_file.writelines(c)

# if __name__ == "__main__":
#     standardlized(1,)
