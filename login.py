#trabalho-cesmac
#aluno-brendow

import PySimpleGUI as pt   #usei a biblioteca PySimpleGUI para interfaces
from fila import Fila  #importando a fila
from main import insere_medico,main,insere_pets,select_medicos,select_pets,consulta_clinica,select_consulta
from conex import criar_conexao,fechar_conexao



br=Fila()



#layout
def login():   #primeira janela
    pt.theme('Reddit')
    layout=[
      [pt.Text('Informe seu login:')],
      [pt.Input()],
      [pt.Button('Entrar')]
    ]

    return pt.Window('clínica veterinária',layout=layout,finalize=True)

#outro layout
def login_acessado():   #segunda janela
    pt.theme('Reddit')
    layout=[
       [pt.Text('Senha para fila')],
       [pt.Button('nova senha'),pt.Button('chamada de senha')],
       [pt.Text('Pet')],
       [pt.Button('Cadastrar')],
       [pt.Button('Listar')],
       [pt.Text('Médico veterinário')],
       [pt.Button('cadastrar')],
       [pt.Button('listar')],
       [pt.Text('Consulta')],
       [pt.Button('CADASTRAR')],
       [pt.Button('LISTAR')],
       [pt.Button('Voltar')]

    ]

    return pt.Window('clínica veterinária',layout=layout,finalize=True)


#janelas
janela1,janela2=login(), None

#eventos
while True:
    window,event,values=pt.read_all_windows()
    #quando a janela for fechada
    if window==janela1 and event==pt.WIN_CLOSED:
        break
    if window==janela2 and event==pt.WIN_CLOSED:
        break

    if window==janela1 and event == 'Entrar':
        janela2=login_acessado()
        janela1.hide()
    if window==janela2 and event =='Voltar':
        janela2.hide()
        janela1.un_hide()
    if window==janela2 and event=='nova senha':  #informando nova senha
        x = input(" Informe sua senha -> ")
        br.inserir(x)
    if window==janela2 and event == 'chamada de senha':  #chamando a senha em ordem de fila
        print('Chamando senha -> '+ str(br.chamando()))
    if window==janela2 and event== 'cadastrar': #cadastrar medico
        con=criar_conexao("127.0.0.1","root","","clinicaveterinaria")
        print("     - - -  CADASTRO DO MEDICO - -  -")
        x=input("informe seu crmv=")
        z=input("informe seu nome=")
        b=input("informe seu cpf=")
        insere_medico(con,x,z,b)
        fechar_conexao(con)
    if window==janela2 and event== 'Cadastrar': #inserir pet
        con=criar_conexao("127.0.0.1","root","","clinicaveterinaria")
        print("     - - -  CADASTRO DO CLIENTE - -  -")
        x=input("informe nome do dono=")
        z=input("informe nome do pet=")
        b=input("informe a raça=")
        c=input("informe o cpf do dono=")
        insere_pets(con,x,z,b,c)
        fechar_conexao(con)
    if window==janela2 and event=='listar': #mostrar os veterinarios cadastrados
        con=criar_conexao("127.0.0.1","root","","clinicaveterinaria")
        print("     - - -  VETERINARIOS CADASTRADOS - -  -")
        select_medicos(con)
        fechar_conexao(con)
    if window==janela2 and event=='Listar': #mostrar os pets cadastrados
        con=criar_conexao("127.0.0.1","root","","clinicaveterinaria")
        print("     - - -  CLIENTES CADASTRADOS - -  -")
        select_pets(con)
        fechar_conexao(con)
    if window==janela2 and event=='CADASTRAR': # cadastrar consulta
        con=criar_conexao("127.0.0.1","root","","clinicaveterinaria")
        print("     - - -  CADASTRO DA CONSULTA - -  -")
        x=input("informe o cpf do cliente=")
        z=input("informe nome do pet=")
        b=input("informe a prescricao medica feita=")
        consulta_clinica(con,x,z,b)
        fechar_conexao(con)
    if window==janela2 and event=='LISTAR': #mostrar as consultas cadastradas
        con=criar_conexao("127.0.0.1","root","","clinicaveterinaria")
        print("     - - -  CONSULTAS CADASTRADAS - -  -")
        select_consulta(con)
        fechar_conexao(con)




    
       

       


    


        
          
    
        