import xml.etree.cElementTree as ET
import hashlib
import time

class ReqGet():
    def __init__(self, request):
        self.signature = request.args.get('signature')
        self.timestamp = request.args.get('timestamp')
        self.nonce = request.args.get('nonce')
        self.echostr = request.args.get('echostr')
        self.token = "aptx4869"

    def confirmToken(self):
        args_list = [self.token, self.timestamp, self.nonce]
        args_list.sort()
        sha1 = hashlib.sha1()
        retStr = ''.join(args_list)
        sha1.update(retStr.encode())
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            return echostr
        else:
            return ""


class ReqPost():
    def __init__(self, request):
        self.data = request.data

    def getMsg(self):
        root = ET.fromstring(self.data)
        msg = {}
        for child in root:
            msg[child.tag] = child.text
        return msg


class RepMsg():
    def __init__(self, msg):
        self.reqMsg = msg

    def makeRepXml(root, msg):
        rt = ET.Element(root)
        for tag in msg:
            child = ET.subElement(rt, tag)
            child.text = msg.tag
        repXML = ET.tostring(rt)

    def makeMsg(self):
        repMsg = {}
        repMsg.ToUserName = self.reqMsg.FromUserName
        repMsg.FromUserName = self.reqMsg.ToUserName
        repMsg.CreateTime = int(time.time)

 
