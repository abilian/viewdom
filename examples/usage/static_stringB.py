from viewdom import html, render

vdom = html('<div class="container">Hello World</div>')
result = render(vdom)
expected = '<div class="container">Hello World</div>'


def test():
    return expected, result
