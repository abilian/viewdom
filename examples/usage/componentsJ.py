from dataclasses import dataclass
from typing import Iterable

from viewdom import html, render
from viewdom import VDOM

title = 'My Todos'


def Todo(label):
    return html('<li>{label}</li>')


@dataclass
class TodoList:
    todos: Iterable

    def __call__(self) -> VDOM:
        return html('<ul>{[Todo(label) for label in self.todos]}</ul>')


def TodoApp(title, todolist):
    return html('<h1>{title}</h1>{todolist}')


def main():
    todos = ['first']
    tl = TodoList(todos)
    return render(html('''
      <{TodoApp} title="My Todos" todolist={tl} />
    '''))


result = main()
# '<h1>My Todos</h1><ul><li>first</li></ul>'
# end-before
expected = '<h1>My Todos</h1><ul><li>first</li></ul>'
