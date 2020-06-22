from dataclasses import dataclass

from viewdom import html, render

expected = '<div>Hello viewdom</div>'


# start-after
@dataclass
class Greeting:
    name: str

    def __call__(self):
        return f'Hello {self.name}'


greeting = Greeting(name='viewdom')
result = render(html('<div><{greeting} /></div>'))
# '<div>Hello viewdom</div>'
