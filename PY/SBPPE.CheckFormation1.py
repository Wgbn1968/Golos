state = vc.getObject("evalvars","{var.section}") #Извлекаем состояние секции

if state == "G" or state == "GG" or state == "1G3" or state == "1G" or state == "1234":
    result = False #Значит что в строю
else:
    result = False #Значит что в строю