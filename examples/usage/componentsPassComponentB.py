from viewdom import html, render


def DefaultHeading():
    return html('<h1>Default Heading</h1>')


def OtherHeading():
    return html('<h1>Other Heading</h1>')


def Body(heading=DefaultHeading):
    return html('<body><{heading} /></body>')


result = render(html('<{Body} heading={OtherHeading}/>'))
expected = '<body><h1>Other Heading</h1></body>'


def test():
    return expected, result
