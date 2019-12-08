#state = vc.getObject("evalvars","{var.section}")
#ModeFire = vc.getObject("evalvars","{var.ModeFire12}")
OnlineMode = vc.getObject("evalvars","{var.OnlineMode}")
Podavlenie = vc.getObject("evalvars","{var.Podavlenie12}")
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