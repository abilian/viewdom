from viewdom import html, render

name = 'viewdom'
result = render(html('<div>Hello {name}</div>'))
expected = '<div>Hello viewdom</div>'


def test():
    assert expected == result
