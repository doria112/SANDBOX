class TextEditor:

    def __init__(self):
        self.text = ""
        self.length = 0
        self.cursor_pos = 0

    def addText(self, text: str) -> None:
        self.text = self.text[:self.cursor_pos] + text + self.text[self.cursor_pos:]
        self.cursor_pos += len(text)
        self.length += len(text)
        return

    def deleteText(self, k: int) -> int:
        nd = min(self.cursor_pos, k)
        self.text = self.text[:self.cursor_pos-nd] + self.text[self.cursor_pos:]
        self.cursor_pos -= nd
        self.length -= nd
        return nd #number deleted
        
    def cursorLeft(self, k: int) -> str:
        ml = min(self.cursor_pos, k) #min left
        self.cursor_pos -= ml
        return self.text[self.cursor_pos - min(self.cursor_pos, 10): self.cursor_pos]
        

    def cursorRight(self, k: int) -> str:
        mr = min(k, self.length - self.cursor_pos)
        self.cursor_pos += mr
        return self.text[self.cursor_pos - min(self.cursor_pos, 10): self.cursor_pos]
