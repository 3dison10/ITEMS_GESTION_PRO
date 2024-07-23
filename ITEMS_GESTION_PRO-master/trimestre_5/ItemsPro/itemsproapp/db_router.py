# itemsproapp/db_router.py

class ProductDatabaseRouter:
    """
    A router to control all database operations on models in the
    'Producto' application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read Producto models go to itemsprod.
        """
        if model._meta.app_label == 'itemsproapp' and model._meta.model_name == 'producto':
            return 'itemsprod'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write Producto models go to itemsprod.
        """
        if model._meta.app_label == 'itemsproapp' and model._meta.model_name == 'producto':
            return 'itemsprod'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the Producto app is involved.
        """
        if obj1._meta.app_label == 'itemsproapp' and obj2._meta.app_label == 'itemsproapp':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the Producto app only appears in the 'itemsprod'
        database.
        """
        if app_label == 'itemsproapp' and model_name == 'producto':
            return db == 'itemsprod'
        return None
