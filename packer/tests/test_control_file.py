""" Тестирование репозитория и модели "control" файла """

import os
import unittest

from packer.models.control import ControlModel
from packer.repositories.control import create_file


class TestControlFile(unittest.TestCase):
    """ Тестирование репозитория и модели "control" файла """

    def test_create_file(self):
        """ Базовое создание файла по шаблону """

        model = ControlModel()

        model.description = "This's a description"
        model.size = 123456789
        model.title = "some.project"
        model.version = "1.0.0"

        template_file: str = os.path.join("..", "templates", "control.template")
        file_path: str = os.path.join("tmp", "control")

        create_file(model, file_path, template_file)


if __name__ == '__main__':
    unittest.main()
