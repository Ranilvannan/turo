from wtforms import Form, StringField, TextAreaField, IntegerField


class InfoForm(Form):
    id = IntegerField(u'ID')
    sequence = StringField(u'Sequence')
    passkey = StringField(u'Passkey')
    url = StringField(u'URL')
    title = StringField(u'Title')
    description = StringField(u'Description')
    preview = TextAreaField(u'Preview')
    content = TextAreaField(u'Content')
