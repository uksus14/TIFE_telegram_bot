from dataclasses import dataclass
@dataclass
class _DB:
    id: int
    @classmethod
    def fields(cls):
        return cls.__dataclass_fields__
    @classmethod
    def get_field(cls, field):
        try:
            answer = cls.fields()[field]
        except KeyError:
            raise KeyError(f"{field} не является полем класса {cls}")
        return answer
    @classmethod
    def get_default(cls, field):
        return cls.get_field(field).default
    @classmethod
    def get_type(cls, field):
        return cls.get_field(field).type

    def to_dict(self):
        return {key: self.__getattribute__(key) for key in self.fields()}

def get_all_classes():
    classes = {name: _class for name, _class in globals().items() if type(_class) == type}
    return [name for name in classes if _DB in classes[name].mro()[1:]]
def get_class_by_str(name):
    try:
        answer = globals()[name]
    except KeyError:
        raise KeyError(f"'{name}' не является существующей базой данных")
    return answer


@dataclass
class User(_DB):
    chat_id: str | None = None
