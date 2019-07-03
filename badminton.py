#-*- coding:utf-8 -*-
# Python 2.7
""" Add MY_NAME to the chat text from group chat with keywords and send back to the group chat
"""
import itchat
import time
MY_NAMES = [u'郭健', u'郭建', u'guojian']
MY_NAME = u'郭健'
keywords = [u'周二晚', u'活动地址', u'人员限制',u'1',u'2',u'3',u'4',u'5']
SECONDS_WAITING = 0.5 #  seconds waiting for
done_list = []


def add_myname(txt, num=6):
    ss = 1
    while ss < num:
        temp = txt[txt.find('\n%s' % ss) + 4:txt.find('\n%s' % (ss + 1))]
        if temp == u' ' or temp == u'':
            txt = txt[:txt.find('\n%s' % ss) + 4] + MY_NAME + \
                txt[txt.find('\n%s' % ss) + 4:]
            return txt
        else:
            ss = ss + 1
    if ss == num:
        temp = txt[txt.find('\n%s' % ss) + 4:]
        if temp == u' ' or temp == u'':
            txt = txt[:txt.find('\n%s' % ss) + 4] + MY_NAME + \
                txt[txt.find('\n%s' % ss) + 4:]
            return txt
    return None


@itchat.msg_register('Text', isGroupChat = True)
def text_reply(msg):
    if msg['FromUserName'] == FOX_USRNAME:
        txt = msg['Text']
        if msg['MsgId'] not in done_list:
            for word in keywords:
                if word not in txt:
                    return None
            for name in MY_NAMES:
                if name in txt:
                    return None
            new_txt = add_myname(txt)
            if new_txt is not None:
                time.sleep(SECONDS_WAITING)
                #import pdb;pdb.set_trace()
                msg.user.send(new_txt)
                done_list.append(msg['MsgId'])

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    names = itchat.get_friends(update=True)
    for name in names:
        if name['PYQuanPin'].startswith('fox'):
            FOX_USRNAME = name['UserName']
            break
    itchat.run()
