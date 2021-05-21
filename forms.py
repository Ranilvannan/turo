from wtforms import Form, StringField, TextAreaField, DateTimeField, IntegerField


class InfoForm(Form):
    id = IntegerField(u'ID')
    create_date = DateTimeField(u'Create Date', format='%Y-%m-%d')
    write_date = DateTimeField(u'Create Date', format='%Y-%m-%d')
    sequence = StringField(u'Sequence')
    passkey = StringField(u'Passkey')
    url = StringField(u'URL')
    title = StringField(u'Title')
    description = StringField(u'Description')
    preview = TextAreaField(u'Preview')
    content = TextAreaField(u'Content')
