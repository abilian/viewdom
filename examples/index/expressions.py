from viewdom import html, render

name = 'viewdom'

result = render(html('<div>Hello {name.upper()}</div>'))
expected = '<div>Hello VIEWDOM</div>'


def test():
    assert expected == result
