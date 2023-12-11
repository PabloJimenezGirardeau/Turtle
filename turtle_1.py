import turtle
''' se importa este moodulo para poder llamar al modulo turtle desde la biblioteca de python
y poder trabajar con dichas herramientas'''


def estrella():
    ''' viendo que al realizar el dibujo este no esta centrado dentro de la hoja, 
    se realizan los siguientes ajustes:'''
    
    turtle.penup()  # Levantar el lápiz para no dibujar
    turtle.goto(-160, 30)  # Mover a las coordenadas deseadas
    turtle.pendown()  # Bajar el lápiz para dibujar
     
    """
    A continuación es la configuración de la tortuga. En este caso estoy definiendo la velocidad a la que quiero
    que dibuje, el color del dibujo, y el grosor del dibujo y el color y el tamaño de la propia tortuga
    asi como el color del fondo del lienzo."""
    
    turtle.shape ("turtle")
    turtle.speed(1)
    turtle.color("white")
    turtle.pensize(5)
    turtle.fillcolor("yellow")
    turtle.shapesize(2)
    turtle.bgcolor("black")
    
    
    
    """
    Este bucle for, me permite dibujar la estrella. En cada iteración, la tortuga avanza 200 unidades 
    hacia alante y luego gira 160º a la derecha. de esta forma, y con el rango definido como 9, el bucle
    se repite 9 veces formando una estrella de 9 puntas como la pedida en el ejercicio.
    """
    for _ in range(9):
        turtle.forward(300)
        turtle.right(160)
    # Finaliza la ventana de Turtle cuando se completa el dibujo
    turtle.done()
    

# Llama a la función para dibujar la estrella
estrella()