#!/usr/bin/python3
"""base py"""
import json


class Base:
    """define a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """define constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string representation of list_objs to a file"""
        content = []
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                content.append(json_dict)

        with open((cls.__name__ + ".json"), mode="w") as fd:
            json.dump(content, fd)

    @staticmethod
    def from_json_string(json_string):
        """decode json string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns a list of instances"""
        from models.square import Square
        from models.rectangle import Rectangle

        if cls.__name__ == "Square":
            r2 = Square(5)
        elif cls.__name__ == "Rectangle":
            r2 = Rectangle(3, 8)
        r2.update(**dictionary)
        return (r2)
