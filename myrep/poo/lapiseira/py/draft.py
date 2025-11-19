class Grafite:
    def __init__(self, calibre:float, dureza:str, tamanho:int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

    def gastoPorFolha(self):
        tabela = {"HB": 1, "2B": 2, "4B": 4, "6B": 6}
        return tabela[self.dureza]
    
    def __str__(self) -> str:
        return f"{self.calibre}:{self.dureza}:{self.tamanho}"
    
class Lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre
        self.bico: Grafite | None = None
        self.tambor: list[Grafite] = []
    
    def insert(self, grafite: Grafite):
        if grafite.calibre != self.calibre:
            print("fail: calibre incompatível")
            return
        self.tambor.append(grafite)

    def pull(self):
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
            return
        if len(self.tambor) == 0:
            print("fail: tambor vazio")
            return
        self.bico = self.tambor.pop(0)

    def remove(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        self.bico = None
    
    def write(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        grafite = self.bico 

        if grafite.tamanho <= 10:
            print("fail: tamanho insuficiente")
            return
        gasto = grafite.gastoPorFolha()

        if grafite.tamanho - gasto < 10:
            print("fail: folha incompleta")
            grafite.tamanho = 10
            return
        
        grafite.tamanho -= gasto

    def __str__(self):
        bico = f"[{self.bico}]" if self.bico is not None else "[]"
        tambor = "".join(f"[{x}]" for x in self.tambor)
        return f"calibre: {self.calibre}, bico: {bico}, tambor: <{tambor}>"
    

def main():
    lap: Lapiseira | None = None

    while True:
        line = input().strip()
        if line == "":
            continue
        print("$" + line)
        args =  line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            cal =  float(args[1])
            lap = Lapiseira(cal)
        elif args[0] == "remove":
            if lap is not None:
                lap.remove()
            else:
                print("fail: lapiseira nao iniciada")
        elif args[0] == "insert":
            if lap is None:
                print("fail: lapiseira nao iniciada")
                continue
            calibre = float(args[1])
            dureza = args[2]
            tam = int(args[3])
            g = Grafite(calibre, dureza, tam)
            lap.insert(g)
        
        elif args[0] == "show":
            if lap is not None:
                print(lap)
            else:
                print("fail: lapiseira nao iniciada")
        elif args[0] == "write":
            if lap is not None:
                lap.write()
            else:
                print("fail: lapiseira nao iniciada")
        elif args[0] == "pull":
            if lap is not None:
                lap.pull()
            else:
                print("fail: lapiseira nao iniciada")

main()