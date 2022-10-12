from wtforms import Field
from wtforms.widgets import TextArea

class JsonField(Field):
    widget = TextArea()

    def _value(self):
        return self.data if self.data else {}

    def process_formdata(self, valuelist):
        output = {}
        if valuelist:
            # list_ = valuelist.split(',')
            for x in valuelist:
                print(x)
                maps = x.split(":")
                output[str(maps[0])] = output[str(maps[1])]

            self.data = output
        else:
            self.data = {}