import json

from ip_service import IpService
from yandex_disk import YandexDisk

YANDEX_TOKEN = "y0__wgBEKqX35ABGNuWAyDI75eLGIV7igiohBSPKYwGAZe0ubsnxkCp"


def main():
    """Основная функция программы."""

    ip = IpService.get_ip()
    print(f"Ваш IP: {ip}")

    location = IpService.get_location(ip)
    print("\nИнформация по IP:")
    print(location)

    file_name = "ip_info.json"

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(location, file, indent=4, ensure_ascii=False)

    print(f"Информация сохранена в файл {file_name}")

    yandex_disk = YandexDisk(YANDEX_TOKEN)

    folder_name = "ip_detector"
    yandex_disk.create_folder(folder_name)

    disk_path = f"{folder_name}/{file_name}"
    yandex_disk.upload_file(disk_path, file_name)


if __name__ == "__main__":
    main()