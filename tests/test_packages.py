from browsedocs.packages import (
    installed_packages,
    package_dependencies,
    package_description,
    package_homepage,
)


def test_installed_packages():
    """
    Test installed packages
    """
    assert "browsedocs" in installed_packages()
    assert "pytest" in installed_packages()


def test_package_dependencies():
    """
    Test package dependencies
    """
    assert "typer" in package_dependencies("browsedocs")
    # list no dev dependencies
    assert "pytest" not in package_dependencies("browsedocs")


def test_package_homepage():
    """
    Test package homepage
    """
    assert package_homepage("browsedocs") == "https://github.com/ggozad/browsedocs"


def test_package_description():
    """
    Test package description
    """
    print(package_description("browsedocs"))
    assert "# browsedocs" in package_description("browsedocs")
