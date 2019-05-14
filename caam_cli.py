# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the ``caam()`` function."""
import click
from gitone.caam import caam


@click.command()
@click.argument("message", nargs=-1)
def caam_cli(message: str) -> None:
    """Add and commit all changes.

    :param message: The commit message to be passed to ``caam()``.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
           There is no need wrap the commit message in quotes.
    """
    caam(" ".join(message)) if message else caam()
