section = vc.getObject("evalvars","{var.section}")
if section == "G":      #если секция не разделена, тоесть равна 0
    XY = "1665,1045"    #тогда у 12го вот эти координаты
    print(XY)
else:                   # иначе (если разделена)
    XY = "1708,1015"    #тогда у 12го вот эти координаты
    print(XY)
vc.callAction("Mouse.MoveAbsolute","%s"%XY, None)   #Перемещяем курсор по координатам