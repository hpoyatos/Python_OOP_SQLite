class Pessoa:
  #Atributos
  id = None
  nome = None

  #Método Construtor
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome

  #Método para ajudar na exibição
  def __str__(self):
    return f"{self.nome} ({self.id})"