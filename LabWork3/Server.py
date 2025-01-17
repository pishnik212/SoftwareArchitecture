from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

# Реализация классов согласно структуре БД
# Пользователь системы (Администратор / сотрудник приемной комиссии)
class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    roleId = db.Column(db.Integer, db.ForeignKey('role.roleId'))

# Роль сотрудника - пользователя в системе
class Role(db.Model):
    roleId = db.Column(db.Integer, primary_key=True)
    roleName = db.Column(db.String(80), nullable=False)

# Запросы, отправляемые пользователями.
class Request(db.Model):
    requestId = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)

# Абитуриент
class Entrant(db.Model):
    entrantId = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(100), nullable=False)
    dateOfBirth = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

# Заявка абитуриента на направление
class Application(db.Model):
    applicationId = db.Column(db.Integer, primary_key=True)
    submissionDate = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    entrantId = db.Column(db.Integer, db.ForeignKey('entrant.entrantId'))

# Просмотр всех пользователей пользователей системы
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'userId': user.userId, 'username': user.username} for user in users])

# Просмотр всех поданных заявок
@app.route('/applications', methods=['POST'])
def add_application():
    data = request.get_json()
    new_application = Application(
        submissionDate=data['submissionDate'],
        status=data['status'],
        entrantId=data['entrantId']
    )
    db.session.add(new_application)
    db.session.commit()
    return jsonify({'applicationId': new_application.applicationId}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
