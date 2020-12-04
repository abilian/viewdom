from viewdom import html, render


def make_bigly(name: str) -> str:
    return f'BIGLY: {name.upper()}'


name = 'viewdom'
result = render(html('<div>Hello {make_bigly(name)}</div>'))
# '<div>Hello BIGLY: VIEWDOM</div>'
expected = '<div>Hello BIGLY: VIEWDOM</div>'


def test():
    assert expected == result
