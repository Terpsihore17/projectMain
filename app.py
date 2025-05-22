from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модели
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(200))
    size = db.Column(db.Integer, nullable=False)
    date_create = db.Column(db.DateTime, default=db.func.current_timestamp())

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date_joined = db.Column(db.DateTime, default=db.func.current_timestamp())

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    status = db.Column(db.String(20), default='Новая')
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

# Создание всех таблиц
with app.app_context():
    db.create_all()  # Создает таблицы на основе моделей

# Основные маршруты
@app.route('/')
def index():
    return render_template('index.html')  # Отображение главной страницы

@app.route('/files')
def files():
    return render_template('files.html')  # Страница управления файлами

@app.route('/users')
def users():
    return render_template('users.html')  # Страница управления пользователями

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')  # Страница управления задачами

# API маршруты
@app.route('/api/files', methods=['GET'])
def get_files():
    files = File.query.all()
    return jsonify([{
        'id': f.id,
        'name': f.name,
        'comment': f.comment,
        'date_create': f.date_create,
        'size': f.size
    } for f in files])

@app.route('/api/files', methods=['POST'])
def add_file():
    data = request.json
    new_file = File(name=data['name'], comment=data['comment'], size=data['size'])
    db.session.add(new_file)
    db.session.commit()
    return jsonify({'message': 'Файл добавлен'}), 201

@app.route('/api/files/<int:id>', methods=['DELETE'])
def delete_file(id):
    file = File.query.get(id)
    if file:
        db.session.delete(file)
        db.session.commit()
        return jsonify({'message': 'Файл удален'})
    return jsonify({'message': 'Файл не найден'}), 404

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': u.id,
        'username': u.username,
        'email': u.email,
        'date_joined': u.date_joined
    } for u in users])

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{
        'id': t.id,
        'title': t.title,
        'description': t.description,
        'status': t.status,
        'date_created': t.date_created
    } for t in tasks])

if __name__ == '__main__':
    app.run(debug=True)


