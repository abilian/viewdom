from viewdom import html, render

vdom = html('''<div>Hello World</div>''')
# VDOM(tag='div', props={}, children=['Hello World'])

result = render(vdom)
# '<div>Hello World</div>'
# end-before
expected = '<div>Hello World</div>'
