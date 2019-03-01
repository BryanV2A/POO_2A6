class EsPar:

    __num = int(0)
    __resultado = int(0)
    """
    Solo se generaron dos valores porque fueron los unicos necesarios para la operacion
    """
    def __init__(self, num):
        """
        Los parámetros del método constructor son solo
        atributos de entrada y no de salida
        """
        self.__num = num

    def determinarPar(self):
        """
        Método donde se determna si el número ingresado es par o no
        mediante el uso del operador (%) que son los residuos en este caso de 2
        """
        self.__resultado = self.__num % 2

        if(self.__resultado == 0):
            return 1

        if(self.__resultado != 0):
            return 0
        """
        Aqui se agregaron dos return que son valores de tipo booleanos 
        para evitar el uso de mensajes dentro de los métodos
        """