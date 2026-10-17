from pathlib import Path


def safe_path(filename):
    path = Path(filename.strip())

    if (
        not str(path)
        or path.is_absolute()
        or ".." in path.parts
    ):
        raise ValueError("Invalid file name")

    return path


def create_file(filename):
    path = safe_path(filename)

    with path.open("x", encoding="utf-8"):
        pass


def write_file(filename, content):
    path = safe_path(filename)

    with path.open("w", encoding="utf-8") as file:
        file.write(content)


def read_file(filename):
    path = safe_path(filename)

    with path.open("r", encoding="utf-8") as file:
        return file.read()


def append_file(filename, content):
    path = safe_path(filename)

    with path.open("a", encoding="utf-8") as file:
        file.write(content + "\n")