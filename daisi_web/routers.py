class DatabaseRouter(object):
    def db_for_read(self, model, **hints):
        database = getattr(model, "_DATABASE")
        if (database == 'daisi'):
            return 'jalapeno'
        else:
            return 'default'
    def db_for_write(self, model, **hints):
        return 'default'