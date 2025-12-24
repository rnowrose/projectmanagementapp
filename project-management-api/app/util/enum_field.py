from peewee import CharField

class EnumField(CharField):
    """Custom field for enum handling"""
    
    def __init__(self, enum_class, *args, **kwargs):
        self.enum_class = enum_class
        max_len = max(len(e.value) for e in enum_class)
        kwargs.setdefault('max_length', max_len)
        super().__init__(*args, **kwargs)
    
    def db_value(self, value):
        """Convert enum to string for database"""
        if isinstance(value, self.enum_class):
            return value.value
        return value
    
    def python_value(self, value):
        """Convert string from database to enum"""
        if value is not None and not isinstance(value, self.enum_class):
            try:
                return self.enum_class(value)
            except ValueError:
                return None
        return value