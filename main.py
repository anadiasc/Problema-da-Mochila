import json


aporte = []
vpl = []

"""
p = [1,2,3]
v = [60,50,120]
"""

def getArquivo(nome_arquivo): #função usada para ler o arquivo onde estão armazenados os investimentos que serão analizados
    with open(f'{nome_arquivo}.json','r') as arquivo:
            conteudo = arquivo.read()
            retorno = json.loads(conteudo)
            
            return retorno

def inserirDados(vetorAporte, vetorVpl):
    arquivo = getArquivo("invest")
    
    for j in range(100):
        vetorAporte.append(arquivo["investimentos"][j]["aporte"])
        vetorVpl.append(arquivo["investimentos"][j]["vpl"])
    
inserirDados(aporte,vpl)

def ecolher_item(cap,n):
    if (n==0):
        return 0
    else:
        if (aporte[n-1]>cap):
            return ecolher_item(cap, n-1)
        else:
            return max(vpl[n-1]+ecolher_item(cap-aporte[n-1],n-1), ecolher_item(cap,n-1))
        
def max (valor1, valor2):
    if(valor1>valor2):
        return valor1
    else:
        return valor2
    

print(ecolher_item(100000,100))
