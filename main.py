from categoria import Categoria
from produto import Produto

def main():
    cVerduras = Categoria("Verduras", "hortaliças, folhas, talos tenros e comestíveis")
    cFrios = Categoria("Frios", "carnes processadas, cozidas e consumidas frias")
    pAlface = Produto("Alface", "verde", "21/03/2025", True, cVerduras)
    pGuisado = Produto("Guisado", "Carne moida", "25/05/2025", True, cFrios)

    print(cVerduras)
    print(cFrios)
    print(pAlface)
    print(pGuisado)

if __name__ == "__main__": 
    main()