from viewdom import html, render

vdom = html('''<div class="container">Hello World</div>''')
# VDOM(tag='div', props={'class': 'container'}, children=['Hello World'])

result = render(vdom)
# '<div class="container">Hello World</div>'
expected = '<div class="container">Hello World</div>'


def test():
    assert expected == result
