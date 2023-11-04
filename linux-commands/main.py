import argparse
import linux_commands

def main():
    parser = argparse.ArgumentParser(description="Emulate Linux commands on Windows")

    parser.add_argument("--ls", metavar="directory", help="List files and directories in a directory")
    parser.add_argument("--pwd", action="store_true", help="Print the current working directory")
    parser.add_argument("--mkdir", metavar="directory_name", help="Create a new directory")
    parser.add_argument("--rm", metavar="file_or_directory", help="Remove a file or directory")
    parser.add_argument("--cat", metavar="filename", help="Display the contents of a file")
    parser.add_argument("--cp", nargs=2, metavar=("source", "destination"), help="Copy a file or directory")
    parser.add_argument("--mv", nargs=2, metavar=("source", "destination"), help="Move a file or directory")

    args = parser.parse_args()

    if args.ls:
        directory = args.ls
        files = linux_commands.ls(directory)
        for file in files:
            print(file)
    elif args.pwd:
        current_directory = linux_commands.pwd()
        print(current_directory)
    elif args.mkdir:
        directory_name = args.mkdir
        linux_commands.mkdir(directory_name)
    elif args.rm:
        file_or_directory = args.rm
        linux_commands.rm(file_or_directory)
    elif args.cat:
        filename = args.cat
        linux_commands.cat(filename)
    elif args.cp:
        source, destination = args.cp
        linux_commands.cp(source, destination)
    elif args.mv:
        source, destination = args.mv
        linux_commands.mv(source, destination)

if __name__ == "__main__":
    main()
