from viewdom import html, render

name = 'viewdom'
result = render(html('<div>Hello {1 + 3}</div>'))
expected = '<div>Hello 4</div>'


def test():
    assert expected == result
