function openUploadModal() {
    $('#uploadModal').modal('show');
}

function uploadFile() {
    const fileName = $('#fileName').val();
    const fileComment = $('#fileComment').val();
    const fileSize = $('#fileSize').val();

    $.ajax({
        url: '/api/files',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ name: fileName, comment: fileComment, size: fileSize }),
        success: function(response) {
            alert('Файл успешно загружен!');
            $('#uploadModal').modal('hide');
            loadFiles();
        },
        error: function(error) {
            alert('Ошибка при загрузке файла');
        }
    });
}

function loadFiles() {
    $.getJSON('/api/files', function(data) {
        $('#fileTable').empty();
        data.forEach(function(file) {
            $('#fileTable').append(`
                <tr>
                    <td>${file.name}</td>
                    <td>${file.comment}</td>
                    <td>${file.date_create}</td>
                    <td>${file.size}</td>
                    <td><button class="btn btn-danger" onclick="deleteFile(${file.id})">Удалить</button></td>
                </tr>
            `);
        });
    });
}

function deleteFile(id) {
    $.ajax({
        url: `/api/files/${id}`,
        type: 'DELETE',
        success: function() {
            alert('Файл удален');
            loadFiles();
        },
        error: function() {
            alert('Ошибка при удалении файла');
        }
    });
}

$(document).ready(function() {
    loadFiles();
});

// Код для управления пользователями
function openUserModal() {
    $('#userModal').modal('show');
}

function addUser() {
    const username = $('#username').val();
    const email = $('#email').val();

    $.ajax({
        url: '/api/users',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ username: username, email: email }),
        success: function(response) {
            alert('Пользователь успешно добавлен!');
            $('#userModal').modal('hide');
            loadUsers();
        },
        error: function(error) {
            alert('Ошибка при добавлении пользователя');
        }
    });
}

function loadUsers() {
    $.getJSON('/api/users', function(data) {
        $('#userTable').empty();
        data.forEach(function(user) {
            $('#userTable').append(`
                <tr>
                    <td>${user.username}</td>
                    <td>${user.email}</td>
                    <td>${user.date_joined}</td>
                    <td><button class="btn btn-danger" onclick="deleteUser(${user.id})">Удалить</button></td>
                </tr>
            `);
        });
    });
}

function deleteUser(id) {
    $.ajax({
        url: `/api/users/${id}`,
        type: 'DELETE',
        success: function() {
            alert('Пользователь удален');
            loadUsers();
        },
        error: function() {
            alert('Ошибка при удалении пользователя');
        }
    });
}

// Код для управления задачами
function openTaskModal() {
    $('#taskModal').modal('show');
}

function addTask() {
    const title = $('#taskTitle').val();
    const description = $('#taskDescription').val();

    $.ajax({
        url: '/api/tasks',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ title: title, description: description }),
        success: function(response) {
            alert('Задача успешно добавлена!');
            $('#taskModal').modal('hide');
            loadTasks();
        },
        error: function(error) {
            alert('Ошибка при добавлении задачи');
        }
    });
}

function loadTasks() {
    $.getJSON('/api/tasks', function(data) {
        $('#taskTable').empty();
        data.forEach(function(task) {
            $('#taskTable').append(`
                <tr>
                    <td>${task.title}</td>
                    <td>${task.description}</td>
                    <td>${task.status}</td>
                    <td>${task.date_created}</td>
                    <td><button class="btn btn-danger" onclick="deleteTask(${task.id})">Удалить</button></td>
                </tr>
            `);
        });
    });
}

function deleteTask(id) {
    $.ajax({
        url: `/api/tasks/${id}`,
        type: 'DELETE',
        success: function() {
            alert('Задача удалена');
            loadTasks();
        },
        error: function() {
            alert('Ошибка при удалении задачи');
        }
    });
}

$(document).ready(function() {
    loadFiles();
    loadUsers();
    loadTasks();
});
