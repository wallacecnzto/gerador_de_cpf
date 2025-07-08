cpf_do_usuario = input("Digite seu CPF (apenas números): ").strip().casefold()
comprimento_do_cpf = 11

while len(cpf_do_usuario) != comprimento_do_cpf:
    print("Tamanho inválido!")
    cpf_do_usuario = input("Digite seu CPF (apenas números): ").strip().casefold()

