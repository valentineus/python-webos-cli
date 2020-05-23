""" Репозиторий файла "package.json" """
import json

from packer.models.package_model import PackageModel


def load_file(file_path: str) -> PackageModel:
    """ Загрузка и обработка файла """
    result: PackageModel = PackageModel()

    with open(file_path) as file:
        data = json.load(file)

        result.description = str(data["description"])
        result.name = str(data["name"])
        result.version = str(data["version"])

    return result
