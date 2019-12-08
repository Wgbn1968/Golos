TypeAmmo = vc.getObject("evalvars","{var.TypeAmmo}") 
print TypeAmmo
#if TypeAmmo == "ОФ-РС" or TypeAmmo == "Кассетные-РС":
if TypeAmmo == "8" or TypeAmmo == "9":
    vc.callAction("Mouse.MoveRelative","0,109", None)
    vc.callAction("VC.Pause","50", None)
    vc.callAction("DxInput.Mouse.Click","Left&&50", None)
    vc.callAction("VC.Pause","50", None)
    vc.callAction("DxInput.Mouse.Click","Left&&50", None)
    vc.callAction("VC.Pause","50", None)
    vc.callAction("Mouse.MoveRelative","0,-109", None)
    result = True
else:
    vc.callAction("Mouse.MoveRelative","0,13", None)
    vc.callAction("VC.Pause","50", None)
    vc.callAction("DxInput.Mouse.Click","Left&&50", None)
    vc.callAction("VC.Pause","50", None)
    vc.callAction("DxInput.Mouse.Click","Left&&50", None)
    vc.callAction("VC.Pause","50", None)
    vc.callAction("Mouse.MoveRelative","0,-13", None)
    result = False