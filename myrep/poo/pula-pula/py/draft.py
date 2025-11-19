class Crianca:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:
        return f"{self.nome}:{self.idade}"


class PulaPula:
    def __init__(self) -> None:
        self.espera = []
        self.pulaPula = []

    def __str__(self) -> str:
        espera = ", ".join([str(x) for x in self.espera])
        pulaPula = ", ".join([str(x) for x in self.pulaPula])
        return f"[{espera}] => [{pulaPula}]"

    def arrive(self, nome: str, idade: int):
     
        self.espera.insert(0, Crianca(nome, idade))

    def enter(self):
      
        if self.espera:
            crianca = self.espera.pop()
            self.pulaPula.insert(0, crianca)
        else:
            print("fail: ninguém na fila")

    def leave(self):

        if self.pulaPula:
            crianca = self.pulaPula.pop()
            self.espera.insert(0, crianca)
    def remove(self, nome: str):
        for i, x in enumerate(self.espera):
            if x.nome == nome:
                del self.espera[i]
                return
        for i, x in enumerate(self.pulaPula):
            if x.nome == nome:
                del self.pulaPula[i]
                return

        print(f"fail: {nome} nao esta no pula-pula")

def main():
    pula = PulaPula()
    while True:
        line = input().strip()
        if not line:
            continue
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "arrive":
            pula.arrive(args[1], int(args[2]))
        elif args[0] == "enter":
            pula.enter()
        elif args[0] == "leave":
            pula.leave()
        elif args[0] == "remove":
            pula.remove(args[1])
        elif args[0] == "show":
            print(pula)

main()
