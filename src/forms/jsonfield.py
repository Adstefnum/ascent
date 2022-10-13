from wtforms import Field
from wtforms.widgets import TextArea
import ujson

class JsonField(Field):
    widget = TextArea()

    def _value(self):
        return self.data if self.data else {}

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = ujson.loads(valuelist[0])

        else:
            self.data = {}