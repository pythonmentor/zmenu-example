class Menu:
    """Représente un menu."""

    def __init__(self, title):
        """Construit un nouveau menu."""
        self.title = title
        self.choices = {}

    def add(self, choices, action=None, **kwargs):
        """Ajoute une entrée au menu."""
        if not isinstance(choices, (list, tuple)):
            choices = [choices]
        for choice in choices:
            key = str(len(self.choices) + 1)
            self.choices[key] = choice, action, kwargs

    def __contains__(self, choice):
        """Valide choix de l'utilisateur."""
        return choice in self.choices

    def __getitem__(self, choice):
        """Gère l'accès au choix de l'utilisateur."""
        return self.choices.get(choice)
