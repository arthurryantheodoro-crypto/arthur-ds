#codigo identifica se tem permissao para 
#assistir filmes +16
idade = int(input("digite sua idade"))
#so aceita meu numero inteiro
if idade  >= 16:
    print("entrada permitida!")
else:
    print("entrada nao permitida!")