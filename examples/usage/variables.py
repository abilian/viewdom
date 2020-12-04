from viewdom import html, render

name = 'viewdom'
result = render(html('<div>Hello {name}</div>'))

# '<div>Hello viewdom</div>'
expected = '<div>Hello viewdom</div>'


def test():
    assert expected == result
