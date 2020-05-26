# -*- coding: utf-8 -*-
from linepy import *
import time

c1 = LINE('mail','pass',appName="IOSIPAD\t9.15.1\tIOSIPAD\t13.2.2")
oepoll = OEPoll(c1)

c1.log("Auth Token : " + str(c1.authToken))

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops != None:
            for op in ops:
                if (op.type == 13):
                    c1.acceptGroupInvitation(op.param1)
                    
                    c1.sendMessage(op.param1,'Mirai canceller 何かあれば http://musicfun.chatx.whocares.jp へ')
                    c1.sendMessage(op.param1,'誰でも使えるので追加して下さい')
                    c1.sendMessage(op.param1,'3')
                    c1.sendMessage(op.param1,'2')
                    c1.sendMessage(op.param1,'1')
                if (op.type == 25):
                    msg = op.message
                    if (msg.text.lower() == 'キャンセル'):
                        s = time.time()
                        c1.sendMessage('Speed!')
                        e = time.time() - s
                        c1.sendMessage('{:.14f}'.format(e))
                    if ('1' in msg.text.lower()):
                        g = c1.getGroup(msg.to)
                        mids = [i.mid for i in g.invitee]
                        for mid in mids:
                            try:
                                c1.cancelGroupInvitation(msg.to,[mid])
                                time.sleep(0.5)
                            except Exception as e:
                                pass
                        c1.sendMessage(msg.to,'キャンセル終了')
                        c1.leaveGroup(msg.to)
                oepoll.setRevision(op.revision)
    except Exception as e:
        c1.log("[SINGLE_TRACE] ERROR : " + str(e))
