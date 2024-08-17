def calcular_media_e_aprovacao(notas, nota_minima_aprovacao):  # Define a função para calcular_media_e_aprovacao e define os valores.
    total_notas = 0  # Começa com o valor 0 em total_notas
    num_alunos = len(notas)  # Recebe o número de alunos
    aprovados = []  # Recebe os aprovados
    reprovados = []  # Recebe os reprovados

    for aluno, nota in notas.items():  # Loop para receber os dados dos alunos
        total_notas += nota  # Soma a nota no total de notas
        if nota >= nota_minima_aprovacao:  # Se a nota for maior ou igual à nota mínima para aprovação
            aprovados.append(aluno)  # Adiciona o aluno à lista de aprovados
        else:  # Senão
            reprovados.append(aluno)  # Adiciona o aluno à lista de reprovados

    media_turma = total_notas / num_alunos  # Calcula a média da turma

    return media_turma, aprovados, reprovados  # Retorna a média da turma, aprovados e reprovados

notas = {
    "Alice": 85,
    "Bruno": 72,  # notas
    "Carlos": 60,
    "Diana": 95,
    "Eduardo": 55
}

nota_minima_aprovacao = 70  # Define a nota mínima para aprovação 

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)

print(f"Média da turma: {media_turma:.2f}")  # Exibe a média da turma
print(f"Alunos aprovados: {', '.join(aprovados)}")  # Exibe os alunos aprovados
print(f"Alunos reprovados: {', '.join(reprovados)}")  # Exibe os alunos reprovados
