""" Репозиторий файла "control" """

from pathlib import Path
from string import Template
from typing import Dict, Union

from packer.models.control import ControlModel


def create_file(options: ControlModel, file_path: str, template_path: str) -> None:
    """ Создать файл по шаблону """

    dictionary: Dict[str, Union[str, int]] = {
        "description": options.description,
        "size": options.size,
        "title": options.title,
        "version": options.version,
    }

    with open(template_path) as file:
        template: Template = Template(file.read())

    with open(file_path, "tw") as file:
        file.write(template.substitute(dictionary))


def get_size(directory_path: str) -> int:
    """ Получить размер директории """

    directory: Path = Path(directory_path)
    result: int = 0

    for file in directory.glob("**/*"):
        if file.is_file():
            result += file.stat().st_size

    return result
