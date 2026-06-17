import os


def move_file(command: str) -> None:
    parts = command.split()

    source_file = parts[1]
    destination = parts[2]

    dirs_and_file = destination.split("/")

    folders = dirs_and_file[:-1]

    path = ""

    for folder in folders:
        path += folder

        if not os.path.exists(path):
            os.mkdir(path)

        path += "/"

    with open(source_file, "r") as file_in, open(destination, "w") as file_out:
        text = file_in.read()
        file_out.write(text)

    os.remove(source_file)
