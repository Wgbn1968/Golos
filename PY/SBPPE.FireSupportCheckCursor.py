import re

cursor = int(vc.getObject("evalvars","{var.cursor}"))
if cursor == 0:
    vc.callAction("Mouse.GetXY","", None)
    mouseXY = vc.getObject("LastResult","")
    mouseXY = re.search(r'(\d+),(\d+)', mouseXY)
    currentX = int(mouseXY.group(1))
    currentY = int(mouseXY.group(2))
    pointX = int(vc.getObject("evalvars","{var.FSDefaultX}"))
    pointY = int(vc.getObject("evalvars","{var.FSDefaultY}"))
    LeftX = pointX - 217
    RightX = pointX + 306
    LeftY = pointY - 6
    RightY = pointY + 330
    if LeftX <= currentX <= RightX and LeftY <= currentY <= RightY:
        #vc.callAction("Results.SetVar","cursor&&1", None)
        print "курсор виден"
        result = 1
    else:
        #vc.callAction("DxInput.Mouse.Click","Left", None)
        print "курсор виден"
        result = 0