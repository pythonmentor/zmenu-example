from .managers import category_manager
from .utils import Menu
from .views import MenuView


def home(session):
    """Contrôle le menu d'accueil."""
    # On vide la session à chaque fois qu'on revient à l'accueil
    session.clear()

    # Créer le menu et la vue
    menu = Menu("Menu d'accueil")
    menu.add("Sélectionner une catégorie", select_category)
    menu.add(
        "Quitter l'application",
        confirm_quit_controller,
        from_controller=home,
    )

    view = MenuView(menu)

    # Traitement du menu et validation du choix de l'utilisateur
    choice = view.render()
    if choice in menu:
        option, next_action, kwargs = menu[choice]
        return next_action, kwargs

    # Erreur de saisie de l'utilisateur
    view.display_invalid_choice()
    return home, {}


def select_category(session):
    """Contrôle le choix de la catégorie."""
    categories = category_manager.get_parent_categories()

    # Créer le menu et la vue
    menu = Menu("Choix des catégories")
    menu.add(categories, select_subcategory)
    menu.add("Retour à l'accueil", home)
    menu.add(
        "Quitter l'application",
        confirm_quit_controller,
        from_controller=select_category,
    )

    view = MenuView(menu)

    # Traitement du menu et validation du choix de l'utilisateur
    choice = view.render()
    if choice in menu:
        option, next_action, kwargs = menu[choice]
        if option in categories:
            session['category'] = option
        return next_action, kwargs

    # Erreur de saisie de l'utilisateur
    view.display_invalid_choice()
    return select_category, {}


def select_subcategory(session):
    """Contrôle le choix de la sous-catégorie."""
    category = session["category"]
    subcategories = category_manager.get_child_categories(category)

    # Créer le menu et la vue
    menu = Menu(f"Choix de la sous-catégorie pour {category.lower()}")
    menu.add(subcategories, done)
    menu.add("Retour à l'accueil", home)
    menu.add("Retour au choix de la catégorie", select_category)
    menu.add(
        "Quitter l'application",
        confirm_quit_controller,
        from_controller=select_subcategory,
    )

    view = MenuView(menu)

    # Traitement du menu et validation du choix de l'utilisateur
    choice = view.render()
    if choice in menu:
        option, next_action, kwargs = menu[choice]
        if option in subcategories:
            session['subcategory'] = option
        return next_action, kwargs

    # Erreur de saisie de l'utilisateur
    view.display_invalid_choice()
    return select_subcategory


def done(session):
    menu = Menu(
        "Voulez-vous quittez l'application ou retourner à l'accueil ? "
    )
    menu.add("Retourner à l'accueil", home)
    menu.add(
        "Quitter l'application",
        confirm_quit_controller,
        from_controller=done,
    )

    view = MenuView(menu)

    # Faisons qch avec la catégorie et la sous-catégorie
    category = session.get('category')
    subcategory = session.get('subcategory')
    view.display_message(
        f"La catégorie que vous avez choisie est {category}\n"
        f"...et la sous-catégorie est {subcategory}. "
        "Merci pour votre sélection !"
    )

    # Traitement du menu et validation du choix de l'utilisateur
    choice = view.render()
    if choice in menu:
        option, next_action, kwargs = menu[choice]
        return next_action, kwargs

    # Erreur de saisie de l'utilisateur
    view.display_invalid_choice()
    return done, {}


def confirm_quit_controller(session, from_controller):
    menu = Menu("Voulez-vous vraiment quitter l'application ? ")
    menu.add("Non", from_controller)
    menu.add("Oui")

    view = MenuView(menu)

    # Traitement du menu et validation du choix de l'utilisateur
    choice = view.render()
    if choice in menu:
        option, next_action, kwargs = menu[choice]
        if option == "Oui":
            view.display_message("Au revoir !")
        return next_action, kwargs

    # Erreur de saisie de l'utilisateur
    view.display_invalid_choice()
    return confirm_quit_controller, {"from_controller": from_controller}
