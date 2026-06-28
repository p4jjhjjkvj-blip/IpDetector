import requests


class IpService:
    """Сервис для получения IP-адреса и информации о нём."""

    IPIFY_URL = "https://api.ipify.org?format=json"
    IPINFO_URL = "https://ipinfo.io/{ip}/geo"

    @staticmethod
    def get_ip():
        """
        Получает текущий IP пользователя через ipify API.

        Returns:
            str: IP-адрес пользователя
        """

        response = requests.get(IpService.IPIFY_URL, timeout=10)
        response.raise_for_status()

        return response.json()["ip"]

    @staticmethod
    def get_location(ip):
        """
        Получает географическую информацию по IP-адресу.

        Args:
            ip (str): IP-адрес пользователя

        Returns:
            dict: информация о геолокации
        """

        url = IpService.IPINFO_URL.format(ip=ip)

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return response.json()