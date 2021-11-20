def fila():
    fila = []
    while(True):
        print("1 - Cadastrar Aluno ")
        print("2 - Retirar Aluno")
        print("3 - Mostrar Fila")
        print("4 - Sair do programa")
        opcao = int(input("->"))
        
        if opcao == 1:
                nome = (str(input("Nome do aluno: ")))
                fila.append(nome)
        
                matricula = (int(input("Numero da matricula: ")))
                fila.append(matricula)
        
                nota1 = float(input("Nota 1: "))
                nota2 = float(input("Nota 2: "))
            
                media = (nota1 + nota2)/2
                
                if media > 7:
                    fila.append("Aprovado!")
                else:
                    fila.append("Reprovado!")
            
        
        elif opcao == 2:
            print("Aluno Retirado!")
            del fila[0:3]
        
        elif opcao == 3:
            print("\n", fila)
        
        elif opcao == 4:
            break
        else:
            print("Opção Invalida")
            
fila()
