import tkinter
from tkinter import messagebox
import requests

# Lógica da API
def buscarcep(cep):

    cep = cep.replace("-", "").strip()
    
    # Validação básica
    if len(cep) != 8 or not cep.isdigit():
        return None
        
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        resposta = requests.get(url, verify=False)
        dados = resposta.json()
        
        if dados.get("erro") or resposta.status_code != 200:
            return None
        
        endereco = {
            "rua": dados.get("logradouro"),
            "bairro": dados.get("bairro"),
            "cidade": dados.get("localidade"),
            "estado": dados.get("uf"),
            "cep": dados.get("cep")
        }
        return endereco
    except Exception:
        return None

def buscar_endereço():
    cep_digitado = cep_entry.get()
    resultado = buscarcep(cep_digitado)
    
    if resultado:
        # Formatar o texto
        texto_formatado = f"{resultado['rua']}, {resultado['bairro']}, {resultado['cidade']} - {resultado['estado']}, {resultado['cep']}"
        label_resultado.config(text=texto_formatado, fg="green")
    else:
        # se o CEP for Invalido 
        label_resultado.config(text="", fg="black")
        messagebox.showerror("Erro", "CEP não encontrado ou inválido!")

# Interface 
janela = tkinter.Tk()
janela.title("Verificador de CEP")
janela.geometry("400x300")


tkinter.Label(janela, text="Digite o CEP:", font=("Arial", 12)).pack(pady=10)

cep_entry = tkinter.Entry(janela, font=("Arial", 12), width=15)
cep_entry.pack(pady=5)

botao = tkinter.Button(janela, text="Consultar", command=buscar_endereço, font=("Arial", 10))
botao.pack(pady=15)

label_resultado = tkinter.Label(janela, text="", font=("Arial", 10), wraplength=350, justify="center")
label_resultado.pack(pady=20)

janela.mainloop()
