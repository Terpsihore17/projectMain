from flask import request, jsonify, render_template
from app import app, db
from models import File, User, Task

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Маршруты для управления файлами
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

# Маршруты для управления пользователями
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': u.id,
        'username': u.username,
        'email': u.email,
        'date_joined': u.date_joined
    } for u in users])

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Пользователь добавлен'}), 201

@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'Пользователь удален'})
    return jsonify({'message': 'Пользователь не найден'}), 404

# Маршруты для управления задачами
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

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    new_task = Task(title=data['title'], description=data['description'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Задача добавлена'}), 201

@app.route('/api/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Задача удалена'})
    return jsonify({'message': 'Задача не найдена'}), 404

# Маршруты для страниц управления
@app.route('/files')
def files():
    return render_template('files.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')
