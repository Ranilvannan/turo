from flask import Flask, request, flash, redirect, url_for, render_template
from forms import InfoForm
from models import db, Information


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


@app.route('/info_update', methods=['GET', 'POST'])
def info_update():
    form = InfoForm(request.form)
    print(dir(form))
    print(form.data)
    if request.method == 'POST' and form.validate():
        passkey = form.passkey.data

        if passkey == "123":
            info = Information(
                create_date=form.create_date.data,
                write_date=form.write_date.data,
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
            print("Fail")
            message = 'Invalid credentials'
        return render_template('info_update.html', form=form, message=message)
    return render_template('info_update.html', form=form)

