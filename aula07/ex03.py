class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Medico:
    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao


class Exame:
    def __init__(self, medico, paciente, descricao, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado

    def  imprimir_exame(self):
        print(f'Nome do paciente: {self.paciente.nome}')
        print(f'CPF do paciente: {self.paciente.cpf}')
        print(f'idade do paciente: {self.paciente.idade}')
        print(f'Nome do medico: {self.medico.nome}')
        print(f'CRM do medico: {self.medico.crm}')
        print(f'Especializacao do medico: {self.medico.especializacao}')
        print(f'Descrcao do exame: {self.descricao}')
        print(f'Resultado do exame: {self.resultado}')

paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')  
exame01.imprimir_exame()						
# Deve exibir relatório com os dados do exame (inclusive os do médico e do paciente)


