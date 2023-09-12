import pyautogui
import time
import pyperclip

# Otorga tiempo para ir a donde se quiere insertar el texto
time.sleep(3)

# Ruta del archivo de texto a leer
file_path = "example.txt"

# Abre el archivo en modo lectura
with open(file_path, "r", encoding="utf-8") as file:
    # Lee todo el contenido del archivo
    lines = file.readlines()

# Inicializa una variable para almacenar el texto
text_to_send = ""

# Itera a través de las líneas del archivo
for line in lines:
    # Si encuentra una línea con 40 guiones seguidos, copia el texto antes de eso
    if line.strip() == "-" * 40:
        if text_to_send:
            pyperclip.copy(text_to_send)
            pyautogui.hotkey("ctrl", "v")  # Pega el texto
            pyautogui.press("enter")  # Presiona Enter para enviar el texto
            time.sleep(5)
            text_to_send = ""  # Reinicia el texto a enviar
    else:
        text_to_send += line  # Agrega la línea actual al texto a enviar
        
# Maneja el último fragmento de texto si es necesario
if text_to_send:
    pyperclip.copy(text_to_send)
    pyautogui.hotkey("ctrl", "v")  # Pega el texto
    pyautogui.press("enter")  # Presiona Enter para buscar
    time.sleep(5)
