from viewdom import html, render

vdom = html('''<div class="container{1}">Hello World</div>''')
# VDOM(tag='div', props={'class': 'container1'}, children=['Hello World'])

result = render(vdom)
# '<div class="container1">Hello World</div>'
expected = '<div class="container1">Hello World</div>'


def test():
    assert expected == result
