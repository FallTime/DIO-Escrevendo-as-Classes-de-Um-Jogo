class Heroi:

    def __init__(self, name, age, tipo):
        self.name = name
        self.age = age
        self.tipo = tipo

    @staticmethod
    def atacar(self):
        match self.tipo:
            case "mago":
                print("O", self.tipo, "atacou usando", "magia")
            case "guerreiro":
                print("O", self.tipo, "atacou usando", "espada")
            case "monge":
                print("O", self.tipo, "atacou usando", "artes marciais")
            case "ninja":
                print("O", self.tipo, "atacou usando", "shuriken")
            case _:
                print("Tipo não existe")

exemplo = Heroi("Jubileu", 23, "mago")
exemplo.atacar(exemplo)