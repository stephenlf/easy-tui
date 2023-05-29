class Menu:
    logs = False
    def __init__(self, options: list, selection=0):
        if logs: logging.debug("::Menu.__init__()::called")
        self.options = options 
        self.selection = selection
        self.num_options = len(self.options)

    def select_down(self):
        if logs: logging.debug("::Menu.select_down()::called")
        self.selection = (self.selection + 1) % self.num_options

    def select_up(self):
        if logs: logging.debug("::Menu.select_up()::called")
        self.selection = (self.selection + (self.num_options - 1)) % self.num_options

    def do_logging(self):
        self.logs = True

class TableMenu:
    logs = False
    def __init__(self, options: list, selection=0):
        if self.logs: logging.debug("::easy_tui::TableMenu - initialized")
        self.options = options 
        self.selection: int = selection
        self.selections: set[int] = set()
        self.num_options = len(self.options)

    def select_down(self):
        if self.logs: logging.debug("::easy_tui::TableMenu - select_down() called")
        self.selection = (self.selection + 1) % self.num_options

    def select_up(self):
        if self.logs: logging.debug("::easy_tui::TableMenu - select_up() called")
        self.selection = (self.selection + (self.num_options - 1)) % self.num_options
    
    def add_selection(self, i):
        if self.logs: logging.debug(f"::easy_tui::TableMenu - selection added: {i}")
        self.selections.add(i)
    
    def rm_selection(self, i):
        if self.logs: logging.debug(f"::easy_tui::TableMenu - selection removed: {i}")
        self.selections.remove(i)