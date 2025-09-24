from manim import *

class MiPrimeraAnimacion(Scene):
    def construct(self):
        # Crear texto de bienvenida
        texto = Text("¡Hola desde Manim!", font_size=50)
        
        # Animar la escritura del texto
        self.play(Write(texto))
        self.wait(1)
        
        # Cambiar color y posición
        self.play(texto.animate.set_color(BLUE).to_edge(UP))
        
        # Crear un círculo
        circulo = Circle(radius=2, color=RED)
        self.play(Create(circulo))
        
        # Rotar el círculo
        self.play(Rotate(circulo, angle=PI))
        self.wait(2)