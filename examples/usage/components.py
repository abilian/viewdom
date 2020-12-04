from viewdom import html, render


def Heading():
    return html('<h1>My Title</h1>')


vdom = html('<{Heading} />')
result = render(vdom)
expected = '<h1>My Title</h1>'


def test():
    assert expected == result
