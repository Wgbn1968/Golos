#197 Выдвигаться,выдвигайся
#181 Атаковать,атакуй
#165 Совершить марш,соверши марш
#149 Отойти,отойди
#133 Провести разведку,проведи разведку
#117 Проделать проход,проделай проход
#101 Прекратить подавление
#85  Подавить,подави

statusPodavlenie = int(vc.getObject("evalvars","{var.Podavlenie{var.Name}}"))
print statusPodavlenie
SpokenCommand = vc.getObject("payloads","")
print SpokenCommand
SpokenCommand = int(SpokenCommand[0])
if statusPodavlenie == 1 and SpokenCommand >= 117:
    result = SpokenCommand + 16
    print 'подавление обнаружено и к координатам будет прибавлено 16 пикселей'
else:
    result = SpokenCommand
    print 'подавление не обнаружено - координата останется без изменений'