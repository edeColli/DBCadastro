import categoria
import produto
print("Bem vindo ao sistema de cadastro!")

while True:
    opcao = int(
        input("Escolha uma opção \n1-Cadastrar Categoria\n2-Cadastrar Produto\n3-Listas Categorias\n4-Listar Produtos\n5-Atualizar Categoria\n6-Atualizar Produtos\n7-Excluir Categoria\n8-Excluir Produto\n0-Sair\n"))

    if opcao == 0:
        break
    elif opcao == 1:
        categoria.cadastrar_categoria()
    elif opcao == 2:
        produto.cadastrar_produto()
    elif opcao == 3:
        categoria.listar_categoria()
    elif opcao == 4:
        produto.listar_produto()
    elif opcao == 5:
        categoria.atualizar_categoria()
    elif opcao == 6:
        produto.atualizar_produto()
    elif opcao == 7:
        categoria.excluir_categoria()
    elif opcao == 8:
        produto.excluir_produto()
    else:
        print("\nOpção inválida!\n")
