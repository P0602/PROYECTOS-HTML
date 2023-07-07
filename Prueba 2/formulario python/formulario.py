import os

os.system ('cls')
respuesta="si"
while (respuesta=="si"):
    
       
        #formulario
        print('-----Calculo de sueldo de los trabajadores------')

        nombres = input('Ingrese su primer y segundo nombre:')

        apellidos = input('Ingrese sus apellidos:')
   
        Run = input('Ingrese su run:')
        
        Sexo = input('Ingrese su sexo, masculino o femenino:')

        print('-----Fecha de nacimiento------')
        
        Dia = input('Ingrese el día:')
        Mes = input('Ingrese el Mes:')
        Año = input('Ingrese el año:')
        
        Cargo_trabajador = input('Ingrese el cargo del trabajador:')
        
        SueldoBase = int(input('Ingrese el sueldo base del trabajador:$'))
        
        Bono_trabajador = int(input('Ingrese el bono del trabajador:$'))

        #variavles
        
        AfpDesc = 0.13
        
        SaludDesc = 0.07
        
        SueldoBruto = SueldoBase + Bono_trabajador
        
        DescAfp = SueldoBruto * AfpDesc
        
        DescIsap = SueldoBruto * SaludDesc
        
        sueldoLiquido = SueldoBruto - DescAfp - DescIsap

        masculino = 'Masculino'
        
        femenino = 'Femenino'

        import os
        os.system ('cls')
        
        print("-- Comprobante de liquidación de sueldo --")
        print("Nombre completo:",nombres, apellidos)
        print("Run:",Run)
        if(Sexo == masculino):
            print("Sexo:",masculino)
        elif(Sexo == femenino):
            print("Sexo:",femenino)
        else:
            print("Sexo:",Sexo)
        print("Fecha de nacimiento:",Dia,'/',Mes,'/',Año)
        print("Cargo del trabajador:",Cargo_trabajador)
        print("sueldo base:$",SueldoBase)
        print("sueldo bruto:$",SueldoBruto)
        print("Descuento afp:$",DescAfp)
        print("Descuento isapre:$",DescIsap)
        print("Sueldo liquido:$",sueldoLiquido)
        respuesta = input("Desea volver a ingresar si o no:")
        while (respuesta!="si" and respuesta!="no"):
            respuesta = input("Incorrecto.Desea volver a ingresar si o no:")
        if(respuesta == "no"):
            print("Fin del programa... ")
        
        
        
        

        
        

    