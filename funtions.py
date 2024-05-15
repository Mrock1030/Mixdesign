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
    #limpiamos la pantalla
    print("\n" *80)
                
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
    
def menu_unidades_metricas():
    
    menu_unidades_metricas = int(input("""
    [1] m
    [2] pulg 
    [3] cm
    """))
    
    while menu_unidades_metricas <1 or menu_unidades_metricas > 3:
        print("¡INGRESASTE UN DATO ERRONEO !")
        menu_unidades_metricas = int(input(">>>")) 
   
    #limpiamos la pantalla
    print("\n" *80)
        
    if menu_unidades_metricas == 1:
        return "m"
    elif menu_unidades_metricas == 2:
        return "pulg"
    elif menu_unidades_metricas == 3:
        return "cm"


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

def unit_converter(u_convertir,dict_unit_presion,unidad):

    if unidad[0:1].upper() and unidad[1::]in dict_unit:
        unidad1= dict_unit[unidad[0:1]]