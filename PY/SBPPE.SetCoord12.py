state = vc.getObject("evalvars","{var.section}")
ModeFire12 = vc.getObject("evalvars","{var.ModeFire12}")
command = vc.getObject("evalvars","{var.CommandName}") #Извлекаем имя команды из переменной CommandName

if state == "G":
    Coord10 = "1628,1013"
    Coord12 = "1709,1013"
    section = "GG"
    Coord1 = "1614,1044"
    Coord3 = "1642,1044"
    Coord2 = "1695,1044"
    Coord4 = "1723,1044"
    vc.callAction("Results.SetVar","ModeFire12&&{var.ModeFire10}", None)
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
    vc.callAction("Results.SetVar","Podavlenie12&&0", None)

if command == "Подавить здесь" or command == "Занять оборону здесь" or command == "Атаковать":
    vc.callAction("Results.SetVar","ModeFire12&&1", None)
else:
    print('')