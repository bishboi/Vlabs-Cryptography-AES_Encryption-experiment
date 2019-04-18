import os
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///answer.sqlite3'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

class answers(db.Model):
    id = db.Column('ans_id', db.Integer, primary_key=True)
    a1 = db.Column(db.String(5))#, unique=True)
    a2 = db.Column(db.String(5))
    a3 = db.Column(db.String(5))
    a4 = db.Column(db.String(100))
    a5 = db.Column(db.String(100))
    a6 = db.Column(db.String(100))
    a7 = db.Column(db.String(100))
    a8 = db.Column(db.String(100))

    def __init__(self, a1, a2, a3, a4, a5, a6, a7, a8):
        self.a1 = a1;
        self.a2 = a2;
        self.a3 = a3;
        self.a4 = a4;
        self.a5 = a5;
        self.a6 = a6;
        self.a7 = a7;
        self.a8 = a8;

    # def __repr__(self):
    #     return '<Dataclass %r>' % self.data

@app.route('/')
def index():
    return render_template('introduction.html')

@app.route('/show', methods=['GET', 'POST'])
def show_all():
    return render_template('show_all.html', answers = answers.query.all())

@app.route("/quizes", methods=['GET', 'POST'])
def quizes():
    os.remove('answer.sqlite3')
    db.create_all()
    if request.method == 'POST':
        if not request.form['a1'] or not request.form['a2'] or not request.form['a3']:
        	flash('Please answer all the MCQs. They are compulsory.')
        	return redirect(url_for('show_all'))
        else:
            answer=answers(request.form['a1'], request.form['a2'], request.form['a3'], request.form['a4'], request.form['a5'], request.form['a6'], request.form['a7'], request.form['a8'])
        db.session.add(answer)
        db.session.commit()
        flash('Answers submitted')
        return redirect(url_for('show_all'))
    return render_template('quizes.html')
# def userAdd():
#     data=request.form['data']
#     db.create_all()
#     new_data=Dataclass(data)
#     db.session.add(new_data)
#     db.session.commit()
#     temp ={}
#     temp['status']=(type(new_data)==Dataclass)
#     return jsonify(temp)


@app.route('/introduction')
def introduction():
    return render_template('introduction.html')


@app.route('/theory')
def theory():
    return render_template('theory.html')


@app.route('/objective')
def objective():
    return render_template('objective.html')


@app.route('/experiment')
def experiment():
    # db.create_all()
    # allDataclasss=Dataclass.query.all()
    # strf = ''
    # for d in allDataclasss:
    #     strf += d.data
    return render_template('experiment.html',strf=strf)


# @app.route('/quizes')
# def quizes():
#     return render_template('quizes.html')


@app.route('/procedure')
def procedure():
    return render_template('procedure.html')

@app.route('/furtherReading')
def furtherReading():
    return render_template('further_reading.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
