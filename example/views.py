def default_menu_formatter(menu):
    """Formate l'apparence visuelle d'un menu."""
    lines = [
        "",
        menu.title,
        "=" * len(menu.title),
        "",
        *(f"  {i}. {choice}" for i, (choice, *_) in menu.choices.items()),
        "",
        "  Votre choix : ",
    ]
    return "\n".join(lines)


class SimpleView:
    """Représente une vue minimale capable d'afficher des messages à
    l'utilisateur."""

    def display_message(self, message):
        """Affiche un message à l'utilisateur."""
        print(f"\n{message}\n")


class MenuView(SimpleView):
    """Gère la présentation du menu à l'écran."""

    def __init__(self, menu, formatter=default_menu_formatter):
        """Constuit une nouvelle vue de menu."""
        self.menu = menu
        self.formatter = formatter

    def render(self):
        """Affiche le menu et demande à l'utilisateur de faire un choix."""
        return input(self.formatter(self.menu))

    def display_invalid_choice(self):
        """Affiche un message à l'utilisateur."""
        print("\nVotre choix est invalide. Réessayez !\n")
