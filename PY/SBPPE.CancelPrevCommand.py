command = vc.getObject("evalvars","{var.PrevCommand}")
def check():
    if command == "Выдвигаться": 
        print('значениt совпало c Выдвигаться')   
        return True        
    elif command == "Атаковать": 
        print('значениt совпало c Атаковать')   
        return True  
    elif command == "Совершить марш": 
        print('значениt совпало c Совершить марш')   
        return True  
    elif command == "Отойти": 
        print('значениt совпало c Отойти')   
        return True  
    elif command == "Провести разведку": 
        print('значениt совпало c Провести разведку')   
        return True  
    elif command == "Проделать проход": 
        print('значениt совпало c Проделать проход')   
        return True  
    elif command == "Подавить здесь": 
        print('значениt совпало c Подавить здесь')   
        return True  
    elif command == "Занять оборону здесь": 
        print('значение совпало с Занять оборону здесь')   
        return True  
    elif command == "Вести огонь по разделению": 
        print('значениt совпало c Вести огонь по разделению"')   
        return True  
    elif command == "Наблюдать": 
        print('значениt совпало c Наблюдать')   
        return True  
    else:
        print('ниодно значение не совпало')
        return False 
check()