state = vc.getObject("evalvars","{var.section}")
#ModeFire = vc.getObject("evalvars","{var.ModeFire3}")
OnlineMode = vc.getObject("evalvars","{var.OnlineMode}")
Podavlenie = vc.getObject("evalvars","{var.Podavlenie3}")

if state == "G3":
    Coord = "293"
elif state == "G34":
    Coord = "309"
elif state == "1G3":
    Coord = "309"

if Podavlenie == "1":
    Coord = int(Coord) + 16
else:
    Coord = int(Coord)

if OnlineMode == "1":
    Coord = int(Coord) + 16
else:
    Coord = int(Coord)

vc.callAction("Mouse.MoveRelative","0,-%s"%Coord, None)