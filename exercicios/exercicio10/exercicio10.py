tarefas = []

while True:
    print("\nGERENCIADOR DE TAREFAS")
    print("1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nTarefas:")
            for i, tarefa in enumerate(tarefas):
                print(i + 1, "-", tarefa)

    elif opcao == "2":
        nova = input("Digite a nova tarefa: ")
        tarefas.append(nova)
        print("Tarefa adicionada!")

    elif opcao == "3":
        numero = int(input("Digite o número da tarefa para remover: "))
        if numero <= len(tarefas):
            removida = tarefas.pop(numero - 1)
            print("Tarefa removida:", removida)
        else:
            print("Tarefa não encontrada.")

    elif opcao == "4":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida.")