import psycopg2
from fastapi import FastAPI

app = FastAPI()

def conexao():
    host='************'
    dbname='*******'
    user='**********'
    password='*************'

    cnn_str="host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)

    con=psycopg2.connect(cnn_str)
    
    return con

@app.post("/entrada/{matricula}, {nome}, {nota}, {situacao}")
def entrada_dados(matricula, nome, nota, situacao):
    con = conexao()
    cursor=con.cursor()
    
    cursor.execute("INSERT INTO alunos (matricula, nome, nota, situacao) VALUES (%s, %s, %s, %s);",(matricula, nome, nota, situacao))
    
    con.commit()  
    cursor.close()
    con.close()


##SEGUNDA PARTE


   
