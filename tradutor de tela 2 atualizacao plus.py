import tkinter as tk
import requests
import mss
import mss.tools
import keyboard
import time
from deep_translator import GoogleTranslator

API_KEY = "suakey"

def mostrar_traducao(texto, traducao):
    popup = tk.Tk()
    popup.title("Tradução")
    popup.geometry("400x200")
    tk.Label(popup, text="Texto original:", font=("Arial", 12, "bold")).pack(pady=5)
    tk.Label(popup, text=texto, wraplength=380, justify="left").pack(pady=5)
    tk.Label(popup, text="Tradução:", font=("Arial", 12, "bold")).pack(pady=5)
    tk.Label(popup, text=traducao, wraplength=380, justify="left", fg="blue").pack(pady=5)
    popup.mainloop()

def capturar_area(x1, y1, x2, y2):
    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)

    with mss.mss() as sct:
        monitor = {"top": top, "left": left, "width": width, "height": height}
        img = sct.grab(monitor)
        mss.tools.to_png(img.rgb, img.size, output="tela_selecionada.png")

    with open("tela_selecionada.png", "rb") as f:
        response = requests.post(
            "https://api.ocr.space/parse/image",
            files={"file": f},
            data={"apikey": API_KEY, "language": "eng"}
        )

    if response.status_code == 200 and "ParsedResults" in response.json():
        result = response.json()
        texto_extraido = result["ParsedResults"][0]["ParsedText"]
        if texto_extraido.strip():
            traducao = GoogleTranslator(source='auto', target='pt').translate(texto_extraido)
            mostrar_traducao(texto_extraido, traducao)
    else:
        print("Erro na requisição OCR:", response.text)

def selecionar_area():
    coords = {}
    rect_id = None

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.3)
    canvas = tk.Canvas(root, cursor="cross")
    canvas.pack(fill="both", expand=True)

    def iniciar(event):
        nonlocal rect_id
        coords["x1"], coords["y1"] = event.x, event.y
        rect_id = canvas.create_rectangle(event.x, event.y, event.x, event.y, outline="red", width=2)

    def arrastar(event):
        if rect_id:
            canvas.coords(rect_id, coords["x1"], coords["y1"], event.x, event.y)

    def finalizar(event):
        coords["x2"], coords["y2"] = event.x, event.y
        root.destroy()
        capturar_area(coords["x1"], coords["y1"], coords["x2"], coords["y2"])

    canvas.bind("<ButtonPress-1>", iniciar)
    canvas.bind("<B1-Motion>", arrastar)
    canvas.bind("<ButtonRelease-1>", finalizar)

    root.mainloop()

print("Pressione F9 para selecionar área e traduzir. Pressione ESC para sair.")

while True:
    if keyboard.is_pressed("F9"):
        selecionar_area()
        time.sleep(1)  # evita múltiplos disparos
    elif keyboard.is_pressed("esc"):
        print("Encerrando programa...")
        break
    time.sleep(0.1)
