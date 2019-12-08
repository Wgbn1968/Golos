state = vc.getObject("evalvars","{var.section}") #Извлекаем состояние секции

if state == "G" or state == "G3" or state == "G34" or state == "1G3" or state == "1234":
    result = True #Значит что не в строю
else:
    result = False #Значит что в строю