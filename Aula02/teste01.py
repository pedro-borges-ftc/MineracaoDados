print("Ola Mundo")

valor = 8
print("Valor: ", valor)

idade = 40
peso = 74.5
altura = 1.65

print("Idade: ", type(idade))
print("Peso: ", type(peso))
print("Altura: ", altura)

alunos = ["fulano","beltrano",8,True,altura]
print("Alunos: ", alunos)
print("Primeiro aluno: ", alunos[0])
print("ultima aluno: ", alunos[4])

for i in range(5):
    print("Aluno na posicao", i+1, ":", alunos[i])