class Curso():
    def __init__(self, name, description, publicationDate, formation):
        self.__name = name
        self.__description = description
        self.__publicationDate = publicationDate
        self.__formation = formation

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def publicationDate(self):
        return self.__publicationDate

    @publicationDate.setter
    def publicationDate(self, publicationDate):
        self.__publicationDate = publicationDate

    @property
    def formation(self):
        return self.__formation

    @formation.setter
    def formation(self, formation):
        self.__formation = formation
