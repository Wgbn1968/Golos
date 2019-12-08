OldDefaultX = int(vc.getObject("evalvars","{var.FSDefaultX}"))
OldDefaultY = int(vc.getObject("evalvars","{var.FSDefaultY}"))

LeftX = OldDefaultX - 217
RightX = OldDefaultX + 306
LeftY = OldDefaultY - 6
RightY = OldDefaultY + 7

mouseXY = vc.getObject("payloads","")

StartX = int(mouseXY[2])
StartY = int(mouseXY[3])

if LeftX <= StartX <= RightX and LeftY <= StartY <= RightY:
    MoveFireSupport = 1
    print "файл 1"
    print MoveFireSupport1
    print (LeftX,StartX,RightX)
    print (LeftY,StartY,RightY)
    print (OldDefaultX,OldDefaultY)
else:
    MoveFireSupport = 0
    print "файл 1"
    print MoveFireSupport0
    print (LeftX,StartX,RightX)
    print (LeftY,StartY,RightY)
    print (OldDefaultX,OldDefaultY)

vc.callAction("OSD.ShowText","начальная координата %s,%s"%(OldDefaultX,OldDefaultY), None)