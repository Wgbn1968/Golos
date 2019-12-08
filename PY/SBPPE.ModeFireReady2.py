state = vc.getObject("evalvars","{var.section}")
ModeFire = vc.getObject("evalvars","{var.ModeFire2}")
OnlineMode = vc.getObject("evalvars","{var.OnlineMode}")
Podavlenie = vc.getObject("evalvars","{var.Podavlenie2}")

if state == "G2":
    if ModeFire == "0":
        Coord = "293"
    elif ModeFire == "2":
        Coord = "277"
elif state == "G24":
    if ModeFire == "0":
        Coord = "309"
    elif ModeFire == "2":
        Coord = "293"

if Podavlenie == "1":
    Coord = int(Coord) + 16
else:
    Coord = int(Coord)

if OnlineMode == "1":
    Coord = int(Coord) + 16
else:
    Coord = int(Coord)

vc.callAction("Mouse.MoveRelative","0,-%s"%Coord, None)