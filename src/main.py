from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class BinaryConverter(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"), ("ctrl-c", "quit", "Quit the application")]

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
    
    def on_key(self, event) -> None:
        if event.key == "enter":
            # Process the user input when Enter key is pressed
            self.process_input()
        elif event.key == "backspace":
            # Handle backspace to delete characters
            self.input_text = self.input_text[:-1]
        else:
            # Append other keys to the input text
            self.input_text += event.text

    def process_input(self) -> None:
        # Process the user input (you can replace this with your logic)
        print("User input:", self.input_text)
        # Clear the input for the next user input
        self.input_text = ""
        
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
    
if __name__ == "__main__":
    app = BinaryConverter()
    app.run()