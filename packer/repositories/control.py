""" Репозиторий файла "control" """

from string import Template

from packer.models.control import ControlModel


def create_file(options: ControlModel, file_path: str, template_path: str) -> None:
    """ Создать файл по шаблону """

    dictionary = {
        "description": options.description,
        "size": options.size,
        "title": options.title,
        "version": options.version,
    }

    with open(template_path) as file:
        template: Template = Template(file.read())

    with open(file_path, "tw") as file:
        file.write(template.substitute(dictionary))
