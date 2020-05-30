"""
Provide various PEP 544 protocol specs.
"""

from typing import Union, NamedTuple, Mapping, List

# Can't go further due to mypy bug on recursion
Children = Union[str, List]
VDOM = NamedTuple("VDOM", [
    ('tag', str),
    ('props', Mapping),
    ('children', Children),
])
