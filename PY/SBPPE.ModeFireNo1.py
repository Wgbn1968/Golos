state = vc.getObject("evalvars","{var.section}")
#ModeFire = vc.getObject("evalvars","{var.ModeFire1}")
OnlineMode = vc.getObject("evalvars","{var.OnlineMode}")
Podavlenie = vc.getObject("evalvars","{var.Podavlenie1}")

if state == "1G":
    Coord = "293"
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