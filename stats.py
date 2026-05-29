def get_book_text(filepath):
    with open(filepath, "r") as f:
        texto = f.read()
        return texto
    
def get_num_words(text):
    texto_dividido = text.split()
    largo = len(texto_dividido)
    return largo

def contar_veces(text):
    dicc = {}
    for chart in text:
        chart = chart.lower()
        if chart in dicc:
            dicc[chart] += 1
        else:
            dicc[chart] = 1
    return dicc

def sorted_list(diccionario):
    lista = []
    for letra, cantidad in diccionario.items():      
        lista.append({"char": letra, "num": cantidad})
    lista.sort(key=lambda di: di["num"], reverse=True)
    return lista

def top_words(text, n=10):
    words = text.lower().split()
    dicc = {}
    for word in words:
        word = ''.join(c for c in word if c.isalpha())
        if word:
            if word in dicc:
                dicc[word] += 1
            else:
                dicc[word] = 1
    sorted_words = sorted(dicc.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]