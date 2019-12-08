Position = vc.getObject("evalvars","{var.Position}")
#1 - 1, 2 - 2, 3 - 3, 4 - 4, Карта - 5, Наводчик - 6, Командир - 7, Внешняя камера - 8, Мехвод - 9

if Position == "Commander":
    if coordCommand >= 117:
        vc.callAction("Results.SetVar","cursor&&0", None)
        #vc.callAction("OSD.ShowText","курсор должен быть скрыт  (значение cursor = 0)", None)
        result = False
    else:
        vc.callAction("Hook.Disable","", None)
        vc.callAction("VC.Pause","300", None)
        vc.callAction("DxInput.Mouse.Click","Left&&50", None)
        vc.callAction("VC.Pause","50", None)
        vc.callAction("Results.SetVar","cursor&&0", None)
        #vc.callAction("OSD.ShowText","курсор должен быть скрыт  (значение cursor = 0)", None)
        vc.callAction("Hook.Enable","", None)
        result = True
else:
    vc.callAction("Hook.Disable","", None)
    vc.callAction("VC.Pause","300", None)
    vc.callAction("DxInput.Mouse.Click","Left&&50", None)
    vc.callAction("VC.Pause","50", None)
    vc.callAction("Results.SetVar","cursor&&0", None)
    #vc.callAction("OSD.ShowText","курсор должен быть скрыт  (значение cursor = 0)", None)
    vc.callAction("Hook.Enable","", None)
    result = True