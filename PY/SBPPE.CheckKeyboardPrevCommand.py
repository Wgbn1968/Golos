PrevCommand = vc.getObject("evalvars","{var.PrevCommand}")
CommandName = vc.getObject("evalvars","{var.CommandName}")

if PrevCommand == "1":
    if CommandName == "Подавить здесь" or CommandName == "Занять оборону здесь" or CommandName == "Наблюдать":
        result = True
    else:
        result = False
else:
    result = False