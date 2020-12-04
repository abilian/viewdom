from viewdom import html, render

vdom = html('Hello World')
# Hello World
result = render(vdom)
# 'Hello World'
expected = 'Hello World'


def test():
    assert expected == result
