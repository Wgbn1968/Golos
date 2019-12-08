#197 Выдвигаться,выдвигайся
#181 Атаковать,атакуй
#165 Совершить марш,соверши марш
#149 Отойти,отойди
#133 Провести разведку,проведи разведку
#117 Проделать проход,проделай проход
#101 Прекратить подавление
#85  Подавить,подави

OnlineMode = vc.getObject("evalvars","{var.OnlineMode}")
statusPodavlenie = int(vc.getObject("evalvars","{var.Podavlenie{var.Name}}"))

coordCommand = vc.getObject("payloads","")
coordCommand = int(coordCommand[1])

if statusPodavlenie == 1 and coordCommand >= 117:
    coordCommand = coordCommand + 16
else:
    coordCommand = coordCommand

if OnlineMode == "1":
    result = coordCommand + 16
else:
    result = coordCommand