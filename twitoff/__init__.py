"""Entry point for TwitOff."""
# This is everything that will be in the __init__.py file


from .app import create_app
APP = create_app()
