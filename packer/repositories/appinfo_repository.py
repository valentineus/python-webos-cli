""" Репозиторий файла "appinfo.json" """

import json

from packer.models.appinfo_model import AppInfoModel


def load_file(file_path: str) -> AppInfoModel:
    """ Загрузка и обработка файла """

    result: AppInfoModel = AppInfoModel()

    with open(file_path)as file:
        data = json.load(file)

        result.id = str(data["id"])
        result.title = str(data["title"])
        result.version = str(data["version"])

    return result
