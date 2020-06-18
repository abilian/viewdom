from viewdom import html, render

title = 'My Todos'


def Todo(label):
    return html('<li>{label}</li>')


def TodoList(todos):
    return html('<ul>{[Todo(label) for label in todos]}</ul>')


def TodoApp(title, todolist):
    return html('<h1>{title}</h1>{todolist}')


def main():
    todos = ['first']
    # noinspection PyUnusedLocal
    todo_list = TodoList(todos)
    return render(html('''
      <{TodoApp} title="My Todos" todolist={todo_list} />
    '''))


result = main()
# '<h1>My Todos</h1><ul><li>first</li></ul>'
# end-before
expected = '<h1>My Todos</h1><ul><li>first</li></ul>'
