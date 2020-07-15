from viewdom import html, render


# start-after
def Heading(title):
    return html('<h1>{title}</h1>')


title = 'My Title'
result = render(html('<{Heading} title={title} />'))
# '<h1>My Title</h1>'
# end-before
expected = '<h1>My Title</h1>'
