import turtle
''' se importa este moodulo para poder llamar al modulo turtle desde la biblioteca de python
y poder trabajar con dichas herramientas'''

def estrella(puntas, color_usuario, tamaño_usuario):

    '''
    La configuración de la tortuga. En este caso estoy definiendo la velocidad a la que quiero
    que dibuje, el color del dibujo, y el grosor del dibujo y el color y el tamaño de la propia tortuga
    asi como el color del fondo del lienzo.'''
    
    turtle.shape("turtle")
    turtle.speed(3)
    turtle.color(color_usuario)
    turtle.pensize(5)
    turtle.fillcolor("yellow")
    turtle.shapesize(2)
    turtle.bgcolor("black")
    '''Este bucle for, me permite dibujar la estrella. En cada iteración, la tortuga avanza las unidades deseadas 
    por el usuario hacia alante y luego gira en grados a la derecha ().'''
    for _ in range(puntas):
        turtle.right( 360 / puntas * 2 )
        turtle.forward(int(tamaño_usuario))

def main():
    
        color_usuario = input(f"Ingresa el color de la estrella (en ingles):  ") 
        puntas_usuario = int(input(f"Ingresa el número de puntas de la estrella (solo nº impares):  "))
        tamaño_usuario = input(f"Ingresa el tamaño de la estrella:  ") 
        estrella(puntas_usuario, color_usuario, tamaño_usuario), 

        turtle.done()

main()
