import json


class MultiTypeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Box):
            # Python knows how to encode a dictionary
            return {"__Box__": o.__dict__}
        if isinstance(o, set):
            return {"__set__": list(o)}
        else:
            super().default(o)


def multiple_type_decoder(o):
    if "__Box__" in o:
        item = o["__Box__"]
        ret_obj = Box(item["length"], item["width"])
        ret_obj.color = item["_color"]
        ret_obj._contents = item["_contents"]
        return ret_obj
    if "__set__" in o:
        return set(o["__set__"])
    else:
        return o


class Box:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
        self._color = "Blue"
        self._contents = set()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def display_contents(self):
        print(self._contents)

    def add_contents(self, item):
        self._contents.add(item)


my_box = Box(2,3)
print(my_box.color)
my_box.color = "Red"
print(my_box.color)
my_box.add_contents("Shoes")
my_box.add_contents("Hats")
my_box.add_contents("Bags")
my_box.display_contents()


box_enc = json.dumps(my_box, cls=MultiTypeEncoder)
print(box_enc)
box_dec = json.loads(box_enc, object_hook=multiple_type_decoder)
print(box_dec)
print(box_dec.__dict__)
print(type(box_dec._contents))
