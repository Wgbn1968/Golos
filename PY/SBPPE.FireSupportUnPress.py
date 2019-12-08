if MoveFireSupport == 1:
    mouseXY = vc.getObject("payloads","")
    EndX = int(mouseXY[2])
    EndY = int(mouseXY[3])
    if StartX >= EndX:
        NewDefaultX = OldDefaultX - (StartX - EndX)
    else:
        NewDefaultX = OldDefaultX + (EndX - StartX)
        
    if StartY >= EndY:
        NewDefaultY = OldDefaultY - (StartY - EndY)
    else:
        NewDefaultY = OldDefaultY + (EndY - StartY)
    vc.callAction("Results.SetVar","FSDefaultX&&%s"%NewDefaultX, None)
    vc.callAction("Results.SetVar","FSDefaultY&&%s"%NewDefaultY, None)    
    MoveFireSupport = 0
else:
    MoveFireSupport = 0

print "файл 2"
print MoveFireSupport
print (StartX,EndX)
print (StartY,EndY)
print (NewDefaultX,NewDefaultY)

vc.callAction("OSD.ShowText","конечная координата %s,%s"%(NewDefaultX,NewDefaultY), None)