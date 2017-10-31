from Clases import *

Controlador.iniciar()

Colores = {'Negro': (0, 0, 0), "Blanco": (255, 255, 255), "Verde": (50, 205, 50),
           "Rojo": (178, 34, 34), "Naranja": (255, 165, 0), "Amarillo": (255, 215, 0),
           "Celeste": (0, 255, 255), "Azul": (0, 0, 255)}

ancho, alto = 1360, 720

FPS = 120

ventana = Controlador.configurar_pantalla(ancho, alto)

Controlador.rellenar_pantalla(ventana, Colores)

reloj = Controlador.iniciar_reloj()

Nombre_Texto = ""

Letras = ""

frames_totales = 0

frames_aux = 0

posicion_texto = 0

frames_escritura = 0

crecimiento = 0

Titulo = Palabra(30, 20, Colores["Blanco"], "ingrese  su  nombre", 90)

aux = 0

posx = 280

x = posx

posy = 280

y = posy

Lista_Letras = []

while True:
    Controlador.set_fps(reloj, FPS)
    Letras = Controlador.buscar_eventos(Colores)
    if Letras is not None:
        if len(Lista_Letras) <= 7:
                Letras.posX = posx
                Letras.posY = posy
                if Letras.texto != " ":
                    Lista_Letras.append(Letras)
                    aux += 1
                    posx += 100
        if Letras.texto == " ":
            Lista_Letras.remove(Lista_Letras[aux-1])
            aux -= 1
            posx -= 100
    Controlador.rellenar_pantalla(ventana, Colores)
    for letra in Lista_Letras:
        ventana.blit(letra.Palabra, (letra.posX, letra.posY))

    ventana.blit(Titulo.Palabra, (Titulo.posX, Titulo.posY))
    pygame.draw.rect(ventana, Colores["Blanco"], (x, y + 95, 50, 20))
    pygame.draw.rect(ventana, Colores["Blanco"], (x + 100, y + 95, 50, 20))
    pygame.draw.rect(ventana, Colores["Blanco"], (x + 200, y + 95, 50, 20))
    pygame.draw.rect(ventana, Colores["Blanco"], (x + 300, y + 95, 50, 20))
    pygame.draw.rect(ventana, Colores["Blanco"], (x + 400, y + 95, 50, 20))
    pygame.draw.rect(ventana, Colores["Blanco"], (x + 500, y + 95, 50, 20))
    pygame.draw.rect(ventana, Colores["Blanco"], (x + 600, y + 95, 50, 20))
    pygame.draw.rect(ventana, Colores["Blanco"], (x + 700, y + 95, 50, 20))
    pygame.display.update()
    frames_totales += 1