from flask import Flask, request 
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, Flask"

@app.route('/item', methods=['POST'])
def post_item():
    data = request.get_json()
    sql = f"INSERT INTO todolist(item, status) VALUES('{dados['item']}','{data['status']}')"
    banco(sql)
    return data

def banco(sq1):
    resultado = ""
    try:
        # Conexão com o banco de dados PostgreeSQL
        conn = psycopg2.connect(
            host = "dpg-cuhumbbqf0us73dtcrv0-a.oregon-postgres.render.com",
            port = "5432",
            dbname = "senaidb_dryp",
            user = "senaidb_dryp_user",
            password = "fv4jzONY5kYKQ2ZALgqG7St2lZYp4OBe"
        )
        cursor = conn.cursor() # cursor vai ser a variável para executar os omenados SQL.
        cursor.execute(sql) # executar o comando sql seja insert, select .. etc
        cursor.close() # finalizar o cursor
        conn.commit() # confirma o comenado SQL
        conn.close() # finaliza a conexão
    except psycopg2.Error as e:
        print("Erro na conexão do banco de dados") 


if __name__ == '__main__':
    app.run(debug=True)