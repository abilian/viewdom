from viewdom import html, render
from .variables import name


def main():
    return render(html('<div>Hello {name}</div>'))


result = main()
# '<div>Hello viewdom</div>'
expected = '<div>Hello viewdom</div>'


def test():
    assert expected == result
