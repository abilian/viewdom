from viewdom import html, render

vdom = html('''<div>Hello World</div>''')
# VDOM(tag='div', props={}, children=['Hello World'])

result = render(vdom)
# '<div>Hello World</div>'
expected = '<div>Hello World</div>'


def test():
    assert expected == result
