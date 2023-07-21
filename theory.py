class ContextManager:
    def __init__(self):
        print("init method called")

    def __enter__(self):
        print("enter method called")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("exit method called")


class CustomFileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
        return True


from contextlib import contextmanager


@contextmanager
def open_file(name, mode):
    f = open(name, mode)
    try:
        yield f
    finally:
        f.close()


if __name__ == '__main__':

    with open_file("greetings.txt", "r") as file:
        print(file.read())
        print(file.closed)

    print(file.closed)
