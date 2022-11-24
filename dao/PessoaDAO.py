from model.Pessoa import Pessoa 

class PessoaDAO:
  conexao = None
  cursor = None

  def __init__(self, con, cur):
    self.conexao = con
    self.cursor = cur

  def getAll(self, orderBy = False):
    sql = "SELECT id, nome FROM pessoa "
    if orderBy == True:
      sql = sql + " ORDER BY nome"
    
    try:
      self.cursor.execute(sql)
      resultado = self.cursor.fetchall()

      pessoas = []
      for linha in resultado:
        pessoa = Pessoa(linha[0], linha[1])
        pessoas.append(pessoa)

      return pessoas
    except Exception as e:
      return e

  #Função/método para inserir no banco.
  def save(self, pessoa):
    sql = "INSERT INTO pessoa (nome) VALUES (%s)"

    try:
      self.cursor.execute(sql, pessoa.nome)
      self.conexao.commit()
      pessoa.id = self.cursor.lastrowid 
      return pessoa
    except Exception as e:
      return e


