from random import randint


class CategoryManager:
    """Fake manager qui simule une récupération des infos de catégories et
    sous-catégories en base de données."""

    def get_parent_categories(self):
        """Simule une récupération de catégories à partir de la base de
        données."""
        return [f"Catégorie {n}" for n in range(1, randint(3, 6))]

    def get_child_categories(self, category):
        """Simule une récupération de sous-catégories à partir de la base de
        données."""
        category = category[-1]
        return [f"Catégorie {category}.{n}" for n in range(1, randint(3, 10))]


category_manager = CategoryManager()
