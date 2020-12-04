from viewdom import html, render

vdom = html('''<div editable={True}>Hello World</div>''')
# VDOM(tag='div', props={'editable': True}, children=['Hello World'])

result = render(vdom)
# '<div editable>Hello World</div>'
expected = '<div editable>Hello World</div>'


def test():
    assert expected == result
