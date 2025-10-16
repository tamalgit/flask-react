from flask import Blueprint, jsonify, request, abort
from sqlalchemy import select

from . import db
from .models import Todo

api_bp = Blueprint('api', __name__)


@api_bp.get('/hello')
def hello():
    return jsonify(message='Hello from Flask'), 200

@api_bp.post('/echo')
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify(received=data), 200


@api_bp.get('/todos')
def list_todos():
    todos = db.session.execute(select(Todo).order_by(Todo.id.asc())).scalars().all()
    return jsonify([t.to_dict() for t in todos])


@api_bp.post('/todos')
def create_todo():
    data = request.get_json(silent=True) or {}
    title = (data.get('title') or '').strip()
    if not title:
        abort(400, description='title is required')
    todo = Todo(title=title)
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_dict()), 201


@api_bp.patch('/todos/<int:todo_id>')
def update_todo(todo_id: int):
    todo = db.session.get(Todo, todo_id)
    if not todo:
        abort(404)
    data = request.get_json(silent=True) or {}
    if 'title' in data:
        title = (data.get('title') or '').strip()
        if not title:
            abort(400, description='title cannot be empty')
        todo.title = title
    if 'completed' in data:
        todo.completed = bool(data.get('completed'))
    db.session.commit()
    return jsonify(todo.to_dict())


@api_bp.delete('/todos/<int:todo_id>')
def delete_todo(todo_id: int):
    todo = db.session.get(Todo, todo_id)
    if not todo:
        abort(404)
    db.session.delete(todo)
    db.session.commit()
    return '', 204


