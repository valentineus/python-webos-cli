""" Тестирования репозитория и модели "package.json" файла """
import os
import unittest

from packer.models.package_model import PackageModel
from packer.repositories.package_repository import load_file


class TestLoadPackageJson(unittest.TestCase):

    def test_load(self):
        """ Базовая загрузка файла """

        example_file = os.path.join("example", "project", "package.json")
        result: PackageModel = load_file(example_file)

        self.assertEqual("1.0.0", result.version)
        self.assertEqual("This's description", result.description)
        self.assertEqual("some-project", result.name)


if __name__ == '__main__':
    unittest.main()
