tarefas = []

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa ainda.")
        else:
            for i, t in enumerate(tarefas, start=1):
                print(f"{i}. {t}")

    elif opcao == "3":
        if len(tarefas) == 0:
            print("Nada para remover.")
        else:
            for i, t in enumerate(tarefas, start=1):
                print(f"{i}. {t}")
            remover = int(input("Digite o número da tarefa: "))
            if 1 <= remover <= len(tarefas):
                tarefas.pop(remover - 1)
                print("Tarefa removida!")
            else:
                print("Número inválido.")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")