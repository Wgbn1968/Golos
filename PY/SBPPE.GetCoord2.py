state = vc.getObject("evalvars","{var.section}")
if state == "G":
  Group10 = "1628,1013"
  Group12 = "1709,1013"
  section = "GG"
  Coord1 = "1614,1044"
  Coord3 = "1642,1044"
  Coord2 = "1695,1044"
  Coord4 = "1723,1044"
if state == "G3":
  Group10 = "0"
  Group12 = "1655,1013"
  section = "1G3"
  Coord1 = "1587,1013"
  Coord2 = "1641,1044"
  Coord4 = "1669,1044"
  Coord3 = "1721,1013"
if state == "GG":
  Group10 = "1602,1013"
  Group12 = "0"
  section = "G24"
  Coord1 = "1588,1044"
  Coord3 = "1616,1044"
  Coord2 = "1668,1013"
  Coord4 = "1721,1013"
if state == "1G3":
  Group10 = "0"
  Group12 = "0"
  section = "1234"
  Coord1 = "1564,1013"
  Coord2 = "1617,1013"
  Coord3 = "1670,1013"
  Coord4 = "1723,1013"
if state == "G4":
  Group10 = "1602,1013"
  Group12 = "0"
  section = "G24"
  Coord1 = "1588,1044"
  Coord3 = "1616,1044"
  Coord2 = "1668,1013"
  Coord4 = "1721,1013"
if state == "G34":
  Group10 = "0"
  Group12 = "0"
  section = "1234"
  Coord1 = "1564,1013"
  Coord2 = "1617,1013"
  Coord3 = "1670,1013"
  Coord4 = "1723,1013"
vc.callAction("Results.SetVar","Group10&&%s"%Group10, None) 
vc.callAction("Results.SetVar","Group12&&%s"%Group12, None) 
vc.callAction("Results.SetVar","section&&%s"%section, None)
vc.callAction("Results.SetVar","Coord1&&%s"%Coord1, None) 
vc.callAction("Results.SetVar","Coord2&&%s"%Coord2, None) 
vc.callAction("Results.SetVar","Coord3&&%s"%Coord3, None) 
vc.callAction("Results.SetVar","Coord4&&%s"%Coord4, None) 
