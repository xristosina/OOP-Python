from typing import Union
import doctest

class Table:
    """
    Абстрактный класс, описывающий физический объект - стол.

    Attributes:
        material (str): Материал, из которого сделан стол.
        weight (float): Вес стола в килограммах.

    Methods:
        move(self, destination: str) -> None:
            Переместить стол в указанное место.

        damage(self, severity: Union[str, int]) -> bool:
            Нанести повреждение столу.

        inspect(self) -> str:
            Получить информацию о материале и весе стола.

    Примеры:
    >>> obj = Table("wood", 10.5)
    >>> obj.move("room")
    >>> obj.inspect()
    """

    def __init__(self, material: str, weight: float):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал, из которого сделан стол.
        :param weight: Вес стола в килограммах.

        Примеры:
        >>> obj = Table("wood", 10.5)  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал стола должен быть типа str")
        self.material = material

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес стола должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес стола должен быть положительным числом")
        self.weight = weight

    def move(self, destination: str) -> None:
        """
        Перемещает объект в указанное место.

        :param destination (str): Место, куда нужно переместить объект.

            Примеры:
        >>> obj = Table("wood", 10.5)
        >>> obj.move("room")
        """
        if not isinstance(destination, str):
            raise TypeError("Место должно быть типа str")
        ...

    def damage(self, severity: Union[str, int]) -> bool:
        """
        Наносит повреждение объекту.

        :param severity (Union[str, int]): Серьезность повреждения.

        :return: Нанесено ли повреждение

        Примеры:
        >>> obj = Table("wood", 10.5)
        >>> obj.damage("hard")
        """
        if not isinstance(severity, (str, int)):
            raise TypeError("Серьезность повреждения должна быть типа str или int")
        ...

    def inspect(self) -> str:
        """
        Получает информацию о материале и весе объекта.

        :return: Информация о материале и весе объекта.

        Примеры:
        >>> obj = Table("wood", 10.5)
        >>> obj.inspect()
        """
        ...


class SocialMediaPlatform:
    """
    Абстрактный класс, описывающий социальную сеть.

    Attributes:
        name (str): Название платформы.
        users (int): Количество пользователей платформы.

    Methods:
        post(self, content: str) -> None:
            Опубликовать контент на платформе.

        get_users_count(self) -> int:
            Получить текущее количество пользователей.

    Примеры:
    >>> platform = SocialMediaPlatform("Facebook", 1000000000)
    >>> platform.post("Hello, world!")
    >>> platform.get_users_count()
    """

    def __init__(self, name: str, users: int):
        """
        :param name: Название платформы.
        :param users: Количество пользователей платформы.
        Примеры:
        >>> platform = SocialMediaPlatform("Facebook", 1000000000)
        """

        if not isinstance(name, str):
            raise TypeError("Имя платформы должно быть типа str")
        self.name = name
        if not isinstance(users, (int, float)):
            raise TypeError("Количество пользователей должно быть int или float")
        if users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным числом")
        self.users = users

    def post(self, content: str) -> None:
        """
        Публикует контент на платформе.

        :param content (str): Контент для публикации.

        Примеры:
        >>> platform = SocialMediaPlatform("Facebook", 1000000000)
        >>> platform.post("Hello, world!")
        """
        if not isinstance(content, str):
            raise TypeError("Текст для контента должен быть типа str")
        ...

    def get_users_count(self) -> int:
        """
        Получает текущее количество пользователей.

        :return: Количество пользователей.
        Примеры:
        >>> platform = SocialMediaPlatform("Facebook", 1000000000)
        >>> platform.get_users_count()
        """
        ...


class AbstractConcept:
    """
    Абстрактный класс, описывающий абстрактное понятие.

    Attributes:
        name (str): Название понятия.
        description (str): Описание понятия.

    Methods:
        define(self) -> str:
            Предоставить определение понятия.

        explore(self) -> None:
            Исследовать понятие.

        discuss(self, topic: str) -> str:
            Обсудить понятие в контексте заданной темы.

    Примеры:
    >>> concept = AbstractConcept("Justice", "The moral principle of fairness.")
    >>> concept.define()
    >>> concept.discuss("Legal System")
    """

    def __init__(self, name: str, description: str):
        """
        :param name: Термин понятия
        :param description: Определение понятия

        Примеры:
        >>> concept = AbstractConcept("Justice", "The moral principle of fairness.")
        """
        if not isinstance(name, str):
            raise TypeError("Термин должен быть типа str")
        self.name = name
        if not isinstance(description, str):
            raise TypeError("Определние понятия должно быть типа str")
        self.description = description

    def define(self) -> str:
        """
        Функция возвращает определение понятия.

        :return: Определение понятия.
        Примеры:
        >>> concept = AbstractConcept("Justice", "The moral principle of fairness.")
        >>> concept.define()
        """
        ...

    def explore(self) -> None:
        """
        Исследует понятие.
        """
        ...

    def discuss(self, topic: str) -> str:
        """
        Метод для обсуждения понятия в контексте заданной темы.

        :param topic: Тема для обсуждения.

        :return: Результат обсуждения.
        Примеры:
        >>> concept = AbstractConcept("Justice", "The moral principle of fairness.")
        >>> concept.discuss("Legal System")
        """
        if not isinstance(topic, str):
            raise TypeError("Тема для обсуждения должна быть типа str")
        ...


if __name__ == "__main__":
    doctest.testmod()
