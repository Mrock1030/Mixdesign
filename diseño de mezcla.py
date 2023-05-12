import os
import time

def clear_screen():
    if os.name == "posix":
        var = "clear"       
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"
    return var
    

#funcion de resistencia a la compresion
def resitence_of_fc(fc):
    if fc < 210:
        fc += 70
    elif fc >=210 and fc <= 350:
        fc += 84
    elif fc > 350:
        fc = (1.1*fc)+50
    return fc




####Datos del programa###

#asentaminetos
settlement = {
    "Zapatas y muros de cimentacion reforzado":{ 
        "Maximo":75,
        "Minimi":25        
    },
    
    "Zapatas cajaones y juros de subestructuras sin refuerzo":{ 
        "Maximo":75,
        "Minimi":25        
    },
    
    "Vigas y Muros reforzados":{ 
        "Maximo":100,
        "Minimi":25        
    },
    
    "Columnas de edificios":{ 
        "Maximo":100,
        "Minimi":25        
    },
    
    "Pavimentos y losas":{ 
        "Maximo":75,
        "Minimi":25        
    },
    
    "Concreto masivo":{ 
        "Maximo":75,
        "Minimi":25        
    },

    
}

compressive_strength = {
    450:{
        "concreto sin aire incluido":0.38,
        "concreto con aire incluido":0.31
        },
    400:{ 
        "concreto sin aire incluido":0.43,
        "concreto con aire incluido":0.34
        },
    350:{
        "concreto sin aire incluido":0.48,
        "concreto con aire incluido":0.40
        },
    300:{
        "concreto sin aire incluido":0.55,
        "concreto con aire incluido":0.46
        },
    250:{
        "concreto sin aire incluido":0.62,
        "concreto con aire incluido":0.53
        },
    200:{
        "concreto sin aire incluido":0.70,
        "concreto con aire incluido":0.61
        },
    150:{
        "concreto sin aire incluido":0.8,
        "concreto con aire incluido":0.72
        },    
}
#tabla del contenido de aire y contenido de agua 
#esta es sin aire incluido
slumps_without_air = {
    "25 a 50":{
         9.5:207,
         12.5:199,
         19:190,
         25:179,
         37.5:166,
         50:154,
         75:130,
         150:113},
    "75 a 100":{
         9.5:228,
         12.5:216,
         19:205,
         25:193,
         37.5:181,
         50:169,
         75:145,
         150:124
        },
    "150 a 175":{
         9.5:243,
         12.5:228,
         19:216,
         25:202,
         37.5:190,
         50:178,
         75:160,
         150:None
         },
    "amount_of_air":{
        9.5:0.03,
        12.5:0.025,
        19:0.02,
        25:0.015,
        37.5:0.01,
        50:0.005,
        75:0.003,
        150:0.002
    }
}
#esta es con aire incluido
slumps_with_air = {
    "25 a 50":{
         9.5:207,
         12.5:199,
         19:190,
         25:179,
         37.5:166,
         50:154,
         75:130,
         150:113},
    "75 a 100":{
         9.5:228,
         12.5:216,
         19:205,
         25:193,
         37.5:181,
         50:169,
         75:145,
         150:124
        },
    "150 a 175":{
         9.5:243,
         12.5:228,
         19:216,
         25:202,
         37.5:190,
         50:178,
         75:160,
         150:None
         },
    
    "amount_of_air":{
        
        "Exposicion blanda":{
             9.5:0.045,
             12.5:0.04,
             19:0.035,
             25:0.03,
             37.5:0.025,
             50:0.02,
             75:0.015,
             150:0.01
            },
        "Exposicion moderada":{
             9.5:0.06,
             12.5:0.055,
             19:0.05,
             25:0.045,
             37.5:0.045,
             50:0.04,
             75:0.035,
             150:0.03
            },
        "Exposicion severa":{
             9.5:0.075,
             12.5:0.07,
             19:0.06,
             25:0.06,
             37.5:0.055,
             50:0.05,
             75:0.045,
             150:0.04
            },  
    }
}

#tabla modulo de finura
nominal_maximum_size={
    9.5:{
        2.40:0.50,
        2.60:0.48,
        2.80:0.46,
        3:0.44},
    12.5:{
        2.40:0.59,
        2.60:0.57,
        2.80:0.55,
        3:0.53},
    19:{
        2.40:0.66,
        2.60:0.64,
        2.80:0.62,
        3:0.60},
    25:{
        2.40:0.71,
        2.60:0.69,
        2.80:0.67,
        3:0.65 },
    37.5:{
        2.40:0.75,
        2.60:0.73,
        2.80:0.71,
        3:0.69},
    50:{
        2.40:0.78,
        2.60:0.76,
        2.80:0.74,
        3:0.72},
    75:{
        2.40:0.82,
        2.60:0.80,
        2.80:0.78,
        3:0.76},
    150:{
        2.40:0.87,
        2.60:0.85,
        2.80:0.83,
        3:0.81},  
}

#funcion que interpolacion 
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

unit = { "M":10e5,"K":1000,"D":10,"pa":1.0197e-5,"psi":0.070307,"kg/cm2":1
}
#esta fucion revisa que unidad este dentro del dict
#y si esta toma la posicion de esas variables en el dict
def unit_fc(fuerza,unit,unidad):

    if unidad[0:1].upper() and unidad[1::]in unit:
        c1= unit[unidad[0:1]]
        c2 = unit[unidad[1::]]
        
    elif unidad in unit:
        c1=1
        c2 = unit[unidad]
    
    else:
        print("Revisar unidades ingresadas")
    fuerza = fuerza*c1*c2
    return fuerza 
#salduo de bienvenida
def welcome():
    print("\t\t Bienvenido al Diseñador de Mezcla de Hormigon \t\t")

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
    
    
def main():
    welcome()
    menu = int(input("""
    [1] Diseñar una Mezcla en hormigon
    [2] Salir  
    >>>"""))
    if menu == 1:
        #datos de agregado grueso.
        print("\t Datos Agregado Grueso \t\n")
        tmn = float(input("Ingrese TMN en pulgadas: " ))
        d_aparente_ag = float(input("Ingrese Densidad aparente: "))
        humedad_ag = float(input("Ingrese" "% " "de humedad: "))
        abosorcion_ag = float(input("Ingrese" "% " "de absorcion: "))
        muc_ag  = float(input("Ingrese MUC: "))
        muc_ag= unit_fc(muc_ag, unit,menu_unidades() )
        mus_ag  = float(input("Ingrese MUS: "))
        mus_ag= unit_fc(mus_ag, unit,menu_unidades() )
        
        #limpia la pantalla
        print("\n" *80)
        
        #Datos de agregado fino.
        print("\t Datos Agregado Fino \t\n")
        mf = float(input("Ingrese Modulo de finura: " ))
        d_aparente_af = float(input("Ingrese Densidad aparente: "))
        humedad_af = float(input("Ingrese" "% " "de humedad: "))
        abosorcion_af = float(input("Ingrese" "% " "de absorcion: "))
        muc_af  = float(input("Ingrese MUC: "))
        muc_af= unit_fc(muc_af, unit,menu_unidades() )
        mus_af  = float(input("Ingrese MUS: "))
        mus_af= unit_fc(mus_af, unit,menu_unidades() )
        print("\n" *100)
        
        #Datos del cemento
        cemento = float(input("Ingrese la densidad del cemento: " ))
        cemento=unit_fc(cemento, unit,menu_unidades() )
        fc = int(input("Ingrese la resistencia especificada: "))
        fc = unit_fc(fc, unit, menu_unidades())
        aire_incluido= int(input("""
    [1] Aire incluido
    [2] Sin Aire incluido  
    >>>"""))
        
        #añadimos un while en caso de que no ingrese un dato erroneo
        while aire_incluido != 1 and aire_incluido!=2:
            print("ingresaste un dato invalido")
            aire_incluido = int(input(":")) 
            print(type(aire_incluido))
                          
    #opcion de menu de inicio 
    elif menu == 2:
        print("Cerrando programa...")
        time.sleep(2)
        exit()
        
        
main()