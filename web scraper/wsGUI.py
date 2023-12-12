import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import tkinter.scrolledtext as scrolledtext

def scrape_quotes(url, output_text):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')

        output_text.delete(1.0, tk.END)

        for index, quote in enumerate(quotes, 1):
            text = quote.text.strip()
            output_text.insert(tk.END, f"Cita {index}: {text}\n")
    else:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"No se pudo acceder a la página. Código: {response.status_code}")

def copy_to_clipboard(output_text):
    text_to_copy = output_text.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(text_to_copy)
    root.update()

def clear_text(output_text):
    output_text.delete(1.0, tk.END)

def start_scraping():
    url = url_entry.get()
    scrape_quotes(url, output_text)

root = tk.Tk()
root.title("WS GUI")

url_label = ttk.Label(root, text="URL:")
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = ttk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

scrape_button = ttk.Button(root, text="Extraer", command=start_scraping)
scrape_button.grid(row=0, column=2, padx=10, pady=10)

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
output_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

copy_button = ttk.Button(root, text="Copiar", command=lambda: copy_to_clipboard(output_text))
copy_button.grid(row=2, column=0, padx=10, pady=10)

clear_button = ttk.Button(root, text="Borrar", command=lambda: clear_text(output_text))
clear_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()