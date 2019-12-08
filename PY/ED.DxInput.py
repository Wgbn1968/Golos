import os
import re
#import sys

ED_KeyName = vc.getObject("evalvars","{var.ED_KeyName}")
ED_KeyPriority = vc.getObject("evalvars","{var.ED_KeyPriority}")
ED_KeyHoldTime = vc.getObject("evalvars","{var.ED_KeyHoldTime}")

if ED_KeyHoldTime == "{PF.3}":
    ED_KeyHoldTime = 0
else:
    ED_KeyHoldTime = int(ED_KeyHoldTime)

startfile = os.path.expanduser('~\AppData\Local\Frontier Developments\Elite Dangerous\Options\Bindings\StartPreset.start') 
path_binds = os.path.expanduser('~\AppData\Local\Frontier Developments\Elite Dangerous\Options\Bindings') 
logfile = open(startfile,'r')
binds_file = logfile.read()
logfile.close()
#print binds_file

bind_file = ("%s\%s.3.0.binds"%(path_binds,binds_file))

""" #начало комментария
#ED_KeyName = "UpThrustButton_Landing"
bind_file = ("D:\Custom.3.0EN.binds")
""" #конец комментария

logfile = open(bind_file,'r')
s = logfile.read()
try:
	s=s.decode('utf-8')
except:
	pass
logfile.close()
print bind_file
s = re.sub('\s*', '', s.strip())
#s = re.sub('/', '', s.strip())
#ED_KeyName = "PhotoCameraToggle_Buggy"
#print ED_KeyName
s = re.search(r'(<%s>(.*?)</%s>)'%(ED_KeyName,ED_KeyName), s)
s = s.group(1)
#print s
#vc.callAction("System.SetClipboardText","%s"%s, None)
if ED_KeyPriority == 'Secondary':
    print 'начинаем проверку клавиши мыши вторичного устройства без модификаторов'
    mySecondaryDeviceType_no_ModifierMouse = re.search(r'<%s>.*<SecondaryDevice="Mouse"Key="(\w+)"/></%s>'%(ED_KeyName,ED_KeyName), s)
    if not mySecondaryDeviceType_no_ModifierMouse:#если клавиши мыши вторичного устройства без модификаторов не существует
        print 'начинаем проверку клавиши вторичного устройства без модификаторов'
        mySecondaryDeviceType_no_Modifier = re.search(r'<%s>.*<SecondaryDevice="Keyboard"Key="Key_(\w+)"/></%s>'%(ED_KeyName,ED_KeyName), s)
        if not mySecondaryDeviceType_no_Modifier:#если клавиши вторичного устройства без модификаторов не существует
            print 'начинаем проверку клавиш вторичного устройства с 1 модификатором'
            mySecondaryDeviceType_with_1_Modifiers = re.search(r'<%s>.*<SecondaryDevice="Keyboard"Key="Key_(\w+)"><ModifierDevice="Keyboard"Key="Key_(\w+)"/>.*</%s>'%(ED_KeyName,ED_KeyName), s)
            if not mySecondaryDeviceType_with_1_Modifiers:#если клавиши вторичного устройства с  модификатором не существует
                print 'начинаем проверку клавиш вторичного устройства с 2 модификаторами'
                mySecondaryDeviceType_with_2_Modifiers = re.search(r'<%s>.*<SecondaryDevice="Keyboard"Key="Key_(\w+)"><ModifierDevice="Keyboard"Key="Key_(\w+)"/><ModifierDevice="Keyboard"Key="Key_(\w+)"/>.*</%s>'%(ED_KeyName,ED_KeyName), s)
                if not mySecondaryDeviceType_with_2_Modifiers:#если клавиши вторичного устройства с 2 модификаторами не существует
                    print 'начинаем проверку клавиш вторичного устройства с 3 модификаторами'
                    mySecondaryDeviceType_with_3_Modifiers = re.search(r'<%s>.*<SecondaryDevice="Keyboard"Key="Key_(\w+)"><ModifierDevice="Keyboard"Key="Key_(\w+)"/><ModifierDevice="Keyboard"Key="Key_(\w+)"/><ModifierDevice="Keyboard"Key="Key_(\w+)"/>.*</%s>'%(ED_KeyName,ED_KeyName), s)
                    if not mySecondaryDeviceType_with_3_Modifiers:#если клавиши вторичного устройства с 3 модификаторами не существует
                        print 'начинаем проверку клавиши мыши первичного устройства без модификаторов'
                        myPrimaryDeviceType_no_ModifierMouse  = re.search(r'<%s><PrimaryDevice="Mouse"Key="(\w+)"/><SecondaryDevice.*</%s>'%(ED_KeyName,ED_KeyName), s)
                        if not myPrimaryDeviceType_no_ModifierMouse :#если клавиши мыши вторичного устройства без модификаторов не существует
                            print 'начинаем проверку клавиши первичного устройства без модификаторов'
                            myPrimaryDeviceType_no_Modifier = re.search(r'<%s><PrimaryDevice="Keyboard"Key="Key_(\w+)"/><SecondaryDevice.*</%s>'%(ED_KeyName,ED_KeyName), s)
                            if not myPrimaryDeviceType_no_Modifier:#если клавиши вторичного устройства без модификаторов не существует
                                print 'начинаем проверку клавиш первичного устройства с 1 модификатором'
                                myPrimaryDeviceType_with_1_Modifiers = re.search(r'<%s><PrimaryDevice="Keyboard"Key="Key_(\w+)"><ModifierDevice="Keyboard"Key="Key_(\w+)"/></Primary>.*</%s>'%(ED_KeyName,ED_KeyName), s)
                                if not myPrimaryDeviceType_with_1_Modifiers:#если клавиши первичного устройства с 1 модификатором не существует
                                    print 'начинаем проверку клавиш первичного устройства с 2 модификаторами'
                                    myPrimaryDeviceType_with_2_Modifiers = re.search(r'<%s><PrimaryDevice="Keyboard"Key="Key_(\w+)"><ModifierDevice="Keyboard"Key="Key_(\w+)"/><ModifierDevice="Keyboard"Key="Key_(\w+)"/></Primary>.*</%s>'%(ED_KeyName,ED_KeyName), s)
                                    if not myPrimaryDeviceType_with_2_Modifiers:#если клавиши первичного устройства с 2 модификаторами не существует
                                        print 'начинаем проверку клавиш первичного устройства с 3 модификаторами'
                                        myPrimaryDeviceType_with_3_Modifiers = re.search(r'<%s><PrimaryDevice="Keyboard"Key="Key_(\w+)"><ModifierDevice="Keyboard"Key="Key_(\w+)"/><ModifierDevice="Keyboard"Key="Key_(\w+)"/><ModifierDevice="Keyboard"Key="Key_(\w+)"/></Primary>.*</%s>'%(ED_KeyName,ED_KeyName), s)
                                        if not myPrimaryDeviceType_with_3_Modifiers:#если клавиши первичного устройства с 3 модификаторами не существует
                                            print 'клавиша первичного устройства с 3 модификаторами не обнаружена'
                                            result = "NoKey"
                                            #vc.callAction("TTS.Speak","Комбинация клавиш на первичном устройстве отсутствует или не соответствует", None)
                                        else:#иначе нажмию клавиши первичного устройства с 3 модификатором
                                            print 'клавиша первичного устройства с 3 модификаторами обнаружена'
                                            print 'нажимаю клавишу первичного устройства с 3 модификаторами'
                                            NumKeys_with_Modifiers = 3
                                            myMainDeviceKey = myPrimaryDeviceType_with_3_Modifiers.group(1)#клавиша первичного устройства без модификаторов
                                            myModifier1Key = myPrimaryDeviceType_with_3_Modifiers.group(2)#клавиша модификатора 1
                                            myModifier2Key = myPrimaryDeviceType_with_3_Modifiers.group(3)#клавиша модификатора 2
                                            myModifier3Key = myPrimaryDeviceType_with_3_Modifiers.group(4)#клавиша модификатора 3
                                            vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                                            vc.callAction("DxInput.KeyDown","%s"%myModifier1Key, None)
                                            vc.callAction("DxInput.KeyDown","%s"%myModifier2Key, None)
                                            vc.callAction("DxInput.KeyDown","%s"%myModifier3Key, None)
                                            if ED_KeyHoldTime > 0:
                                                print 'тут нажимаем клавишу на n мс'
                                                vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                                            else:
                                                print ('тут нажимаем простую клавишу без удержания')
                                                vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
                                            vc.callAction("DxInput.KeyUp","%s"%myModifier3Key, None)
                                            vc.callAction("DxInput.KeyUp","%s"%myModifier2Key, None)
                                            vc.callAction("DxInput.KeyUp","%s"%myModifier1Key, None)
                                    else:#иначе нажмию клавиши первичного устройства с 2 модификатором
                                        print 'клавиша первичного устройства с 2 модификаторами обнаружена'
                                        print 'нажимаю клавишу первичного устройства с 2 модификаторами'
                                        NumKeys_with_Modifiers = 2
                                        myMainDeviceKey = myPrimaryDeviceType_with_2_Modifiers.group(1)#клавиша первичного устройства без модификаторов
                                        myModifier1Key = myPrimaryDeviceType_with_2_Modifiers.group(2)#клавиша модификатора 1
                                        myModifier2Key = myPrimaryDeviceType_with_2_Modifiers.group(3)#клавиша модификатора 2
                                        vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                                        vc.callAction("DxInput.KeyDown","%s"%myModifier1Key, None)
                                        vc.callAction("DxInput.KeyDown","%s"%myModifier2Key, None)
                                        if ED_KeyHoldTime > 0:
                                            print 'тут нажимаем клавишу на n мс'
                                            vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                                        else:
                                            print ('тут нажимаем простую клавишу без удержания')
                                            vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
                                        vc.callAction("DxInput.KeyUp","%s"%myModifier2Key, None)
                                        vc.callAction("DxInput.KeyUp","%s"%myModifier1Key, None)
                                else:#иначе нажмию клавиши первичного устройства с 1 модификатором
                                    print 'клавиша первичного устройства с 1 модификатором обнаружена'
                                    print 'нажимаю клавишу первичного устройства с 1 модификатором'
                                    NumKeys_with_Modifiers = 1
                                    myMainDeviceKey = myPrimaryDeviceType_with_1_Modifiers.group(1)#клавиша первичного устройства без модификаторов
                                    myModifier1Key = myPrimaryDeviceType_with_1_Modifiers.group(2)#клавиша модификатора 1
                                    vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                                    vc.callAction("DxInput.KeyDown","%s"%myModifier1Key, None)
                                    if ED_KeyHoldTime > 0:
                                        print 'тут нажимаем клавишу на n мс'
                                        vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                                    else:
                                        print ('тут нажимаем простую клавишу без удержания')
                                        vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
                                    vc.callAction("DxInput.KeyUp","%s"%myModifier1Key, None)
                            else:#иначе нажмию клавиши первичного устройства без модификаторов
                                print 'клавиша первичного устройства без модификаторов обнаружены'
                                print 'нажимаю клавишу первичного устройства без модификаторов'
                                NumKeys_with_Modifiers = 0
                                myMainDeviceKey = myPrimaryDeviceType_no_Modifier.group(1)#клавиша первичного устройства без модификаторов
                                vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                                if ED_KeyHoldTime > 0:
                                    print 'тут нажимаем клавишу на n мс'
                                    vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                                else:
                                    print ('тут нажимаем простую клавишу без удержания')
                                    vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
                        else:#иначе нажмию клавиши мыши первичного устройства без модификаторов
                            print 'клавиша мыши первичного устройства без модификаторов обнаружены'
                            print 'нажимаю клавишу мыши первичного устройства без модификаторов'
                            NumKeys_with_Modifiers = 0
                            myMainDeviceKey = myPrimaryDeviceType_no_ModifierMouse.group(1)#клавиша первичного устройства без модификаторов
                            vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                            if ED_KeyHoldTime > 0:
                                print 'тут нажимаем клавишу на n мс'
                                vc.callAction("DxInput.Mouse.Click","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                            else:
                                print ('тут нажимаем простую клавишу без удержания')
                                vc.callAction("DxInput.Mouse.Click","%s"%myMainDeviceKey, None)
                    else:#иначе нажмию клавиши вторичного устройства с 3 модификатором
                        print 'клавиша вторичного устройства с 3 модификаторами обнаружена'
                        print 'нажимаю клавишу вторичного устройства с 3 модификаторами'
                        NumKeys_with_Modifiers = 3
                        myMainDeviceKey = mySecondaryDeviceType_with_3_Modifiers.group(1)#клавиша вторичного устройства без модификаторов
                        myModifier1Key = mySecondaryDeviceType_with_3_Modifiers.group(2)#клавиша модификатора 1
                        myModifier2Key = mySecondaryDeviceType_with_3_Modifiers.group(3)#клавиша модификатора 2
                        myModifier3Key = mySecondaryDeviceType_with_3_Modifiers.group(4)#клавиша модификатора 3
                        vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                        vc.callAction("DxInput.KeyDown","%s"%myModifier1Key, None)
                        vc.callAction("DxInput.KeyDown","%s"%myModifier2Key, None)
                        vc.callAction("DxInput.KeyDown","%s"%myModifier3Key, None)
                        if ED_KeyHoldTime > 0:
                            print 'тут нажимаем клавишу на n мс'
                            vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                        else:
                            print ('тут нажимаем простую клавишу без удержания')
                            vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
                        vc.callAction("DxInput.KeyUp","%s"%myModifier3Key, None)
                        vc.callAction("DxInput.KeyUp","%s"%myModifier2Key, None)
                        vc.callAction("DxInput.KeyUp","%s"%myModifier1Key, None)
                else:#иначе нажмию клавиши вторичного устройства с 2 модификатором
                    print 'клавиша вторичного устройства с 2 модификаторами обнаружена'
                    print 'нажимаю клавишу вторичного устройства с 2 модификаторами'
                    NumKeys_with_Modifiers = 2
                    myMainDeviceKey = mySecondaryDeviceType_with_2_Modifiers.group(1)#клавиша вторичного устройства без модификаторов
                    myModifier1Key = mySecondaryDeviceType_with_2_Modifiers.group(2)#клавиша модификатора 1
                    myModifier2Key = mySecondaryDeviceType_with_2_Modifiers.group(3)#клавиша модификатора 2
                    vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                    vc.callAction("DxInput.KeyDown","%s"%myModifier1Key, None)
                    vc.callAction("DxInput.KeyDown","%s"%myModifier2Key, None)
                    if ED_KeyHoldTime > 0:
                        print 'тут нажимаем клавишу на n мс'
                        vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                    else:
                        print ('тут нажимаем простую клавишу без удержания')
                        vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
                    vc.callAction("DxInput.KeyUp","%s"%myModifier2Key, None)
                    vc.callAction("DxInput.KeyUp","%s"%myModifier1Key, None)
            else:#иначе нажмию клавиши вторичного устройства с 1 модификатором
                print 'клавиша вторичного устройства с 1 модификатором обнаружены'
                print 'нажимаю клавишу вторичного устройства с 1 модификатором'
                NumKeys_with_Modifiers = 1
                myMainDeviceKey = mySecondaryDeviceType_with_1_Modifiers.group(1)#клавиша вторичного устройства без модификаторов
                myModifier1Key = mySecondaryDeviceType_with_1_Modifiers.group(2)#клавиша модификатора 1
                vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                vc.callAction("DxInput.KeyDown","%s"%myModifier1Key, None)
                if ED_KeyHoldTime > 0:
                    print 'тут нажимаем клавишу на n мс'
                    vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                else:
                    print ('тут нажимаем простую клавишу без удержания')
                    vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
                vc.callAction("DxInput.KeyUp","%s"%myModifier1Key, None)
        else:#иначе нажмию клавиши вторичного устройства без модификаторов
            print 'клавиша вторичного устройства без модификаторов обнаружена'
            print 'нажимаю клавишу вторичного устройства без модификаторов'
            NumKeys_with_Modifiers = 0
            myMainDeviceKey = mySecondaryDeviceType_no_Modifier.group(1)#клавиша вторичного устройства без модификаторов
            vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
            if ED_KeyHoldTime > 0:
                print 'тут нажимаем клавишу на n мс'
                vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
            else:
                print ('тут нажимаем простую клавишу без удержания')
                vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
    else:#иначе нажмию клавишу мыши вторичного устройства без модификаторов
        print 'клавиша мыши вторичного устройства без модификаторов обнаружена'
        print 'нажимаю клавишу мыши вторичного устройства без модификаторов'
        NumKeys_with_Modifiers = 0
        myMainDeviceKey = mySecondaryDeviceType_no_ModifierMouse.group(1)#клавиша мыши вторичного устройства без модификаторов
        vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
        if ED_KeyHoldTime > 0:
            print 'тут нажимаем клавишу на n мс'
            vc.callAction("DxInput.Mouse.Click","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
        else:
            print ('тут нажимаем простую клавишу без удержания')
            vc.callAction("DxInput.Mouse.Click","%s&&"%myMainDeviceKey, None)
else:
    print 'начинаем проверку клавиши мыши первичного устройства без модификаторов'
    myPrimaryDeviceType_no_ModifierMouse  = re.search(r'<%s><PrimaryDevice="Mouse"Key="(\w+)"/><SecondaryDevice.*</%s>'%(ED_KeyName,ED_KeyName), s)
    if not myPrimaryDeviceType_no_ModifierMouse :#если клавиши мыши первичного устройства без модификаторов не существует
        print 'начинаем проверку клавиши первичного устройства без модификаторов'
        myPrimaryDeviceType_no_Modifier = re.search(r'<%s><PrimaryDevice="Keyboard"Key="Key_(\w+)"/><SecondaryDevice.*</%s>'%(ED_KeyName,ED_KeyName), s)
        if not myPrimaryDeviceType_no_Modifier:#если клавиши первичного устройства без модификаторов не существует
            print 'начинаем проверку клавиш первичного устройства с 1 модификатором'
            myPrimaryDeviceType_with_1_Modifiers = re.search(r'<%s><PrimaryDevice="Keyboard"Key="Key_(\w+)"><ModifierDevice="Keyboard"Key="Key_(\w+)"/></Primary>.*</%s>'%(ED_KeyName,ED_KeyName), s)
            if not myPrimaryDeviceType_with_1_Modifiers:#если клавиши первичного устройства с 1 модификатором не существует
                print 'начинаем проверку клавиш первичного устройства с 2 модификаторами'
                myPrimaryDeviceType_with_2_Modifiers = re.search(r'<%s><PrimaryDevice="Keyboard"Key="Key_(\w+)"><ModifierDevice="Keyboard"Key="Key_(\w+)"/><ModifierDevice="Keyboard"Key="Key_(\w+)"/></Primary>.*</%s>'%(ED_KeyName,ED_KeyName), s)
                if not myPrimaryDeviceType_with_2_Modifiers:#если клавиши первичного устройства с 2 модификаторами не существует
                    print 'начинаем проверку клавиш первичного устройства с 3 модификаторами'
                    myPrimaryDeviceType_with_3_Modifiers = re.search(r'<%s><PrimaryDevice="Keyboard"Key="Key_(\w+)"><ModifierDevice="Keyboard"Key="Key_(\w+)"/><ModifierDevice="Keyboard"Key="Key_(\w+)"/><ModifierDevice="Keyboard"Key="Key_(\w+)"/></Primary>.*</%s>'%(ED_KeyName,ED_KeyName), s)
                    if not myPrimaryDeviceType_with_3_Modifiers:#если клавиши первичного устройства с 3 модификаторами не существует
                        print 'начинаем проверку клавиши мыши вторичного устройства без модификаторов'
                        mySecondaryDeviceType_no_ModifierMouse = re.search(r'<%s>.*<SecondaryDevice="Mouse"Key="(\w+)"/></%s>'%(ED_KeyName,ED_KeyName), s)
                        if not mySecondaryDeviceType_no_ModifierMouse:#если клавиши мыши вторичного устройства без модификаторов не существует
                            print 'начинаем проверку клавиши вторичного устройства без модификаторов'
                            mySecondaryDeviceType_no_Modifier = re.search(r'<%s>.*<SecondaryDevice="Keyboard"Key="Key_(\w+)"/></%s>'%(ED_KeyName,ED_KeyName), s)
                            if not mySecondaryDeviceType_no_Modifier:#если клавиши вторичного устройства без модификаторов не существует
                                print 'начинаем проверку клавиш вторичного устройства с 1 модификатором'
                                mySecondaryDeviceType_with_1_Modifiers = re.search(r'<%s>.*<SecondaryDevice="Keyboard"Key="Key_(\w+)"><ModifierDevice="Keyboard"Key="Key_(\w+)"/>.*</%s>'%(ED_KeyName,ED_KeyName), s)
                                if not mySecondaryDeviceType_with_1_Modifiers:#если клавиши вторичного устройства с  модификатором не существует
                                    print 'начинаем проверку клавиш вторичного устройства с 2 модификаторами'
                                    mySecondaryDeviceType_with_2_Modifiers = re.search(r'<%s>.*<SecondaryDevice="Keyboard"Key="Key_(\w+)"><ModifierDevice="Keyboard"Key="Key_(\w+)"/><ModifierDevice="Keyboard"Key="Key_(\w+)"/>.*</%s>'%(ED_KeyName,ED_KeyName), s)
                                    if not mySecondaryDeviceType_with_2_Modifiers:#если клавиши вторичного устройства с 2 модификаторами не существует
                                        print 'начинаем проверку клавиш вторичного устройства с 3 модификаторами'
                                        mySecondaryDeviceType_with_3_Modifiers = re.search(r'<%s>.*<SecondaryDevice="Keyboard"Key="Key_(\w+)"><ModifierDevice="Keyboard"Key="Key_(\w+)"/><ModifierDevice="Keyboard"Key="Key_(\w+)"/><ModifierDevice="Keyboard"Key="Key_(\w+)"/>.*</%s>'%(ED_KeyName,ED_KeyName), s)
                                        if not mySecondaryDeviceType_with_3_Modifiers:#если клавиши вторичного устройства с 3 модификаторами не существует
                                            print 'клавиша вторичного устройства с 3 модификаторами не обнаружена'
                                            result = "NoKey"
                                            #vc.callAction("TTS.Speak","Комбинация клавиш на первичном устройстве отсутствует или не соответствует", None)
                                        else:#иначе нажмию клавиши вторичного устройства с 3 модификатором
                                            print 'клавиша вторичного устройства с 3 модификаторами обнаружена'
                                            print 'нажимаю клавишу вторичного устройства с 3 модификаторами'
                                            NumKeys_with_Modifiers = 3
                                            myMainDeviceKey = mySecondaryDeviceType_with_3_Modifiers.group(1)#клавиша вторичного устройства без модификаторов
                                            myModifier1Key = mySecondaryDeviceType_with_3_Modifiers.group(2)#клавиша модификатора 1
                                            myModifier2Key = mySecondaryDeviceType_with_3_Modifiers.group(3)#клавиша модификатора 2
                                            myModifier3Key = mySecondaryDeviceType_with_3_Modifiers.group(4)#клавиша модификатора 3
                                            vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                                            vc.callAction("DxInput.KeyDown","%s"%myModifier1Key, None)
                                            vc.callAction("DxInput.KeyDown","%s"%myModifier2Key, None)
                                            vc.callAction("DxInput.KeyDown","%s"%myModifier3Key, None)
                                            if ED_KeyHoldTime > 0:
                                                print 'тут нажимаем клавишу на n мс'
                                                vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                                            else:
                                                print ('тут нажимаем простую клавишу без удержания')
                                                vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
                                            vc.callAction("DxInput.KeyUp","%s"%myModifier3Key, None)
                                            vc.callAction("DxInput.KeyUp","%s"%myModifier2Key, None)
                                            vc.callAction("DxInput.KeyUp","%s"%myModifier1Key, None)
                                    else:#иначе нажмию клавиши вторичного устройства с 2 модификатором
                                        print 'клавиша вторичного устройства с 2 модификаторами обнаружена'
                                        print 'нажимаю клавишу вторичного устройства с 2 модификаторами'
                                        myMainDeviceKey = mySecondaryDeviceType_with_2_Modifiers.group(1)#клавиша вторичного устройства без модификаторов
                                        myModifier1Key = mySecondaryDeviceType_with_2_Modifiers.group(2)#клавиша модификатора 1
                                        myModifier2Key = mySecondaryDeviceType_with_2_Modifiers.group(3)#клавиша модификатора 2
                                        NumKeys_with_Modifiers = 2
                                        vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                                        vc.callAction("DxInput.KeyDown","%s"%myModifier1Key, None)
                                        vc.callAction("DxInput.KeyDown","%s"%myModifier2Key, None)
                                        if ED_KeyHoldTime > 0:
                                            print 'тут нажимаем клавишу на n мс'
                                            vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                                        else:
                                            print ('тут нажимаем простую клавишу без удержания')
                                            vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
                                        vc.callAction("DxInput.KeyUp","%s"%myModifier2Key, None)
                                        vc.callAction("DxInput.KeyUp","%s"%myModifier1Key, None)
                                else:#иначе нажмию клавиши вторичного устройства с 1 модификатором
                                    print 'клавиша вторичного устройства с 1 модификатором обнаружены'
                                    print 'нажимаю клавишу вторичного устройства с 1 модификатором'
                                    NumKeys_with_Modifiers = 1
                                    myMainDeviceKey = mySecondaryDeviceType_with_1_Modifiers.group(1)#клавиша вторичного устройства без модификаторов
                                    myModifier1Key = mySecondaryDeviceType_with_1_Modifiers.group(2)#клавиша модификатора 1
                                    vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                                    vc.callAction("DxInput.KeyDown","%s"%myModifier1Key, None)
                                    if ED_KeyHoldTime > 0:
                                        print 'тут нажимаем клавишу на n мс'
                                        vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                                    else:
                                        print ('тут нажимаем простую клавишу без удержания')
                                        vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
                                    vc.callAction("DxInput.KeyUp","%s"%myModifier1Key, None)
                            else:#иначе нажмию клавиши вторичного устройства без модификаторов
                                print 'клавиша вторичного устройства без модификаторов обнаружена'
                                print 'нажимаю клавишу вторичного устройства без модификаторов'
                                NumKeys_with_Modifiers = 0
                                myMainDeviceKey = mySecondaryDeviceType_no_Modifier.group(1)#клавиша вторичного устройства без модификаторов
                                vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                                if ED_KeyHoldTime > 0:
                                    print 'тут нажимаем клавишу на n мс'
                                    vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                                else:
                                    print ('тут нажимаем простую клавишу без удержания')
                                    vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
                        else:#иначе нажмию клавишу мыши вторичного устройства без модификаторов
                            print 'клавиша мыши вторичного устройства без модификаторов обнаружена'
                            print 'нажимаю клавишу мыши вторичного устройства без модификаторов'
                            NumKeys_with_Modifiers = 0
                            myMainDeviceKey = mySecondaryDeviceType_no_ModifierMouse.group(1)#клавиша мыши вторичного устройства без модификаторов
                            vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                            if ED_KeyHoldTime > 0:
                                print 'тут нажимаем клавишу на n мс'
                                vc.callAction("DxInput.Mouse.Click","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                            else:
                                print ('тут нажимаем простую клавишу без удержания')
                                vc.callAction("DxInput.Mouse.Click","%s&&"%myMainDeviceKey, None)            
                    else:#иначе нажмию клавиши первичного устройства с 3 модификатором
                        print 'клавиша первичного устройства с 3 модификаторами обнаружена'
                        print 'нажимаю клавишу первичного устройства с 3 модификаторами'
                        NumKeys_with_Modifiers = 3
                        myMainDeviceKey = myPrimaryDeviceType_with_3_Modifiers.group(1)#клавиша первичного устройства без модификаторов
                        myModifier1Key = myPrimaryDeviceType_with_3_Modifiers.group(2)#клавиша модификатора 1
                        myModifier2Key = myPrimaryDeviceType_with_3_Modifiers.group(3)#клавиша модификатора 2
                        myModifier3Key = myPrimaryDeviceType_with_3_Modifiers.group(4)#клавиша модификатора 3
                        vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                        vc.callAction("DxInput.KeyDown","%s"%myModifier1Key, None)
                        vc.callAction("DxInput.KeyDown","%s"%myModifier2Key, None)
                        vc.callAction("DxInput.KeyDown","%s"%myModifier3Key, None)
                        if ED_KeyHoldTime > 0:
                            print 'тут нажимаем клавишу на n мс'
                            vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                        else:
                            print ('тут нажимаем простую клавишу без удержания')
                            vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
                        vc.callAction("DxInput.KeyUp","%s"%myModifier3Key, None)
                        vc.callAction("DxInput.KeyUp","%s"%myModifier2Key, None)
                        vc.callAction("DxInput.KeyUp","%s"%myModifier1Key, None)
                else:#иначе нажмию клавиши первичного устройства с 2 модификатором
                    print 'клавиша первичного устройства с 2 модификаторами обнаружена'
                    print 'нажимаю клавишу первичного устройства с 2 модификаторами'
                    NumKeys_with_Modifiers = 2
                    myMainDeviceKey = myPrimaryDeviceType_with_2_Modifiers.group(1)#клавиша первичного устройства без модификаторов
                    myModifier1Key = myPrimaryDeviceType_with_2_Modifiers.group(2)#клавиша модификатора 1
                    myModifier2Key = myPrimaryDeviceType_with_2_Modifiers.group(3)#клавиша модификатора 2
                    vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                    vc.callAction("DxInput.KeyDown","%s"%myModifier1Key, None)
                    vc.callAction("DxInput.KeyDown","%s"%myModifier2Key, None)
                    if ED_KeyHoldTime > 0:
                        print 'тут нажимаем клавишу на n мс'
                        vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                    else:
                        print ('тут нажимаем простую клавишу без удержания')
                        vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
                    vc.callAction("DxInput.KeyUp","%s"%myModifier2Key, None)
                    vc.callAction("DxInput.KeyUp","%s"%myModifier1Key, None)
            else:#иначе нажмию клавиши первичного устройства с 1 модификатором
                print 'клавиша первичного устройства с 1 модификатором обнаружена'
                print 'нажимаю клавишу первичного устройства с 1 модификатором'
                NumKeys_with_Modifiers = 1
                myMainDeviceKey = myPrimaryDeviceType_with_1_Modifiers.group(1)#клавиша первичного устройства без модификаторов
                myModifier1Key = myPrimaryDeviceType_with_1_Modifiers.group(2)#клавиша модификатора 1
                vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
                vc.callAction("DxInput.KeyDown","%s"%myModifier1Key, None)
                if ED_KeyHoldTime > 0:
                    print 'тут нажимаем клавишу на n мс'
                    vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
                else:
                    print ('тут нажимаем простую клавишу без удержания')
                    vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
                vc.callAction("DxInput.KeyUp","%s"%myModifier1Key, None)
        else:#иначе нажмию клавиши первичного устройства без модификаторов
            print 'клавиша первичного устройства без модификаторов обнаружены'
            print 'нажимаю клавишу первичного устройства без модификаторов'
            NumKeys_with_Modifiers = 0
            myMainDeviceKey = myPrimaryDeviceType_no_Modifier.group(1)#клавиша первичного устройства без модификаторов
            vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
            if ED_KeyHoldTime > 0:
                print 'тут нажимаем клавишу на n мс'
                vc.callAction("DxInput.KeyHold","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
            else:
                print ('тут нажимаем простую клавишу без удержания')
                vc.callAction("DxInput.KeyPress","%s"%myMainDeviceKey, None)
    else:#иначе нажмию клавиши мыши первичного устройства без модификаторов
        print 'клавиша мыши первичного устройства без модификаторов обнаружены'
        print 'нажимаю клавишу мыши первичного устройства без модификаторов'
        NumKeys_with_Modifiers = 0
        myMainDeviceKey = myPrimaryDeviceType_no_ModifierMouse.group(1)#клавиша первичного устройства без модификаторов
        vc.callAction("PY.ExecFile","PY\ED.KeyRUtoKeyEN.py", None) #1111111
        if ED_KeyHoldTime > 0:
            print 'тут нажимаем клавишу на n мс'
            vc.callAction("DxInput.Mouse.Click","%s&&%s"%(myMainDeviceKey,ED_KeyHoldTime), None)
        else:
            print ('тут нажимаем простую клавишу без удержания')
            vc.callAction("DxInput.Mouse.Click","%s"%myMainDeviceKey, None)