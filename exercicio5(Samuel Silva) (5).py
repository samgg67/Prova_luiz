def calcular_imc(peso, altura):  # Define que quer calcular o IMC definindo peso e altura
    imc = peso / (altura ** 2)  # Calcula o IMC
    return imc  # Retorna o IMC

def classificar_imc(imc):  # Define a função para classificar o IMC
    if imc < 18.5:  # Se o IMC for menor que 18.5
        return "Abaixo do peso"  # Retorna abaixo do peso
    elif 18.5 <= imc < 24.9:  # Senão, se o IMC for maior ou igual a 18.5 e menor que 24.9
        return "Peso normal"  # Retorna peso normal
    elif 25 <= imc < 29.9:  # Senão, se o IMC for maior ou igual a 25 e menor que 29.9
        return "Sobrepeso"  # Retorna como sobrepeso
    elif 30 <= imc < 34.9:  # Senão, se o IMC for maior ou igual a 30 e menor que 34.9
        return "Obesidade grau 1"  # Retorna obesidade grau 1
    elif 35 <= imc < 39.9:  # Senão, se o IMC for maior ou igual a 35 e menor que 39.9
        return "Obesidade grau 2"  # Retorna obesidade grau 2
    else:  # Senão
        return "Obesidade grau 3"  # Retorna obesidade grau 3

def sugestao_atividade_fisica(classificacao_imc):  # Define a função sugestao_atividade_fisica baseada na classificação do IMC
    if classificacao_imc == "Abaixo do peso":  # Se o IMC for abaixo do peso
        return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em proteínas e calorias."  # Retorna esse texto
    elif classificacao_imc == "Peso normal":  # Senão, se o IMC for peso normal
        return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e natação, junto a um treino de força moderado."  # Retorna esse texto
    elif classificacao_imc == "Sobrepeso":  # Senão, se o IMC for sobrepeso
        return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além de exercícios de resistência."  # Retorna esse texto
    elif classificacao_imc == "Obesidade grau 1":  # Senão, se o IMC for obesidade grau 1
        return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um programa de reeducação alimentar."  # Retorna esse texto
    elif classificacao_imc == "Obesidade grau 2":  # Senão, se o IMC for obesidade grau 2
        return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e acompanhamento nutricional."  # Retorna esse texto
    else:  # Senão
        return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica, fisioterapia, e consultas regulares com um nutricionista."  # Retorna esse texto

peso = float(input("Digite seu peso (em kg): "))  # Pede para o usuário digitar o peso
altura = float(input("Digite sua altura (em metros): "))  # Pede a altura
imc = calcular_imc(peso, altura)  # Calcula o IMC
classificacao_imc = classificar_imc(imc)  # Classifica o IMC
sugestao = sugestao_atividade_fisica(classificacao_imc)  # Sugere atividades físicas baseada na classificação do IMC

print(f"Seu IMC é: {imc:.2f}")  # Exibe para o usuário o IMC
print(f"Classificação: {classificacao_imc}")  # Exibe para o usuário a classificação
print(f"Sugestão de atividade física: {sugestao}")  # Exibe para o usuário a sugestão de atividade física
