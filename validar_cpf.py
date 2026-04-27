def validar_cpf(cpf: str) -> bool:
    # 1. Limpeza: remove pontos e traços, deixando apenas os números
    cpf_limpo = ''.join(filter(str.isdigit, cpf))

    # 2. Verificação de tamanho: um CPF deve ter exatamente 11 dígitos
    if len(cpf_limpo) != 11:
        return False

    # 3. Verificação de CPFs com números repetidos (ex: 111.111.111-11)
    # A matemática falha ao identificar esses casos como inválidos, então barramos aqui.
    if cpf_limpo == cpf_limpo[0] * 11:
        return False

    # 4. Cálculo do primeiro dígito verificador
    # Multiplicamos os 9 primeiros dígitos por pesos decrescentes de 10 até 2
    soma_1 = sum(int(cpf_limpo[i]) * (10 - i) for i in range(9))
    digito_1 = (soma_1 * 10) % 11
    if digito_1 == 10:
        digito_1 = 0

    # 5. Cálculo do segundo dígito verificador
    # Multiplicamos os 10 primeiros dígitos por pesos decrescentes de 11 até 2
    soma_2 = sum(int(cpf_limpo[i]) * (11 - i) for i in range(10))
    digito_2 = (soma_2 * 10) % 11
    if digito_2 == 10:
        digito_2 = 0

    # 6. Validação final: verifica se os dígitos calculados são iguais aos fornecidos
    digitos_calculados = f"{digito_1}{digito_2}"
    digitos_informados = cpf_limpo[-2:]
    
    return digitos_calculados == digitos_informados

# Interface simples no terminal para o usuário interagir
if __name__ == "__main__":
    print("-" * 30)
    cpf_input = input("Digite o CPF para validação: ")
    print("-" * 30)
    
    if validar_cpf(cpf_input):
        print("CPF válido!")
    else:
        print("CPF inválido!")
    print("-" * 30)