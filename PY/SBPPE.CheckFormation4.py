state = vc.getObject("evalvars","{var.section}") #Извлекаем состояние секции

if state == "G" or state == "G4" or state == "G34" or state == "G24" or state == "1234":
    result = True #Значит что не в строю
else:
    result = False #Значит что в строю