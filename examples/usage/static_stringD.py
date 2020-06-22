from viewdom import html, render

vdom = html('''<div>Hello <span>World<em>!</em></span></div>''')
# VDOM(tag='div', props={}, children=['Hello ', VDOM(tag='span', props={}, \
# children=['World', VDOM(tag='em', props={}, children=['!'])])])

result = render(vdom)
# '<div>Hello <span>World<em>!</em></span></div>'
# end-before
expected = '<div>Hello <span>World<em>!</em></span></div>'
