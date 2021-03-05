class Caballo:
    def __init__(self, nombre=""):
        self.__nombre = nombre

    def set_nombre(self,nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

def main():

    pony = Caballo("Ico Ico")
    print(pony.get_nombre())


if __name__ == "__main__":
    main()