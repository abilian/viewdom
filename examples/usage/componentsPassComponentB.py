from viewdom import html, render


# start-after
def DefaultHeading():
    return html('<h1>Default Heading</h1>')


def OtherHeading():
    return html('<h1>Other Heading</h1>')


def Body(heading=DefaultHeading):
    return html('<body><{heading} /></body>')


result = render(html('<{Body} heading={OtherHeading}/>'))
# '<body><h1>Other Heading</h1></body>'
# end-before
expected = '<body><h1>Other Heading</h1></body>'
