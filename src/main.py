from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class BinaryConverter(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"), ("ctrl-c", "quit", "Quit the application")]

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
    
if __name__ == "__main__":
    app = BinaryConverter()
    app.run()