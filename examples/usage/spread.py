from viewdom import html, render


# start-after
def Heading(children, title):
    props = dict(a='A', b='B')
    return html('<div ...{props}>Hello</div>')


result = render(html('<{Heading} title="My Title">Child<//>'))
# '<div a="A" b="B">Hello</div>'
# end-before
expected = '<div a="A" b="B">Hello</div>'
