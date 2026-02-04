import inspect


def test_skill_interfaces():
    """Skills interfaces should accept defined parameters."""
    # NOTE: This intentionally fails until implementation exists.
    from chimera.skills import (  # noqa: F401
        skill_fetch_trends,
        skill_generate_content,
        skill_publish_content,
    )

    sig_fetch = inspect.signature(skill_fetch_trends)
    sig_generate = inspect.signature(skill_generate_content)
    sig_publish = inspect.signature(skill_publish_content)

    assert list(sig_fetch.parameters.keys()) == ["payload"]
    assert list(sig_generate.parameters.keys()) == ["payload"]
    assert list(sig_publish.parameters.keys()) == ["payload"]
