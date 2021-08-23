#Caja de contabilidad
#Proyecto final

#Entrada

repetir = 1
productosc = eval(input("¿Cuantas lamparas se compraron este mes: "))
kardexc = eval(input("¿Cual es el costo promedio de lamparas en inventario?: "))
inventarioi = eval(input("¿Cuantas lamparas tenias en bodega a principio de mes?: "))
costoc = eval(input("¿Cuanto costo cada producto"))
cajach = eval(input("¿Cuanto tenias en caja chica al principio del mes?: "))
aportacionesac = eval(input("¿Cuanto dinero tenian aportado desde antes?: "))
aportaciones = eval(input("¿cuanto aportaron los socios al inicio del mes?: "))
gastoluz = eval(input("¿Cuanto se gasto en luz?: "))
gastoagua = eval(input("¿Cuanto se gasto en agua?: "))
gastorenta = eval(input("¿Cuanto se te cobra al mes de renta?: "))
gastosvar = eval(input("¿Cuanto estuvo en otros gastos?"))
productosv = eval(input("¿Cuantos productos se vendieron este mes?: "))
preciov = eval(input("¿A cuanto se vendio cada porducto?: "))
trabajadores = eval(input("¿Cuantos trabajadores tienes?: "))
pagot = eval(input("¿Cuanto se le paga al trabajador al mes?: "))

#Variables dependientes
totalp = inventarioi + productosc
kardexcn = (costoc * productosc/totalp) + (kardexc + inventarioi/totalp) #Costo promedio
inventariof = inventarioi + productosc - productosv
nomina = trabajadores * pagot
gastosb = gastoluz + gastoagua + gastorenta + gastosvar
iva = preciov/.16
ingresos = productosv * preciov
utilidadb = ingresos -iva
utilidadn = utilidadb - gastosb - nomina
valori = inventariof * kardexcn
costot = productosc * costoc
isr = (utilidadn * .30)

if utilidadn > 0:
    utilidadf = (-utilidadn * .30) + utilidadn
else:
    if    utilidadn < 0:
     print("Solo hubo perdidoas, no hay ganancia", utilidadn, "fue la cantidad de perdida que tuvo este mes")
    else:
        print("No hubo ganancia ni perdida, se recomienda un mejor seguimiento a la compra y venta de el producto")


while repetir == 1:

    #Salida
    print("-------------------------------")
    print("Estadisticas en la empresa: ")
    print("-------------------------------")
    print("1- Utilidad")
    print("2- impuestos")
    print("3- Inventario")
    print("4- Compra")
    print("5- Venta")
    print("6- Administración")
    menu1 = eval(input("Escriba el numero de la opcion deseada: "))
    if menu1 == 1:
        print("-------------------------------")
        print("menu de utilidad")
        print("-------------------------------")
        print("1- Utilidad bruta")
        print("2- Utilidad Neta")
        print("3- utilidad final")
        mm1 = eval(input("Escriba el numero de la opcion deseada: "))
        if mm1 == 1:
            print("tu utilidad bruta es de ", utilidadb)
        else:
            if mm1 == 2:
                print("tu utilidad neta es de ", utilidadn)
            else:
                if mm1 == 3:
                    print("tu utilidad final es de ", utilidadf)
                else:
                    print("Favor de escoger aalgo que exista")
    else:
        if menu1 == 2:
            print("-------------------------------")    
            print("menu de impuestos")
            print("-------------------------------")
            print("1- Iva a pagar")
            print("2- ISR a pagar")
            mm2 = eval(input("Escriba el numero de la opcion deseada: "))
            if mm2 == 1:
                print("su iva es de ", iva)
            else:
                if mm2 == 2:
                    print("El ISR a pagar es de ", isr)
                else:
                    print("favor de escoger algo que si exista")
        else:
            if menu1 == 3:
                print("-------------------------------")
                print("Menu inventario")
                print("-------------------------------")
                print("1- Inventario actual")
                print("2- Inventario inicial")
                print("3- Costo promedio del producto")
                print("4- valor de inventario")
                mm3 = eval(input("Escriba el numero de la opcion deseada: "))
                if mm3 == 1:
                    print("tu inventario actual es de ", inventariof, "lamparas")
                else:
                    if mm3 == 2:
                        print("Su inventario al inicio del mes era de ", inventarioi , "piezas")
                    else:
                        if mm3 == 3:
                            print("el costo promedio por producto ", kardexcn , "pesos")
                        else:
                            if mm3 == 4:
                                print("el valor total del inventario es de ", valori , "pesos")
                            else:
                                print("favor de escoger algo que exista")
            else:
                if menu1 == 4:
                    print("-------------------------------")
                    print("Menu de compra")
                    print("-------------------------------")
                    print("1-productos comprados")
                    print("2- costo de compra total")
                    mm4 = eval(input("Escriba el numero de la opcion deseada: "))
                    if mm4 == 1:
                        print("Se compraron ", productosc , "lamparas")
                    else:
                        if mm4 == 2:
                            print("el total de costo de productos fue de ", costot , "pesos" )
                        else:
                            print("Favor de escoger algo que existe")
                else:
                    if menu1 == 5:
                        print("-------------------------------")
                        print("Menu de venta")
                        print("-------------------------------")
                        print("1- Productos vendidos")
                        print("2-Total de ventas")
                        mm5 = eval(input("Escriba el numero de la opcion deseada: "))
                        if mm5 == 1:
                            print("el total de productos vendidos fue de ", productosv , "lamparas")
                        else:
                            if mm5 == 2:
                                print("los ingresos por ventas totales fueron de ", ingresos , "pesos")
                    else:
                        if menu1 == 6:
                            print("-------------------------------")
                            print("Menu de administracion")
                            print("-------------------------------")
                            print("1- caja chica al finalizar el mes")
                            print("2-gastos basicos")
                            print("3-nomina")
                            mm6 = eval(input("Escriba el numero de la opcion deseada: "))
                            if mm6 == 1:
                                print("Cuentas con ", cajach , "de caja chica")
                            else:
                                if mm6 == 2:
                                    print("los gastos basicos totales fueron de ", gastosb , "pesos")
                                else:
                                    if mm6 == 3:
                                        print("los gastos de nomina dieron un total de ", nomina , "pesos")
                        else:
                            print("Favor de escoger algo que exista")
    print("-------------------------------")
    print("¿Que desea hacer?")
    print("-------------------------------")
    print("1- regresar al menu")
    print("2- finalizar el programa")
    repetir = eval(input("Seleccione su opcion"))
else: print("****************************")
print("Que tenga un buen dia")
print("****************************")
