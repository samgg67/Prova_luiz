def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso,): #Define a função calcular_juros_atraso e 
    
    taxa_juros_diaria = taxa_juros_anual / 365 / 100 #Calculo da taxa de juros diaria 
    juros = valor_principal * taxa_juros_diaria * dias_atraso # Calculo de juros

    valor_total = valor_principal + juros #Calculo do valor total
    return valor_total, juros #Vai retornar os valores de valor_total e juros

valor_principal = 1000.00 #Dá um valor númerico ao valor principal
taxa_juros_anual = 5.0 #Dá um valor npumerico a taxa_juros_anual
dias_atraso = 30 #Dá um valor númerico aos dias de atraso
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)
print(f"Valor total a ser pago: R${valor_total:.2f}") #Printa o valor a ser pago para o usuario usando o valor_total
print(f"Valor dos juros: R${juros:.2f}") #Printa o valor dos juros para o usuário usando juros.