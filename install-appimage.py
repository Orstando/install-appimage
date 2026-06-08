import argparse
import shutil
import os

parser = argparse.ArgumentParser(description = "Application Installer")
parser.add_argument("-n", "--name", help = "Name of application", required = True, default = "")
parser.add_argument("-d", "--description", help = "Description of application", default = "")
parser.add_argument("-i", "--icon", help = "Application icon", default = "")
parser.add_argument("-t", "--terminal", help = "Whether to run application in a terminal or not", type=bool)
parser.add_argument("-c", "--commandline", help = "Name of binary for running on command line", default = "")
parser.add_argument('filename')

argument = parser.parse_args()

print(f"Installing '{argument.name}'...")

desktop_entry = "[Desktop Entry]\n"

if argument.name:
    desktop_entry += f"Name={argument.name}\n"

if argument.description:
    desktop_entry += f"Comment={argument.description}\n"

if argument.icon:
    os.makedirs("/opt/application-installer/icons/", exist_ok=True)
    shutil.copy(argument.icon, f"/opt/application-installer/icons/{argument.icon}")
    desktop_entry += f"Icon=/opt/application-installer/icons/{argument.icon}\n"
if argument.terminal:
    desktop_entry += f"Terminal=true"
else:
    desktop_entry += f"Terminal=false"

if argument.commandline:
    shutil.copy(argument.filename, f"/bin/{argument.commandline}")
    desktop_entry += f"Exec={argument.commandline}\n"
else:
    shutil.copy(argument.filename, "/bin/")
    desktop_entry += f"Exec={argument.filename}\n"

desktop_entry += "Type=Application"

with open(f"/usr/share/applications/{argument.name}.desktop", "w") as f:
    f.write(desktop_entry)

print("Installation complete.")
