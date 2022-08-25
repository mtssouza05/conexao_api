from fastapi import FastAPI

app = FastAPI()
conexao=app.get("http://127.0.0.1:8000/")

cod=True
tot=0
resp=[]
nome=[]
notas=[]
gabarito=['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
maior=0
menor=9999
apro=0
rec=0
repro=0
tot_notas=0
situacao_=[]
matricula=[]
matricula_s=[]
notas_s=[]


while cod:
    tot+=1
    nota=0  
    resp.clear() #limpar um vetor
    c=input('Nome: ')
    nome.append(c)
    d=input('Matricula: ')
    matricula.append(d)
    for x in range(10):
    
        y=input(f'Sua Resposta da questão {x+1}: ')
        i=y.upper()
        resp.append(i)

        if resp[x]==gabarito[x]:
            nota+=1
    

    notas.append(nota)
    tot_notas+=nota

    cod=input("Mais algum aluno irá se registrar ? Aperte 'n' para interromper o programa ou qualquer tecla para continuar: ")
    if cod=='n':
        cod=False
        print("FIM DO PROGRAMA")


print()
        
x=0
for x in range(x, tot, 1):
    if notas[x]>maior:
        maior=notas[x]
    if notas[x]<menor:
        menor=notas[x]


        
    if notas[x]>=7:
        apro+=1 
        situacao_.append("APROVADO")
        print(f'Nome: {nome[x]}')
        print(situacao_[x])

    elif notas[x]<7 and notas[x]>=5:
        rec+=1
        situacao_.append("RECUPERACAO")
        print(f'Nome: {nome[x]}')
        print(situacao_[x])
    else:
        repro+=1
        situacao_.append("REPROVADO")
        print(f'Nome: {nome[x]}')
        print(situacao_[x])

    matricula_s.append(str(matricula[x]))
    notas_s.append(str(notas[x]))
    
    
    alunos_info=app.post("http://127.0.0.1:8000/entrada/{matricula_s[x]},{nome[x]},{notas_s[x]},{situacao_[x]}")

    
    


print()

media_turma=0
media_turma=tot_notas/tot


print("----Relatório geral da Turma----")
print(f'Alunos Aprovados: {apro}')
print(f'Alunos em Recuperação: {rec}')
print(f'Alunos Reprovados: {repro}')
print(f'Média da Turma: {media_turma:,.2f}')
print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')











