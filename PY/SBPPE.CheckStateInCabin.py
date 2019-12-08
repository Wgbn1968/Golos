state = vc.getObject("evalvars","{var.StateInCabin}")

if state == "Vysunut":
    result = "Q"
elif state == "Boevomy":
    result = "B"
elif state == "Pohodnomy":
    result = "Q"
else:
    result = False