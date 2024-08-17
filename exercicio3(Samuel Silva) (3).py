def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial):  # Define a função diagnosticar_diabetes

    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200:  # Se a glicemia em jejum for maior ou igual a 126 ou a glicemia pós-prandial for maior ou igual a 200
        return "Diabetes"  # Retorna como diabetes se a glicemia bater
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:  # Senão, se a glicemia em jejum for entre 100 e 125 ou a glicemia pós-prandial for entre 140 e 199
        return "Pré-diabetes"  # Retorna como pré-diabetes se o valor bater
    else:  # Senão
        return "Normal"  # Retornará o valor como normal

glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): "))  # Pede para o usuário digitar o valor em jejum
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))  # Pede para o usuário digitar o valor da glicemia pós-prandial

resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)  # Calcula o resultado chamando a função diagnosticar_diabetes
print(f"O diagnóstico é: {resultado}")  # Exibe para o usuário o resultado
