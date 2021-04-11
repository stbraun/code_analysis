# coding=utf-8
""" Configuration of nox test automation tool. """

import nox


@nox.session(python=['3.8', '3.9'])
def lint(session):
    """Run static analysis."""
    session.run("pipenv", "install", external=True)
    session.run("flake8", "code_analysis/", "tests/")


@nox.session(python=['3.8', '3.9'])
def tests(session):
    """Run tests for all supported versions of Python."""
    session.run("pipenv", "install", external=True)
    session.run("pytest", "tests/")
