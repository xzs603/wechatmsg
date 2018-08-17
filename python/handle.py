# -*- coding: utf-8 -*-
# filename: handle.py
# update at 2018-08-17 22:25:41
import hashlib
import reply
import receive
import web

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "hahaha" #请按照公众平台官网\基本配置中信息填写
            print("handle/GET func: signature, timestamp, nonce: ", signature, timestamp, nonce)
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return echostr #此处本应返回空串，此处不做校验
        except Exception as e:
            print('Exception:', e)
			
    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)
            #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "你好"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print ("do nothing right now")
                return "success"
        except Exception as e:
            print('Exception:', e)