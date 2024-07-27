from enum import Enum


class ServiceErrors(Enum):
    cs_money: str = "Не удалось найти предметы на площадке CS-Money"
    cs_market: str = "Не удалось найти предметы на площадке CS-Market"