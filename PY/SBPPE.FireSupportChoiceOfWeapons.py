import time

needWeapons = vc.getObject("payloads","")
needWeapons = int(needWeapons[0])
defaultWeapons = 6

if defaultWeapons >= needWeapons:
    x = defaultWeapons - needWeapons
    for i in range(0,x):
        vc.callAction("DxInput.KeyPress","Up", None)
        time.sleep(0.1)
else:
    x = needWeapons - defaultWeapons
    for i in range(0,x):
        vc.callAction("DxInput.KeyPress","Down", None)
        time.sleep(0.1)