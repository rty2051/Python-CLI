import os
import subprocess

VSCODE_PATH = "C:/Users/Ryan/AppData/Local/Programs/Microsoft VS Code/Code.exe"
# VSCODE_PATH = "C:/Windows/System32/OpenWith.exe"

def run_command(command, args):
    if command == "mkdir":
        if len(args) == 0:
            raise Exception("    USAGE: mkdir name [path]")
        name = args[0]
        if len(args) > 1:
            path = args[1]
        else:
            path = os.getcwd()
        os.makedirs(f"{path}/{name}")
    if command == "rmdir":
        if len(args) == 0:
            raise Exception("    USAGE: rmdir name [path]")
        name = args[0]
        if len(args) > 1:
            path = args[1]
        else:
            path = os.getcwd()
        os.rmdir(f"{path}/{name}")
    if command == "open":
        if len(args) == 0:
            raise Exception("    USAGE: open path")
        print("    Opening file in VS Code...")
        subprocess.run([VSCODE_PATH, args[0]])

    if command == "man":
        print("    mkdir name [path]")
        print("    @param name: name of the folder to be made")
        print("    @param path: destination path of folder")
        print("")
        print("    rmdir name [path]")
        print("    @param name: name of the folder to be removed")
        print("    @param path: source path of folder")
        print("")
        print("    open path")
        print("    @param path: path of the file to be opened")
        print("")

def main():
    while True:
        user_in = input().split(" ")
        if user_in[0] == "end":
            return
        try:
            run_command(user_in[0], user_in[1:])
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()