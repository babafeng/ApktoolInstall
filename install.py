import os
import shutil
import platform

VERSION = "v1.0"


def install_apktool():
    system = platform.system()
    print("I: Apktool Install %s." % VERSION)
    print("I: System: %s." % system)

    if system == "Linux":
        try:
            shutil.copyfile(os.path.abspath("apktool_2.2.0.jar"), "/usr/bin/apktool.jar")
            print("I: Copy [apktool_2.2.0.jar] to [/usr/bin/] successed.")
        except Exception as err:
            print("E: %s." % err)
            print("E: Failed.")
            return

        try:
            shutil.copyfile(os.path.abspath("apktool"), "/usr/bin/apktool")
            print("I: Copy [apktool] to [/usr/bin/] successed.")
        except Exception as err:
            print("E: %s." % err)
            print("E: Failed.")
            return

        p = os.popen("sudo chmod 755 /usr/bin/apktool.jar")
        p = os.popen("sudo chmod 755 /usr/bin/apktool")
        p.read()

        print("I: Done.")

    elif system == "Windows":
        try:
            shutil.copyfile(os.path.abspath("apktool_2.2.0.jar"), "C:\\Windows\\System32\\apktool.jar")
            print("I: Copy [apktool_2.2.0.jar] to [C:\\Windows\\System32] successed.")
        except Exception as err:
            print("E: %s." % err)
            print("E: Failed.")
            return

        apktool_cmd_text = """@echo off\nset PATH=%CD%;%PATH%;\njava -jar "%~dp0\\apktool.jar" %1 %2 %3 %4 %5 %6 %7 %8 %9"""
        try:
            with open("C:\\Windows\\System32\\apktool.cmd", "w") as apktool_cmd_file:
                apktool_cmd_file.write(apktool_cmd_text)
                apktool_cmd_file.close()
        except Exception as err:
            print("E: %s." % err)

        finally:
            if os.path.exists("C:\\Windows\\System32\\apktool.cmd"):
                print("I: Create [apktool.cmd] successed.")
            else:
                print("E: Create [apktool.cmd] failed.")
                print("E: Failed.")
                return

        print("I: Done.")


if __name__ == '__main__':
    install_apktool()
