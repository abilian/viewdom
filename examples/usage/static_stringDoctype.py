from markupsafe import Markup

from viewdom import html, render

doctype = Markup('<!DOCTYPE html>\n')
vdom = html('''{doctype}<div>Hello World</div>''')
# Markup('<!DOCTYPE html>\n'), VDOMNode(tag='div', props={}, children=['Hello World'])]

result = render(vdom)
# '<!DOCTYPE html>\n<div>Hello World</div>'
expected = '<!DOCTYPE html>\n<div>Hello World</div>'


def test():
    assert expected == result
