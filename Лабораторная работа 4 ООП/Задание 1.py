if __name__ == "__main__":
    class Device:
        def __init__(self, brand: str, model: str):
            """
            Конструктор базового класса устройства.

            :param brand: Бренд устройства
            :param model: Модель устройства
            """
            self._brand = brand
            self._model = model
            self._power_on = False  # Приватный атрибут, который указывает, включено ли устройство

        def turn_on(self) -> None:
            """
            Метод для включения устройства

            :return: None
            """
            self._power_on = True

        def turn_off(self) -> None:
            """
            Метод для выключения устройства

            :return: None
            """
            self._power_on = False

        def is_powered_on(self) -> bool:
            """
            Метод, который возвращает текущее состояние питания устройства

            :return: True, если устройство включено, False в противном случае
            """
            return self._power_on

        def perform_task(self, task: str) -> str:
            """
            Метод для выполнения общей задачи на устройстве

            :param task: Строка с описанием задачи
            :return: Строка с информацией о выполненной задаче на устройстве
            """
            return f"Задача '{task}' выполнена на устройстве {self._brand} {self._model}"

        def __str__(self) -> str:
            """
            Метод для представления объекта в виде строки

            :return: Строка с информацией о бренде, модели и состоянии питания устройства
            """
            power_status = "включено" if self._power_on else "выключено"
            return f"{self._brand} {self._model}, состояние: {power_status}"

        def __repr__(self) -> str:
            """
            Метод для представления объекта в виде строки

            :return: Строка, которая может быть использована для создания нового объекта
            """
            return f"{self.__class__.__name__}(brand={self._brand!r}, model={self._model!r})"


    class Smartphone(Device):
        def __init__(self, brand: str, model: str, os: str):
            """
            Конструктор дочернего класса смартфона

            :param brand: Бренд смартфона
            :param model: Модель смартфона
            :param os: Операционная система смартфона
            """
            super().__init__(brand, model)
            self._os = os

        def make_call(self, number: str) -> str:
            """
            Метод для осуществления звонка со смартфона

            :param number: Номер, на который осуществляется звонок
            :return: Строка с информацией о звонке
            """
            if self.is_powered_on():
                return f"Звонок на номер {number} с {self._brand} {self._model}"
            else:
                return "Смартфон выключен, невозможно совершить звонок"

        def make_video_call(self, number: str) -> str:
            """
            Перегрузка метода для осуществления видеозвонка со смартфона

            :param number: Номер, на который осуществляется видеозвонок
            :return: Строка с информацией о видеозвонке
            """
            if self.is_powered_on():
                return f"Видеозвонок на номер {number} с {self._brand} {self._model}"
            else:
                return "Смартфон выключен, невозможно совершить видеозвонок"

        def perform_task(self, task: str) -> str:
            """
            Перегрузка метода для выполнения задачи на смартфоне

            :param task: Строка с описанием задачи
            :return: Строка с информацией о выполненной задаче на смартфоне

            Причина перегрузки: Добавление информации об операционной системе (ОС),
            так как выполнение задачи на смартфоне может зависеть от используемой операционной системы
            """
            return f"{super().perform_task(task)}, ОС: {self._os}"

        def __str__(self) -> str:
            """
            Перегрузка метода __str__ для представления смартфона в виде строки

            :return: Строка с информацией о бренде, модели, состоянии питания и операционной системе смартфона
            """
            power_status = "включен" if self.is_powered_on() else "выключен"
            return f"{super().__str__()}, ОС: {self._os}, состояние: {power_status}"

        def __repr__(self) -> str:
            """
            Перегрузка метода __repr__ для представления смартфона в виде строки

            :return: Строка, которая может быть использована для создания нового объекта
            """
            return f"{self.__class__.__name__}(brand={self._brand!r}, model={self._model!r}, os={self._os!r})"


    class Laptop(Device):
        def __init__(self, brand: str, model: str, screen_size: float, processor: str):
            """
            Конструктор дочернего класса ноутбука

            :param brand: Бренд ноутбука
            :param model: Модель ноутбука
            :param screen_size: Размер экрана ноутбука в дюймах
            :param processor: Процессор ноутбука
            """
            super().__init__(brand, model)
            self._screen_size = screen_size
            self._processor = processor
            self._lid_closed = True  # Приватный атрибут, указывающий, закрыта ли крышка ноутбука

        def open_lid(self) -> None:
            """
            Метод для открытия крышки ноутбука

            :return: None
            """
            self._lid_closed = False

        def close_lid(self) -> None:
            """
            Метод для закрытия крышки ноутбука

            :return: None
            """
            self._lid_closed = True

        def is_lid_closed(self) -> bool:
            """
            Метод, который возвращает текущее состояние крышки ноутбука

            :return: True, если крышка закрыта, False в противном случае
            """
            return self._lid_closed

        def perform_task(self, task: str) -> str:
            """
            Перегрузка метода для выполнения задачи на ноутбуке

            :param task: Строка с описанием задачи
            :return: Строка с информацией о выполненной задаче на ноутбуке

            Причина перегрузки: Добавление информации о состоянии крышки (открыта/закрыта),
            так как выполнение задачи на ноутбуке может зависеть от состояния крышки
            """
            lid_status = "закрыта" if self.is_lid_closed() else "открыта"
            return f"{super().perform_task(task)}, Экран: {self._screen_size}\", " \
                   f"Процессор: {self._processor}, крышка: {lid_status}"

        def __str__(self) -> str:
            """
            Перегрузка метода __str__ для представления ноутбука в виде строки

            :return: Строка с информацией о бренде, модели, состоянии питания и характеристиках ноутбука
            """
            power_status = "включен" if self.is_powered_on() else "выключен"
            lid_status = "закрыта" if self.is_lid_closed() else "открыта"
            return f"{super().__str__()}, Экран: {self._screen_size}\", "\
                f"Процессор: {self._processor}, состояние: {power_status}, крышка: {lid_status}"

        def __repr__(self) -> str:
            """
            Перегрузка метода __repr__ для представления ноутбука в виде строки

            :return: Строка, которая может быть использована для создания нового объекта
            """
            return f"{self.__class__.__name__}(brand={self._brand!r}, model={self._model!r}, " \
                   f"screen_size={self._screen_size!r}, processor={self._processor!r})"


    pass
