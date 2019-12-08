state = vc.getObject("evalvars","{var.section}")
OnlineMode = vc.getObject("evalvars","{var.OnlineMode}")
statusPodavlenie = vc.getObject("evalvars","{var.Podavlenie12}")
	
if state == "GG" or state == "1G":
    Coord10 = "1679,1013"
    Coord12 = "0"
    section = "G"
    Coord1 = "1638,1044"
    Coord2 = "1666,1044"
    Coord3 = "1694,1044"
    Coord4 = "1722,1044"
    Return = "229"
elif state == "1G3":
    Coord10 = "1641,1013"
    Coord12 = "0"
    section = "G3"
    Coord1 = "1614,1044"
    Coord2 = "1642,1044"
    Coord4 = "1670,1044"
    Coord3 = "1722,1013"
    Return = "245"

if statusPodavlenie == "1":
    Return = int(Return) + 16
else:
    Return = int(Return)

if OnlineMode == "1":
    CoordReturn = int(Return) + 16
else:
    CoordReturn = int(Return)

vc.callAction("Mouse.MoveRelative","0,-%s"%CoordReturn, None)
vc.callAction("Results.SetVar","Coord10&&%s"%Coord10, None)
vc.callAction("Results.SetVar","Coord12&&%s"%Coord12, None)
vc.callAction("Results.SetVar","section&&%s"%section, None)
vc.callAction("Results.SetVar","Coord1&&%s"%Coord1, None)
vc.callAction("Results.SetVar","Coord2&&%s"%Coord2, None)
vc.callAction("Results.SetVar","Coord3&&%s"%Coord3, None)
vc.callAction("Results.SetVar","Coord4&&%s"%Coord4, None)