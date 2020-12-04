from viewdom import html, render


def main(name='viewdom'):
    return render(html('<div>Hello {name}</div>'))


result = main()
# '<div>Hello viewdom</div>'
expected = '<div>Hello viewdom</div>'


def test():
    assert expected == result
