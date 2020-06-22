from viewdom import VDOM

expected = VDOM(tag='div', props={}, children=['Hello World'])

# start-after
from viewdom import html
result = html('''<div>Hello World</div>''')
# VDOM(tag='div', props={}, children=['Hello World'])
