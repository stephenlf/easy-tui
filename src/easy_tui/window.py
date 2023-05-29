class Window:
    logs = False
    def __init__(self, window_height: int = 27):
        self.window_height = window_height
        self.buffer = self.new_buffer()
        if self.logs: logging.debug(f"::easy_tui::Window - Initializing {self.__name__}")

    def do_logging(self):
        self.logs = True

    def __repr__(self):
        return '\n'.join(self.buffer)

    def new_buffer(self):
        if self.logs: logging.debug(f"::easy_tui::Window - Creating buffer of height {self.window_height} on {self.__name__}")
        return ["" for _ in range(self.window_height)]

    def print(self):
        if self.logs: logging.debug(f"::easy_tui::Window - print() called on {self.__name__}")
        for line in self.buffer:
            print(line)

    def wipe(self):
        if self.logs: logging.debug(f"::easy_tui::Window - wipe() called on {self.__name__}")
        for i in range(self.window_height):
            self.buffer[i] = ""
        self.print()