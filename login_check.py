class contas:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.rnome = []
        self.rsenha = []

    def reg(self):
        if a1.nome in self.rnome:
            print('Login já existente')
        else:
            self.rnome.append(a1.nome)
            self.rsenha.append(a1.senha)

    def login(self):
        try:
            check = self.rnome.index(a1.nome)
            if self.rsenha[check] == a1.senha:
                print('Login OK!')
            else:
                print('Senha ou login invalidos')
        except:
            print('Senha ou login invalidos')


nova_con = ['_']
n = str(input('É novo aqui? S/N' )).upper()

for x in nova_con:
    a1 = contas(str(input('Login: ')), input('Senha: '))
    if n == 'S':
        a1.reg()
        ncon = (input('Fazer login? S/N')).upper()
        if ncon == 'S':
            nova_con.append('')
        else:
            print('Obrigado!')
    elif n == 'N':
        a1.login()




