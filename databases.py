from dataclasses import dataclass
@dataclass
class _DB:
    id: int
    @classmethod
    def fields(cls):
        return cls.__dataclass_fields__
    @classmethod
    def get_field(cls, field):
        return cls.fields()[field]
    @classmethod
    def get_default(cls, field):
        return cls.get_field(field).default
    @classmethod
    def get_type(cls, field):
        return cls.get_field(field).type

@dataclass
class User(_DB):
    chat_id: str | None = None

def get_all_classes():
    return [name for name, _class in globals().items() if type(_class) == type]
def get_class_by_str(name):
    return globals()[name]