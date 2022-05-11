from asyncio.windows_events import NULL


class NoException(Exception):
    pass

class PosicaoNaoVazia(NoException):
    pass

class No:

    def __init__(self, valor):
        self.valor = valor
        self.filho_esquerda = None
        self.filho_direita = None

    def __str__(self):
        return f'No(valor={self.valor})'

    def add_esquerda(self, valor):
        if self.tem_filho_esquerda():
            raise PosicaoNaoVazia()

        self.filho_esquerda = No(valor)       

    def add_direita(self, valor):
        if self.tem_filho_direita():
            raise PosicaoNaoVazia()
        
        self.filho_direita = No(valor)
            
    def tem_filho_esquerda(self):
        return self.filho_esquerda is not None

    def tem_filho_direita(self):
        return self.filho_direita is not None

    def eh_folha(self) -> bool:
        return (not self.tem_filho_direita()) and (not self.tem_filho_esquerda())


class Arvore:

    def __init__(self):
        self.raiz : No = None

    def esta_vazia(self):
        return self.raiz is None

    def obter_raiz(self):
        return self.raiz

    def add(self, valor):
        if self.esta_vazia():
            self.raiz = No(valor)
        else:
            self.add_(self.raiz, valor)
    
    def add_(self, no, valor):
        if valor > no.valor:
            if no.filho_direita:
                self.add_(no.filho_direita, valor)
            else:
                no.filho_direita = No(valor)
        else:
            if no.filho_esquerda:
                self.add_(no.filho_esquerda, valor)
            else:
                no.filho_esquerda = No(valor)

    def percorrer(self):
        self.percorrer_pos_ordem(self.raiz)
        print()

    def percorrer_pre_ordem(self, no: No):
        if no is None:
            return 

        print(no.valor, end=' ')
        self.percorrer_pre_ordem(no.filho_esquerda)
        self.percorrer_pre_ordem(no.filho_direita)

    def percorrer_em_ordem(self, no : No):
        if no is None:
            return
        
        self.percorrer_em_ordem(no.filho_esquerda)
        print(no.valor, end=' ')
        self.percorrer_em_ordem(no.filho_direita)

    def percorrer_pos_ordem(self, no: No):
        if no is None:
            return

        self.percorrer_pos_ordem(no.filho_esquerda)
        self.percorrer_pos_ordem(no.filho_direita)
        print(no.valor, end=' ')
  

    def altura (self) -> int:
        return self._altura(self.raiz)

    def _altura(self, no: No) -> int:
        if no is None or no.eh_folha():
            return 0

        alt_esquerda = self._altura(no.filho_esquerda)
        alt_direita = self._altura(no.filho_direita)

        if alt_esquerda > alt_direita:
            return 1 + alt_esquerda
        else:
            return 1 + alt_direita

    def quant(self) -> int:
        return self._quant(self.raiz)

    def _quant (self, no : No):
        if no is None:
            return 0
        else:
            return 1 + self._quant(no.filho_esquerda) + self._quant(no.filho_direita)

    def folhas(self) -> int:
        return self._folhas(self.raiz)
    def _folhas(self, no: No) -> int:
        if no is None:
            return 0
        if no.eh_folha():
            return 1
        return self._folhas(no.filho_direita) + self._folhas(no.filho_esquerda)