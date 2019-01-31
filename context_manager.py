from contextlib import ContextDecorator

class makeparagraph(ContextDecorator):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('<p>')
        return self

    def __exit__(self, *exc):
        print('</p>')
        return False

@makeparagraph('lalala')
def emit_html():
    print('Here is some non-HTML')

# emit_html()

with makeparagraph('lala') as maker:
    print(maker.name)
    evolut = "eveee"

print(evolut)
print(maker.name)
