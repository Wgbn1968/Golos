position = vc.getObject("evalvars","{var.tmpPosition}")
StateInCabin = vc.getObject("evalvars","{var.StateInCabin}")
#1 - 1, 2 - 2, 3 - 3, 4 - 4, Карта - 5, Наводчик - 6, Командир - 7, Внешняя камера - 8, Мехвод - 9

if position == "1":
    result = 1
elif position == "2":
    result = 2
elif position == "3":
    result = 3
elif position == "4":
    result = 4
elif position == "Navodchik":
    vc.callAction("DxInput.KeyPress","F6", None)
    result = True
elif position == "Commander":
    vc.callAction("DxInput.KeyPress","F7", None)
    vc.callAction("VC.Pause","100", None) 
    if StateInCabin == "Vysunut":
        vc.callAction("DxInput.KeyPress","Q", None)
    elif StateInCabin == "Pohodnomy":
        vc.callAction("DxInput.KeyPress","Q", None)
        vc.callAction("VC.Pause","100", None)
        vc.callAction("DxInput.KeyPress","Q", None)
    result = True
elif position == "Vneshniy":
    vc.callAction("DxInput.KeyPress","F8", None)
    result = True
elif position == "Mehvod":
    vc.callAction("DxInput.KeyPress","F9", None)
    result = True
else:
    result = False