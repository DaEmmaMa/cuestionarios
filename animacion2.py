from manim import *
import numpy as np

class Misegunda(Scene):
    def construct(self):
        # Cambiar fondo a blanco
        self.camera.background_color = WHITE
        
        # 1. Primer texto: nombre (cambiar color para que se vea en fondo blanco)
        texto1 = Text("David Martinez Salazar", font_size=48, color=BLACK)
        self.play(Write(texto1))
        self.wait(2)
        
        # Hacer desaparecer el primer texto
        self.play(FadeOut(texto1))
        self.wait(0.5)
        
        # 2. Función exponencial
        # Crear plano cartesiano (cambiar colores para fondo blanco)
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 8, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": BLACK},
            x_axis_config={"numbers_to_include": np.arange(-3, 4, 1)},
            y_axis_config={"numbers_to_include": np.arange(0, 9, 1)}
        )
        
        # Etiquetas de los ejes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        x_label.set_color(BLACK)
        y_label.set_color(BLACK)
        
        # Mostrar el plano cartesiano
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)
        
        # Crear la función exponencial e^x
        exp_graph = axes.plot(
            lambda x: np.exp(x),
            color=RED,
            x_range=[-2.5, 2]
        )
        
        # Etiqueta de la función
        func_label = MathTex("f(x) = e^x", color=RED).next_to(exp_graph, UR)
        
        # Animar la función de izquierda a derecha
        self.play(Create(exp_graph), Write(func_label), run_time=3)
        self.wait(2)
        
        # Hacer desaparecer la función
        self.play(FadeOut(axes), FadeOut(exp_graph), FadeOut(func_label), FadeOut(x_label), FadeOut(y_label))
        self.wait(0.5)
        
        # 3. Gráfico de barras con ejes
        # Crear ejes para el gráfico de barras
        bar_axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 25, 5],
            x_length=8,
            y_length=5,
            axis_config={"color": BLACK},
            y_axis_config={"numbers_to_include": np.arange(0, 26, 5)}
        )
        
        # Etiquetas de los ejes del gráfico de barras
        x_label_bars = bar_axes.get_x_axis_label("Categorias")
        y_label_bars = bar_axes.get_y_axis_label("Valores")
        x_label_bars.set_color(BLACK)
        y_label_bars.set_color(BLACK)
        
        # Mostrar los ejes
        self.play(Create(bar_axes), Write(x_label_bars), Write(y_label_bars))
        
        # Título del gráfico
        chart_title = Text("Estadística para Big Data", font_size=40, color=BLACK).to_edge(UP)
        self.play(Write(chart_title))
        self.wait(1)
        
        # Crear las barras alineadas con el eje
        # Posiciones en el eje X: A=1, B=2, C=3
        bar_A = Rectangle(
            width=0.6, 
            height=bar_axes.c2p(0, 6)[1] - bar_axes.c2p(0, 0)[1], 
            color=BLUE, 
            fill_opacity=0.8
        ).move_to(bar_axes.c2p(1, 3))  # Centrada en x=1, altura media=3
        
        bar_B = Rectangle(
            width=0.6, 
            height=bar_axes.c2p(0, 10)[1] - bar_axes.c2p(0, 0)[1], 
            color=GREEN, 
            fill_opacity=0.8
        ).move_to(bar_axes.c2p(2, 5))  # Centrada en x=2, altura media=5
        
        bar_C = Rectangle(
            width=0.6, 
            height=bar_axes.c2p(0, 20)[1] - bar_axes.c2p(0, 0)[1], 
            color=RED, 
            fill_opacity=0.8
        ).move_to(bar_axes.c2p(3, 10))  # Centrada en x=3, altura media=10
        
        # Etiquetas en el eje X
        label_A = Text("A", font_size=24, color=BLACK).move_to(bar_axes.c2p(1, -2))
        label_B = Text("B", font_size=24, color=BLACK).move_to(bar_axes.c2p(2, -2))
        label_C = Text("C", font_size=24, color=BLACK).move_to(bar_axes.c2p(3, -2))
        
        # Valores encima de las barras
        value_A = Text("6", font_size=20, color=BLACK).move_to(bar_axes.c2p(1, 7))
        value_B = Text("10", font_size=20, color=BLACK).move_to(bar_axes.c2p(2, 11))
        value_C = Text("20", font_size=20, color=BLACK).move_to(bar_axes.c2p(3, 21))
        
        # Animar aparición de las barras
        self.play(
            GrowFromEdge(bar_A, DOWN),
            GrowFromEdge(bar_B, DOWN),
            GrowFromEdge(bar_C, DOWN),
            Write(label_A),
            Write(label_B),
            Write(label_C),
            Write(value_A),
            Write(value_B),
            Write(value_C)
        )
        self.wait(2)
        
        # Hacer desaparecer el gráfico
        self.play(
            FadeOut(bar_A), FadeOut(bar_B), FadeOut(bar_C),
            FadeOut(label_A), FadeOut(label_B), FadeOut(label_C),
            FadeOut(value_A), FadeOut(value_B), FadeOut(value_C),
            FadeOut(chart_title), FadeOut(bar_axes), 
            FadeOut(x_label_bars), FadeOut(y_label_bars)
        )
        self.wait(0.5)
        
        # 4. Texto final
        texto2 = Text("Colegio Universitario de Cartago", font_size=44, color=BLACK)
        self.play(Write(texto2))
        self.wait(3)
        
        # Fade out final
        self.play(FadeOut(texto2))
        self.wait(1)