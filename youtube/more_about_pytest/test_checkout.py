import pytest
from pytest_check import check


@pytest.mark.regression
def test_checkout():
    print("\n--- Checkout is successfully ---")


@pytest.mark.xfail
def test_logout():
    with check:
        assert False
    print("\n--- Check Xfail ---")
