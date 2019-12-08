command = vc.getObject("evalvars","{var.CommandName}") #Извлекаем имя команды из переменной CommandName

if command == "Выдвигаться":
    vc.callAction("TTS.Speak","выдвигаюсь", None)
    result = True
elif command == "Атаковать":
    vc.callAction("TTS.Speak","атакую цель", None)
    result = True
elif command == "Совершить марш":
    vc.callAction("TTS.Speak","марш так марш", None)
    result = True
elif command == "Отойти":
    vc.callAction("TTS.Speak","отхожу к позиции", None)
    result = True
elif command == "Провести разведку":
    vc.callAction("TTS.Speak","иду в разведку", None)
    result = True
elif command == "Проделать проход":
    vc.callAction("TTS.Speak","иду напроход", None)
    result = True
elif command == "Подавить здесь":
    vc.callAction("TTS.Speak","подавляю врага", None)
    result = True
elif command == "Занять оборону здесь":
    vc.callAction("TTS.Speak","занимаю оборону", None)
    result = True
elif command == "Наблюдать":
    vc.callAction("TTS.Speak","наблюдаю", None)
    result = True
else:
    result = False