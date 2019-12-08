import time

needNum = vc.getObject("payloads","")
needNum = int(needWeapons[0])
currentNum = int(vc.getObject("evalvars","{var.currentFSNum}"))

if currentNum > needNum:
    num = currentNum - needNum
    for i in range(0,num):
        vc.callAction("DxInput.KeyPress","Up", None)
        time.sleep(0.1)
else:
    num = needNum - currentNum
    for i in range(0,num):
        vc.callAction("DxInput.KeyPress","Down", None)
        time.sleep(0.1)