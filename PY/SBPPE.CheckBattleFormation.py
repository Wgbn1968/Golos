tempBattleFormation = vc.getObject("evalvars","{var.tempBattleFormation}")
#BattleFormation При назначении боевого порядка его значение записывается в эту переменную. 
#Колонна - 0, Линия - 1, Клин - 2, Угол назад - 3, Уступ влево - 4, Уступ вправо - 5, Ёлочка - 6

if tempBattleFormation == "1":
    vc.triggerEvent("BattleFormation1",None)
elif tempBattleFormation == "2":
    vc.triggerEvent("BattleFormation2",None)
elif tempBattleFormation == "3":
    vc.triggerEvent("BattleFormation3",None)
elif tempBattleFormation == "4":
    vc.triggerEvent("BattleFormation4",None)
elif tempBattleFormation == "5":
    vc.triggerEvent("BattleFormation5",None)
elif tempBattleFormation == "6":
    vc.triggerEvent("BattleFormation6",None)