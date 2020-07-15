from viewdom import html, render


# start-after
def Heading(title='My Title'):
    return html('<h1>{title}</h1>')


result = render(html('<{Heading} />'))
# '<h1>My Title</h1>'
# end-before
expected = '<h1>My Title</h1>'
