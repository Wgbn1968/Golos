position = vc.getObject("evalvars","{var.Position}")

if position == "Map":
    mouseXY = vc.getObject("payloads","")
    X = int(mouseXY[2])
    Y = int(mouseXY[3])
    if 1779 <= X <= 1815 and 54 <= Y <= 90:
        vc.callAction("Hook.Disable","", None)
        vc.callAction("VC.Pause","300", None)
        vc.callAction("Results.SetVar","Position&&{var.tmpPosition}", None)
        position = vc.getObject("evalvars","{var.Position}")
        if position == "Commander":           
            Binoculars = vc.getObject("evalvars","{var.Binoculars}")
            vc.callAction("DxInput.KeyPress","F7", None)
            vc.callAction("VC.Pause","100", None)
            StateInCabin = vc.getObject("evalvars","{var.StateInCabin}")
            if StateInCabin == "Vysunut":
                vc.callAction("DxInput.KeyPress","Q", None)
                vc.callAction("VC.Pause","200", None)
                if Binoculars == "1":
                    vc.callAction("DxInput.KeyPress","N", None)
            elif StateInCabin == "Pohodnomy":
                vc.callAction("DxInput.KeyPress","Q", None)
                vc.callAction("VC.Pause","100", None)
                vc.callAction("DxInput.KeyPress","Q", None)
                vc.callAction("VC.Pause","200", None)
                if Binoculars == "1":
                    vc.callAction("DxInput.KeyPress","N", None)        
        vc.callAction("VC.Pause","500", None)
        vc.callAction("Mouse.MoveAbsolute","960,540", None)
        vc.callAction("VC.Pause","50", None)
        vc.callAction("DxInput.Mouse.Click","Left&&50", None)
        vc.callAction("VC.Pause","50", None)
        vc.callAction("Results.SetVar","cursor&&0", None)
        vc.callAction("Hook.Enable","", None)
        result = True
    else:
        result = False
else:
    result = True