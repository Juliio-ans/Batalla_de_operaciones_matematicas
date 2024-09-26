import random
import tkinter as tk
from tkinter import messagebox


class BatallaMatematica:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Batalla de Operaciones Matemáticas")
        self.ventana.geometry("600x500")

        # Variables del juego
        self.puntaje_jugador1 = 0
        self.puntaje_jugador2 = 0
        self.tiempo_limite = 20  # Tiempo máximo por turno (en segundos)
        self.turno = 1  # 1 = Jugador 1, 2 = Jugador 2
        self.jugador1 = "Jugador 1"
        self.jugador2 = "Jugador 2"
        self.tiempo_restante = self.tiempo_limite
        self.temporizador_id = None  # Guardará el ID del temporizador

        # Elementos de la ventana
        self.label_bienvenida = tk.Label(self.ventana, text="¡Bienvenido a la Batalla Matemática!", font=("Arial", 14))
        self.label_bienvenida.pack(pady=10)

        self.boton_instrucciones = tk.Button(self.ventana, text="Instrucciones", command=self.mostrar_instrucciones,
                                             font=("Arial", 12))
        self.boton_instrucciones.pack(pady=5)

        self.boton_iniciar = tk.Button(self.ventana, text="Iniciar Juego", command=self.configurar_juego,
                                       font=("Arial", 12))
        self.boton_iniciar.pack(pady=10)

        # Crear un espacio para las instrucciones dinámicas
        self.canvas_instrucciones = tk.Canvas(self.ventana, width=350, height=100, bg="white", highlightthickness=0)
        self.label_instrucciones_dinamicas = tk.Label(self.canvas_instrucciones, text="", font=("Arial", 10),
                                                      bg="white", wraplength=300)
        self.label_instrucciones_dinamicas.place(x=20, y=20)
        self.canvas_instrucciones.pack(pady=5)

    def mostrar_instrucciones(self):
        instrucciones = (
            "¡Bienvenido a la Batalla Matemática!\n\n"
            "Reglas del juego:\n"
            "1. Este juego es para dos jugadores.\n"
            "2. Cada jugador debe resolver una operación matemática.\n"
            "3. Tienes 20 segundos para responder, si no lo haces a tiempo, pierdes tu turno.\n"
            "4. Ganas 10 puntos por cada respuesta correcta.\n"
            "5. Al final, quien tenga más puntos será el ganador.\n"
            "¡Buena suerte!"
        )
        messagebox.showinfo("Instrucciones del Juego", instrucciones)

    def mostrar_instrucciones_secuencial(self):
        # Lista de instrucciones que aparecerán secuencialmente
        self.instrucciones = [
            "Este juego es para dos jugadores.",
            "Cada jugador debe resolver una operación matemática.",
            "Tienes 20 segundos para responder.",
            "Ganas 10 puntos por cada respuesta correcta.",
            "El que más puntos tenga al final, gana.",
            "¡Buena suerte!"
        ]
        self.indice_instruccion = 0
        self.actualizar_instrucciones()

    def actualizar_instrucciones(self):
        if self.indice_instruccion < len(self.instrucciones):
            # Mostrar una instrucción en la nube de diálogo
            self.label_instrucciones_dinamicas.config(text=self.instrucciones[self.indice_instruccion])
            self.dibujar_nube()
            self.indice_instruccion += 1
            # Programar la siguiente instrucción en 3 segundos
            self.ventana.after(3000, self.actualizar_instrucciones)
        else:
            # Limpiar la nube de diálogo después de mostrar todas
            self.label_instrucciones_dinamicas.config(text="")
            self.canvas_instrucciones.delete("nube")

    def dibujar_nube(self):
        # Dibujar una "nube" alrededor de las instrucciones
        self.canvas_instrucciones.delete("nube")  # Limpiar cualquier nube previa
        self.canvas_instrucciones.create_oval(10, 10, 340, 90, fill="#ADD8E6", outline="#ADD8E6", tags="nube")  # Cuerpo
        self.canvas_instrucciones.create_polygon(50, 90, 80, 110, 100, 90, fill="#ADD8E6", outline="#ADD8E6", tags="nube")  # Pico

    def configurar_juego(self):
        self.boton_iniciar.pack_forget()
        self.boton_instrucciones.pack_forget()
        self.label_bienvenida.pack_forget()

        # Preguntar por el modo de juego
        self.label_modo = tk.Label(self.ventana, text="Selecciona el modo de juego:", font=("Arial", 12))
        self.label_modo.pack(pady=10)

        self.boton_modo2 = tk.Button(self.ventana, text="2 Jugadores", command=self.modo_multijugador)
        self.boton_modo2.pack(pady=5)

    def modo_multijugador(self):
        self.solicitar_nombres()

    def solicitar_nombres(self):
        # Limpiar la pantalla
        self.label_modo.pack_forget()
        self.boton_modo2.pack_forget()

        # Etiqueta de instrucciones
        self.label_instrucciones = tk.Label(self.ventana, text="Introduce el nombre de los jugadores", font=("Arial", 12))
        self.label_instrucciones.pack(pady=10)

        # Entrada para el nombre del jugador 1
        self.label_jugador1 = tk.Label(self.ventana, text="Nombre Jugador 1:", font=("Arial", 12))
        self.label_jugador1.pack(pady=5)
        self.entrada_jugador1 = tk.Entry(self.ventana, font=("Arial", 14))
        self.entrada_jugador1.pack(pady=5)

        # Entrada para el nombre del jugador 2
        self.label_jugador2 = tk.Label(self.ventana, text="Nombre Jugador 2:", font=("Arial", 12))
        self.label_jugador2.pack(pady=5)
        self.entrada_jugador2 = tk.Entry(self.ventana, font=("Arial", 14))
        self.entrada_jugador2.pack(pady=5)

        # Botón para confirmar nombres e iniciar el juego
        self.boton_confirmar_nombres = tk.Button(self.ventana, text="Confirmar Nombres",
                                                 command=self.guardar_nombres,
                                                 font=("Arial", 12))
        self.boton_confirmar_nombres.pack(pady=10)

    def guardar_nombres(self):
        self.jugador1 = self.entrada_jugador1.get() or "Jugador 1"
        self.jugador2 = self.entrada_jugador2.get() or "Jugador 2"

        # Limpiar pantalla y empezar el juego
        self.label_instrucciones.pack_forget()
        self.label_jugador1.pack_forget()
        self.entrada_jugador1.pack_forget()
        self.label_jugador2.pack_forget()
        self.entrada_jugador2.pack_forget()
        self.boton_confirmar_nombres.pack_forget()

        # Iniciar las notificaciones en paralelo con el juego
        self.mostrar_instrucciones_secuencial()
        self.iniciar_ronda()

    def iniciar_ronda(self):
        # Reiniciar el tiempo y cancelar temporizadores previos
        self.cancelar_temporizador()
        self.tiempo_restante = self.tiempo_limite

        # Etiqueta de instrucciones
        self.label_operacion = tk.Label(self.ventana, text="", font=("Arial", 16))
        self.label_operacion.pack(pady=10)

        # Entrada para la respuesta
        self.entrada_respuesta = tk.Entry(self.ventana, font=("Arial", 14))
        self.entrada_respuesta.pack(pady=10)
        self.entrada_respuesta.bind("<Return>", lambda event: self.verificar_respuesta())

        # Botón para enviar la respuesta
        self.boton_enviar = tk.Button(self.ventana, text="Enviar Respuesta", command=self.verificar_respuesta,
                                      font=("Arial", 12))
        self.boton_enviar.pack(pady=5)

        # Cronómetro
        self.label_cronometro = tk.Label(self.ventana, text=f"Tiempo restante: {self.tiempo_limite} segundos",
                                         font=("Arial", 12))
        self.label_cronometro.pack(pady=10)

        # Etiqueta de resultados
        self.label_resultados = tk.Label(self.ventana, text="")
        self.label_resultados.pack(pady=10)

        # Mostrar puntajes
        self.label_puntajes = tk.Label(self.ventana,
                                       text=f"{self.jugador1}: {self.puntaje_jugador1} puntos | {self.jugador2}: {self.puntaje_jugador2} puntos")
        self.label_puntajes.pack(pady=5)

        # Botón para finalizar el juego
        self.boton_finalizar = tk.Button(self.ventana, text="Finalizar Juego", command=self.finalizar_juego,
                                         font=("Arial", 12))
        self.boton_finalizar.pack(pady=10)

        # Generar una operación nueva
        self.nueva_operacion()

    def nueva_operacion(self):
        self.cancelar_temporizador()  # Cancelar cualquier temporizador previo
        self.tiempo_restante = self.tiempo_limite
        a, b, operador = self.generar_operacion_sencilla()
        self.resultado_correcto = self.calcular_resultado(a, b, operador)

        # Limpiar la entrada de respuesta
        self.entrada_respuesta.delete(0, tk.END)  # Vaciar la entrada de texto

        # Actualizar la etiqueta con la operación
        jugador_actual = self.jugador1 if self.turno == 1 else self.jugador2
        self.label_operacion.config(text=f"{jugador_actual}, resuelve: {a} {operador} {b}")

        # Reiniciar el cronómetro
        self.actualizar_cronometro()

    def generar_operacion_sencilla(self):
        operadores = ['+', '-', '*', '/']
        operador = random.choice(operadores)
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        if operador == '/':
            a = a * b  # Asegurarse de que la división sea exacta
        return a, b, operador

    def calcular_resultado(self, a, b, operador):
        if operador == '+':
            return a + b
        elif operador == '-':
            return a - b
        elif operador == '*':
            return a * b
        elif operador == '/':
            return a // b  # División entera

    def verificar_respuesta(self):
        try:
            respuesta = int(self.entrada_respuesta.get())
        except ValueError:
            self.label_resultados.config(text="Respuesta inválida. Por favor, ingresa un número.")
            return

        if respuesta == self.resultado_correcto:
            self.label_resultados.config(text="¡Correcto!")
            if self.turno == 1:
                self.puntaje_jugador1 += 10
            else:
                self.puntaje_jugador2 += 10
        else:
            self.label_resultados.config(text=f"Incorrecto. La respuesta era {self.resultado_correcto}.")

        # Actualizar puntajes
        self.label_puntajes.config(
            text=f"{self.jugador1}: {self.puntaje_jugador1} puntos | {self.jugador2}: {self.puntaje_jugador2} puntos")

        # Cambiar de turno
        self.turno = 2 if self.turno == 1 else 1
        self.nueva_operacion()

    def actualizar_cronometro(self):
        if self.tiempo_restante > 0:
            self.label_cronometro.config(text=f"Tiempo restante: {self.tiempo_restante} segundos")
            self.tiempo_restante -= 1
            self.temporizador_id = self.ventana.after(1000, self.actualizar_cronometro)
        else:
            self.label_resultados.config(text="¡Tiempo agotado!")
            self.verificar_respuesta()

    def cancelar_temporizador(self):
        if self.temporizador_id is not None:
            self.ventana.after_cancel(self.temporizador_id)
            self.temporizador_id = None

    def finalizar_juego(self):
        self.cancelar_temporizador()
        ganador = self.jugador1 if self.puntaje_jugador1 > self.puntaje_jugador2 else self.jugador2
        if self.puntaje_jugador1 == self.puntaje_jugador2:
            ganador = "¡Empate!"
        messagebox.showinfo("Fin del Juego", f"El juego ha terminado.\nPuntajes finales:\n"
                                             f"{self.jugador1}: {self.puntaje_jugador1} puntos\n"
                                             f"{self.jugador2}: {self.puntaje_jugador2} puntos\n"
                                             f"Ganador: {ganador}")

        self.ventana.quit()


# Ejecutar el juego
ventana = tk.Tk()
juego = BatallaMatematica(ventana)
ventana.mainloop()
