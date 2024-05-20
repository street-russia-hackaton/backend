from enum import IntEnum


class FieldLength(IntEnum):
    """Длины полей в приложенях"""

    # Максимальная длина полей title
    MAX_LENGTH_TITLE = 150


class UserFieldsLength(IntEnum):
    """Длины полей в приложении юзеров"""

    # Атрибуты приложения Юзеров
    # Максимальная длина поля username
    MAX_LENGTH_USERNAME = 150
    # Максимальная длина поля email
    MAX_LENGTH_EMAIL = 150
    # Максимальная длина поля phone
    MAX_LENGTH_PHONE = 15
    # Максимальная длина поля first_name
    MAX_LENGTH_FIRST_NAME = 150
    # Максимальная длина поля last_name
    MAX_LENGTH_LAST_NAME = 150
    # Максимальная длина поля middle_name
    MAX_LENGTH_MIDDLE_NAME = 150
    # Максимальная длина поля password
    MAX_LENGTH_PASSWORD = 150
    # Максимальная длина поля position
    MAX_LENGTH_POSITION = 150
    # Максимальная длина поля account_status
    MAX_LENGTH_STATUS = 20
    # Масимальная длина поля series
    MAX_LENGTH_SERIES = 4
    # Масимальная длина поля number
    MAX_LENGTH_NUMBER = 6
    # Масимальная длина поля issued_by
    MAX_LENGTH_ISSUED = 150
