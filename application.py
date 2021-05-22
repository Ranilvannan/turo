from flask import Flask, request, flash, redirect, url_for, render_template
from forms import InfoForm
from models import db, Information
from datetime import datetime


app = Flask(__name__)
app.config.from_object('config.ProductionConfig')
app.config['SECRET_KEY'] = 'you-will-never-guess'
db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/home_page')
def home_page():
    return 'Hello, World!'


@app.route('/info_list')
def info_list():
    info = Information.query.all()
    return render_template('info_list.html', info=info)


@app.route('/info/create', methods=['GET', 'POST'])
def info_create():
    form = InfoForm(request.form)
    if request.method == 'POST' and form.validate():
        passkey = form.passkey.data

        if passkey == "123":
            info = Information(
                create_date=datetime.now(),
                write_date=datetime.now(),
                sequence=form.sequence.data,
                passkey=form.passkey.data,
                url=form.url.data,
                title=form.title.data,
                preview=form.preview.data,
                content=form.content.data)
            db.session.add(info)
            db.session.commit()
            return redirect(url_for('info_list'))
        else:
            message = 'Invalid credentials'
        return render_template('info_create.html', form=form, message=message)
    return render_template('info_create.html', form=form)


@app.route('/info/edit/<record_id>', methods=['GET', 'POST'])
def info_edit(record_id):
    form = InfoForm(request.form)
    if record_id:
        info = Information.query.get(record_id)

    if request.method == 'POST' and form.validate():
        passkey = form.passkey.data

        if passkey == "123":
            info.write_date = datetime.now()
            info.sequence = form.sequence.data
            info.passkey = form.passkey.data
            info.url = form.url.data
            info.title = form.title.data
            info.preview = form.preview.data
            info.content = form.content.data

            db.session.commit()
            return redirect(url_for('info_list'))
        else:
            message = 'Invalid credentials'
        return render_template('info_create.html', form=form, message=message)
    return render_template('info_edit.html', form=form, info=info)
