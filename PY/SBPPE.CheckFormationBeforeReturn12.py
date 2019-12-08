state = vc.getObject("evalvars","{var.section}") #Извлекаем состояние секции

if state == "GG" or state == "1G3" or state == "1G":
    result = False #значит что в строю
else:
    result = True #значит что не в строю