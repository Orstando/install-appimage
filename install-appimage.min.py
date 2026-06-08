import argparse,shutil,os;p=argparse.ArgumentParser(description="Application Installer");p.add_argument("-n","--name",help="Name of application",required=True,default="");p.add_argument("-d","--description",help="Description of application",default="");p.add_argument("-i","--icon",help="Application icon",default="");p.add_argument("-t","--terminal",help="Whether to run application in a terminal or not",type=bool);p.add_argument("-c","--commandline",help="Name of binary for running on command line",default="");p.add_argument('filename');a=p.parse_args();print(f"Installing '{a.name}'...");desktop_entry="[Desktop Entry]\n"
if a.name:desktop_entry += f"Name={a.name}\n"
if a.description:desktop_entry+=f"Comment={a.description}\n"
if a.icon:os.makedirs("/opt/application-installer/icons/",exist_ok=True);shutil.copy(a.icon,f"/opt/application-installer/icons/{a.icon}");desktop_entry+=f"Icon=/opt/application-installer/icons/{a.icon}\n"
if a.terminal:desktop_entry+=f"Terminal=true"
else:desktop_entry+=f"Terminal=false"
if a.commandline:shutil.copy(a.filename,f"/bin/{a.commandline}");desktop_entry+=f"Exec={a.commandline}\n"
else:shutil.copy(a.filename,"/bin/");desktop_entry+=f"Exec={a.filename}\n"
desktop_entry+="Type=Application"
with open(f"/usr/share/applications/{a.name}.desktop","w")as f:f.write(desktop_entry)
print("Installation complete.")
