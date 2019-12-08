state = vc.getObject("evalvars","{var.section}") #Извлекаем состояние секции

if state == "G" or state == "GG" or state == "G2" or state == "G4" or state == "1G" or state == "G24":
    result = True #значит что в строю
else:
    result = False #значит что не в строю