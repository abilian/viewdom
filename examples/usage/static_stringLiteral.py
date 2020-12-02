from viewdom import html, render

vdom = html('Hello World')
# Hello World
result = render(vdom)
# 'Hello World'
# end-before
expected = 'Hello World'
