import pkg_resources
from importlib import metadata


def installed_packages():
    """
    List all installed python packages
    """

    return sorted([dist.project_name for dist in pkg_resources.working_set])


def package_dependencies(package: str):
    """
    List all dependencies of a given package
    """

    dist = pkg_resources.get_distribution(package)
    return sorted([dep.project_name for dep in dist.requires()])


def package_homepage(package: str):
    """
    Get the homepage of a given package
    """

    return metadata.distribution(package).metadata.get("Home-page")
