state = vc.getObject("evalvars","{var.section}")
ModeFire = vc.getObject("evalvars","{var.ModeFire1}")
ModeFire12 = vc.getObject("evalvars","{var.ModeFire12}")
command = vc.getObject("evalvars","{var.CommandName}") #Извлекаем имя команды из переменной CommandName

if state == "G":
    Coord10 = "1627,1013"
    Coord12 = "1708,1013"
    section = "GG"
    Coord1 = "1614,1044"
    Coord3 = "1642,1044"
    Coord2 = "1695,1044"
    Coord4 = "1723,1044"
    vc.callAction("Results.SetVar","ModeFire12&&{var.ModeFire10}", None)
elif state == "GG":
    Coord10 = "0"
    Coord12 = "1655,1013"
    section = "1G3"
    Coord1 = "1587,1013"
    Coord2 = "1641,1044"
    Coord4 = "1669,1044"
    Coord3 = "1721,1013"
    vc.callAction("Results.SetVar","ModeFire1&&{var.ModeFire10}", None)
    vc.callAction("Results.SetVar","ModeFire3&&{var.ModeFire10}", None)
elif state == "G3":
    Coord10 = "0"
    Coord12 = "1655,1013"
    section = "1G3"
    Coord1 = "1587,1013"
    Coord2 = "1641,1044"
    Coord4 = "1669,1044"
    Coord3 = "1721,1013"
    vc.callAction("Results.SetVar","ModeFire1&&{var.ModeFire10}", None)
    vc.callAction("Results.SetVar","ModeFire12&&{var.ModeFire10}", None)
elif state == "G4":
    Coord10 = "1601,1013"
    Coord12 = "0"
    section = "G24"
    Coord1 = "1588,1044"
    Coord3 = "1616,1044"
    Coord2 = "1668,1013"
    Coord4 = "1721,1013"
    vc.callAction("Results.SetVar","ModeFire2&&{var.ModeFire10}", None)
elif state == "G34":
    Coord10 = "0"
    Coord12 = "0"
    section = "1234"
    Coord1 = "1564,1013"
    Coord2 = "1617,1013"
    Coord3 = "1670,1013"
    Coord4 = "1723,1013"
    vc.callAction("Results.SetVar","ModeFire1&&{var.ModeFire10}", None)
    vc.callAction("Results.SetVar","ModeFire2&&{var.ModeFire10}", None)
elif state == "G24":
    Coord10 = "0"
    Coord12 = "0"
    section = "1234"
    Coord1 = "1564,1013"
    Coord2 = "1617,1013"
    Coord3 = "1670,1013"
    Coord4 = "1723,1013"
    vc.callAction("Results.SetVar","ModeFire1&&{var.ModeFire10}", None)
    vc.callAction("Results.SetVar","ModeFire3&&{var.ModeFire10}", None)
else:
    print('')

vc.callAction("Results.SetVar","Coord10&&%s"%Coord10, None)
vc.callAction("Results.SetVar","Coord12&&%s"%Coord12, None)
vc.callAction("Results.SetVar","section&&%s"%section, None)
vc.callAction("Results.SetVar","Coord1&&%s"%Coord1, None)
vc.callAction("Results.SetVar","Coord2&&%s"%Coord2, None)
vc.callAction("Results.SetVar","Coord3&&%s"%Coord3, None)
vc.callAction("Results.SetVar","Coord4&&%s"%Coord4, None)

if command == "Подавить здесь":
    vc.callAction("Results.SetVar","Podavlenie12&&1", None)
else:
    vc.callAction("Results.SetVar","Podavlenie1&&0", None)

if command == "Подавить здесь" or command == "Занять оборону здесь" or command == "Атаковать":
    vc.callAction("Results.SetVar","ModeFire1&&1", None)
else:
    print('')