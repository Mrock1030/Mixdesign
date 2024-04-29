import time 
from data import * 
from funtions import *

#funcion principal    
def main():
    welcome()
    menu = int(input("""
    [1] Diseñar una Mezcla en hormigon
    [2] Salir  
    >>>"""))
    if menu == 1:
        press = None
        while True:
            #datos de agregado grueso.
            #limpia la pantalla
            print("\n" *80)
            print("Cargando datos de agregado Grueso")
            time.sleep(2)
            print("\n" *80)
            
            print("\t Datos Agregado Grueso \t\n")
            try:
               
                tmn = float(input("Ingrese TMN en pulgadas: " ))
                d_aparente_ag = float(input("Ingrese Densidad aparente: "))
                humedad_ag = float(input("Ingrese" "% " "de humedad: "))
                abosorcion_ag = float(input("Ingrese" "% " "de absorcion: "))
                muc_ag  = float(input("Ingrese MUC: "))
                muc_ag= unit_converter(muc_ag,dict_unit,menu_unidades())
                mus_ag  = float(input("Ingrese MUS: "))
                mus_ag= unit_converter(mus_ag,dict_unit,menu_unidades() )
                 #limpia la pantalla
                print("\n" *80)
                print("Cargando datos de agregado fino")
                time.sleep(2)
                break
                    
            except ValueError as error :
                print("INGRESASTE UN CARACTER EN VEZ DE UN NUMERO\n\n") 
                print("Volviendo al menu")
                time.sleep(2)
                pass
            
        
        #limpia la pantalla
        print("\n" *80)
        print("Cargando datos de agregado Grueso")
        time.sleep(2)
        print("\n" *80)
        
        
        #Datos de agregado fino.
        print("\t Datos Agregado Fino \t\n")
        while True:
            try:
                mf = float(input("Ingrese Modulo de finura: " ))
                d_aparente_af = float(input("Ingrese Densidad aparente: "))
                humedad_af = float(input("Ingrese" "% " "de humedad: "))
                abosorcion_af = float(input("Ingrese" "% " "de absorcion: "))
                muc_af  = float(input("Ingrese MUC: "))
                muc_af= unit_converter(muc_af,dict_unit,menu_unidades())
                mus_af  = float(input("Ingrese MUS: "))
                mus_af= unit_converter(mus_af, dict_unit,menu_unidades() )
                print("\n" *80)
                
                print("Cargando datos de cemento\n")
                time.sleep(2)
                    
                break
                print("\n" *100)
                
            except ValueError as error:
                print("INGRESASTE UN CARACTER EN VEZ DE UN NUMERO\n") 
                
                
        #limpia la pantalla
        print("\n" *80)
                
        #Datos del cemento
        print("\t ..Datos Cemento.. \t\n")
        
        while True:
            try:
                cemento = float(input("Ingrese la densidad del cemento: " ))
                cemento=unit_converter(cemento,dict_unit,menu_unidades() )
                fc = int(input("Ingrese la resistencia especificada: "))
                fc = unit_converter(fc,dict_unit,menu_unidades())
                fc = resitence_of_fc(fc)
                break
        #except     
            except ValueError as error:
                print("INGRESASTE UN CARACTER EN VEZ DE UN NUMERO \n")
                print("Volviendo al menu")
                time.sleep(2)
                
        while True:
            try:
                aire_incluido= int(input("""
                [1] Aire incluido
                [2] Sin Aire incluido  
                >>>"""))
                if aire_incluido == 1:
                    condition = "concreto con aire incluido"
                    break
                
                elif aire_incluido ==2:
                    condition = "concreto sin aire incluido"
                    break
            except:
                print("INGRESASTE UN CARACTER EN VEZ DE UN NUMERO \n")
                print("Volviendo al menu")
                time.sleep(2)
                
        #relacion agua cemento
        #solamente tomamos los dos preimeros decimales despues del cero.       
        ram = interpolation(compressive_strength, fc, condition)
        ram =ignoradecimales(ram)
                                  
    #opcion de menu de inicio 
    elif menu == 2:
        print("Cerrando programa...")
        time.sleep(2)
        exit()       
main()