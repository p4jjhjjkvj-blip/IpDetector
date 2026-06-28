import requests


class YandexDisk:
    """Класс для работы с REST API Яндекс.Диска."""

    BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"

    def __init__(self, token):
        self.headers = {
            "Authorization": f"{token}"
        }

    def create_folder(self, folder_name):
        """Создаёт папку на Яндекс.Диске."""

        url = self.BASE_URL
        params = {"path": folder_name}

        response = requests.put(url, headers=self.headers, params=params)

        if response.status_code in (201, 409):
            print(f"Папка '{folder_name}' готова.")
            return True

        print("Ошибка создания папки:", response.text)
        return False

    def upload_file(self, disk_path, file_path):
        """Загружает файл на Яндекс.Диск."""

        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

        params = {
            "path": disk_path,
            "overwrite": "true"
        }

        # получаем ссылку для загрузки
        response = requests.get(upload_url, headers=self.headers, params=params)

        if response.status_code != 200:
            print("Ошибка получения upload URL:", response.text)
            return False

        href = response.json().get("href")

        # загружаем файл
        with open(file_path, "rb") as f:
            upload_response = requests.put(href, files={"file": f})

        if upload_response.status_code in (201, 202):
            print("Файл успешно загружен на Яндекс.Диск")
            return True

        print("Ошибка загрузки файла:", upload_response.text)
        return False