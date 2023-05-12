#
# FUNCIONES DEL PROGRAMA
#

#salduo de bienvenida
def welcome():
    print("\t\t Bienvenido al Diseñador de Mezcla de Hormigon \t\t")
    
#funcion de menu de unidades    
def menu_unidades():
    
    menu_unidades = int(input("""
    [1] Mpa
    [2] Kpa 
    [3] Dpa
    [4] pa 
    [5] psi
    [6] kg/cm2
    """))
    
    while menu_unidades <1 or menu_unidades > 6:
        print("¡INGRESASTE UN DATO ERRONEO !")
        menu_unidades = int(input(">>>"))  
        
    if menu_unidades == 1:
        return "Mpa"
    elif menu_unidades == 2:
        return "Kpa"
    elif menu_unidades == 3:
        return "Dpa"
    elif menu_unidades == 4:
        return "pa"
    elif menu_unidades == 5:
        return "psi"
    elif menu_unidades == 6:
        return "kg/cm2"

#funcion de resistencia a la compresion
def resitence_of_fc(fc):
    if fc < 210:
        fc += 70
    elif fc >=210 and fc <= 350:
        fc += 84
    elif fc > 350:
        fc = (1.1*fc)+50
    return fc

#esta funcion revisa que unidad este dentro del dict
#y si esta toma la posicion de esas variables en el dict

def unit_converter(fuerza,dict_unit,unidad):

    if unidad[0:1].upper() and unidad[1::]in dict_unit:
        c1= unit[unidad[0:1]]
        c2 = unit[unidad[1::]]
        
    elif unidad in dict_unit:
        c1=1
        c2 = dict_unit[unidad]
        
    else:
        print("Revisar unidades ingresadas")
    fuerza = fuerza*c1*c2
    return fuerza


#funcion de  interpolacion de datos en diccinarios 
def interpolation(dictionary, keys, expo):
        if keys  in dictionary:
            return dictionary[keys][expo]
        else:
            sorted_keys = sorted(dictionary.keys())
            if keys < sorted_keys[0] or keys > sorted_keys[-1]:
                return None  # error, key is out of range.
            
            for i in range(len(sorted_keys) - 1):
                if keys >= sorted_keys[i] and keys <= sorted_keys[i + 1]:
                    x1, x2 = sorted_keys[i], sorted_keys[i + 1]
                    y1, y2 = dictionary[x1][expo], dictionary[x2][expo]
                    return y1 + (y2 - y1) * ((keys - x1) / (x2 - x1))


#segunda funcion de interpolacion 
def interpolation_added_end(dictionary,nominal,module):
    if nominal in dictionary:
        if module in dictionary[nominal].keys():
            return dictionary[nominal][module]

        else:
            #organizo los valores de menor a mayor
            sorted_values = sorted(dictionary[nominal].keys())
            #en caso de que el valor este por fuera de los limites
            if module < sorted_values[0] or module>sorted_values[-1]:
                return  print("Sua valor esta fuera del rango ")
            #
            for x in range(len(sorted_values)-1):
                if module >= sorted_values[x] and sorted_values[x+1]:
                    #definimos las variables
                    x1,x2 = sorted_values[x], sorted_values[x+1]
                    y1,y2 = dictionary[nominal][x1], dictionary[nominal][x2] 
                    print("Valores de x1, x2, y1, y2: ", x1, x2, y1, y2)
                    return y1 + (y2 - y1) * ((module - x1) / (x2 - x1))
    else:
        print("valor incorrecto")
 