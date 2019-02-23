class EsPar:

    __num = int(0)
    __resultado = int(0)
    __r = ""

    def __init__(self, num):
        self.__num = num

    def determinarPar(self):
        self.__resultado = self.__num % 2

        if(self.__resultado == 0):
            return 1

        if(self.__resultado != 0):
            return 0