import pytest

LOGIN_DATA = [("Valid login", "Jajaja"), ("Invalid login", "Boohoo")]  # Test `test_login`


@pytest.mark.smoke
@pytest.mark.parametrize("login_type, is_valid", LOGIN_DATA)
def test_login(login_type, is_valid):
    print(login_type, is_valid)
    print("\n--- Login is successfully ---")


@pytest.mark.smoke
def test_logout(setup):
    print("\n--- Logout is successfully ---")
    print(f"Running tests on {setup.upper()} browser")
