from .controllers import home


class Application:
    """Représente l'application elle-même."""

    def __init__(self):
        """Initialise l'état de l'application."""
        self.session = {}

    def start(self):
        """Démarre l'application."""
        next_action = home
        kwargs = {}
        while next_action is not None:
            next_action, kwargs = next_action(self.session, **kwargs)
