from http import client
from unittest import result


print("------------------")
print("-----cheques------")
print("------------------")

billetes =[10000,2000,100]
dinero_dar= int(input("-->"))

def operaciones (dinero_dar):
    result= []
    for b in billetes:
        if b== dinero_dar:
            print("un billete de",b)
            exit()
        cant_billetes_dar= dinero_dar//b
        if cant_billetes_dar<0:
            break
        if cant_billetes_dar !=0:
            result.append()
