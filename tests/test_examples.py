import pytest

from examples.index import (
    vdom,
    render,
    split,
    scope,
    props,
    expressions,
    escaping,
    prevent_escaping,
    conditional,
    looping,
    components,
    callable,
    context,
)


@pytest.mark.parametrize(
    'target',
    [
        vdom,
        render,
        split,
        scope,
        props,
        expressions,
        escaping,
        prevent_escaping,
        conditional,
        looping,
        components,
        callable,
        context,
    ],
)
def test_examples(target):
    target.test()
