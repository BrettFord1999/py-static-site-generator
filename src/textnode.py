from enum import Enum, auto

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, comparison):
        return (
            self.text_type == comparison.text_type
            and self.text == comparison.text
            and self.url == comparison.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type},{self.url})"