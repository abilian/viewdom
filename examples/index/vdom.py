from viewdom import VDOMNode, html

result = html('''<div>Hello World</div>''')
expected = VDOMNode(tag='div', props={}, children=['Hello World'])


def test():
    assert expected == result
