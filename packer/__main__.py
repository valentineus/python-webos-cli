import os
import shutil
import tempfile

from packer.models.appinfo import AppInfoModel
from packer.models.control import ControlModel
from packer.models.package import PackageModel
from packer.repositories.appinfo import load_file as load_appinfo_file
from packer.repositories.control import create_file as create_control_file, get_size
from packer.repositories.package import load_file as load_package_file

project_path: str = os.path.join("tests", "example", "project")

package_file_path: str = os.path.join(project_path, "package.json")
package_file: PackageModel = load_package_file(package_file_path)
print("Package", package_file)

appinfo_file_path: str = os.path.join(project_path, "appinfo.json")
appinfo_file: AppInfoModel = load_appinfo_file(appinfo_file_path)
print("AppInfo:", appinfo_file)

temp_directory = tempfile.mkdtemp()
print("Temp Directory:", temp_directory)

control_options: ControlModel = ControlModel()
control_options.description = package_file.description
control_options.size = get_size(project_path)
control_options.title = appinfo_file.title
control_options.version = appinfo_file.version
print("Control Options:", control_options)

control_template_file = os.path.join("templates", "control.template")
control_output_file = os.path.join(temp_directory, "control")
create_control_file(control_options, control_output_file, control_template_file)

shutil.rmtree(temp_directory)
