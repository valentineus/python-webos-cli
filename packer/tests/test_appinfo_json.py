""" Тестирование репозитория и модели "appinfo.json" файла """

import os
import unittest

from packer.models.appinfo import AppInfoModel
from packer.repositories.appinfo import load_file


class TestAppInfoJson(unittest.TestCase):

    def test_load(self):
        """ Базовая загрузка файла """

        example_file = os.path.join("example", "project", "appinfo.json")
        result: AppInfoModel = load_file(example_file)

        self.assertEqual("1.0.0", result.version)
        self.assertEqual("Project", result.title)
        self.assertEqual("some.project", result.id)


if __name__ == '__main__':
    unittest.main()
