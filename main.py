from conex import criar_conexao,fechar_conexao


def insere_medico(con,crmv,nome,cpf):
    cursor = con.cursor()
    sql = "INSERT INTO medico(crmv,nome,cpf) values (%s,%s,%s)"
    valores= (crmv,nome,cpf)
    cursor.execute(sql,valores)
    cursor.close()
    con.commit()

def select_medicos(con):
    consulta_sql="select * from medico"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas=cursor.fetchall()
    print("numero de registros retornados: ", cursor.rowcount)

    print("Mostrando os médicos cadastros:")
    for linha in linhas:
        print("crmv:",linha[0])
        print("nome:",linha[1])
        print("cpf:",linha[2])


def insere_pets(con,dono,nome,raça,cpf_dono):
    cursor = con.cursor()
    sql = "INSERT INTO pets(dono,nome,raça,cpf_dono) values (%s,%s,%s,%s)"
    valores = (dono,nome,raça,cpf_dono)
    cursor.execute(sql,valores)
    cursor.close()
    con.commit()

def select_pets(con):
    consulta_sql="select * from pets"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas=cursor.fetchall()
    print("numero de registros retornados: ", cursor.rowcount)

    print("Mostrando os pets cadastros:")
    for linha in linhas:
        print("dono:",linha[0])
        print("nome:",linha[1])
        print("raça:",linha[2])
        print("cpf_dono:",linha[3])


def consulta_clinica(con,cpf_cliente,nome_animal,prescricao):
    cursor = con.cursor()
    sql = "INSERT INTO consulta(cpf_cliente,nome_animal,prescricao) values (%s,%s,%s)"
    valores = (cpf_cliente,nome_animal,prescricao)
    cursor.execute(sql,valores)
    cursor.close()
    con.commit()

def select_consulta(con):
    consulta_sql="select * from consulta"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas=cursor.fetchall()
    print("numero de registros retornados: ", cursor.rowcount)

    print("Mostrando as consultas registradas:")
    for linha in linhas:
        print("cpf do cliente:",linha[0])
        print("nome do animal:",linha[1])
        print("prescricao:",linha[2])

def main():
    con=criar_conexao("127.0.0.1","root","","clinicaveterinaria")
    
    
    #insere_medico(con,900888,'tacyanna','55566699910')
    #insere_pets(con,'Matheus','Belinha','chihuauha')
    

    fechar_conexao(con)



if __name__=="__main__":
    main()
