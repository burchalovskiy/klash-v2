class ClientFault(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class ConnectionFault(Exception):
    def __init__(self, message, code=None):
        super().__init__(code, message)
        self.message = message
        self.code = code


class BusinessLogicFault(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class ExceptionMessages:
    AUTH = 'Ошибка авторизации: {exc}'
    NOT_FOUND = 'Отсутствуют запрашиваемые данные'
