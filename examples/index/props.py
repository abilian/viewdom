from viewdom import html, render

expected = '<div id="id-42" title="viewdom">Hello viewdom</div>'

# start-after
name = 'viewdom'
this_id = 42
result = render(
    html('<div id={f"id-{this_id}"} title="{name}">Hello {name}</div>')
)
# '<div id="id-42" title="viewdom">Hello viewdom</div>'
