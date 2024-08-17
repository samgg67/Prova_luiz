def calcular_area_comodos():  # Define a função de calcular_area_comodos
    total_area = 0  # Recebe o valor de 0 na area total no inicio do código

    while True:  # Loop para as proximas perguntas e comando até o break
        largura = float(input("Digite a largura do cômodo (em metros): "))  # Pergunta para o usuario a largura
        comprimento = float(input("Digite o comprimento do cômodo (em metros): "))  # Pergunta para o usuario o comprimento

        area_comodo = largura * comprimento  # define a area_comodo como largura vezes o comprimento
        print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.")  # Printa para o usuario o tamanho da area do comodo usando area_comodo

        total_area += area_comodo  # atualiza a area

        mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()  # comando que pergunta para o usuario se quer adicionar mais comodos
        if mais_comodos != 's':  # Fala que SE o valor de mais_comados for = a (s) continua o loop, se não passa para o break
            break  # Quebra o loop

    return total_area  # Retorna o valor

area_total = calcular_area_comodos()  # Area total é igual a area dos comodos
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")  # Printa para o usuario a area total.
