####Datos del programa###


#diccinario de unidades
dict_unit = { "M":10e6,"K":1000,"D":10,"pa":1.0197e-5,"psi":0.070307,"kg/cm2":1
}

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
