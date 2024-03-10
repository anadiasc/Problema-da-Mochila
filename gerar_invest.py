import random
import json


"""
VARIÁVEIS: 
ID_INVESTIMENTO | APORTE INICIAL | VPL
"""
def gerar_aporte():
    aporte = random.randint(100,100000)

    return aporte

#print(gerar_aporte())

def gerar_vpl(): # VPL - VALOR PRESENTE LÍQUIDO
    vpl = random.randint(101,150000)
    return vpl

#print(gerar_vpl())

def criarArquivo(nome_arquivo):
    with open(f'{nome_arquivo}.json','w') as arquivo:
        for i in range(100):
            arquivo.write("\n{")
            
            arquivo.write(f'\n"aporte":{gerar_aporte()},\n"vpl":{gerar_vpl()}\n')
            
            arquivo.write("},\n")

criarArquivo("invest")