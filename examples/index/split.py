from viewdom import html, render

vdom = html('<div>Hello World</div>')
result = render(vdom)
expected = '<div>Hello World</div>'


def test():
    return expected, result
