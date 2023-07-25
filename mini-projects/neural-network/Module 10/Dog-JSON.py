import collections
import json
import collections

flat = "A Pancake"
bumpy = ["A Pancake", "A sausage"] # I can't use f.write(bumpy)
"""
JSON provides some mechanisms fo taking bumpy objects and actually serializing
them. Converting them to a string like structure that can be saved to a file.
But later retrieved and recreated back into the original object. 
"""
really_bumpy = [ "A Pancake", [4,3, "A sausage"], ("A", "Tuple"), {4: "Four", 5: "Five"}]
bad_bumpy = collections.deque(really_bumpy)


class Dog:
    def __init__(self, name, age, tricks):
        self._name = name
        self._age = age
        self._tricks = tricks

    def __str__(self):
        ret_str = f"{self._name} is {self._age} years old and knows"
        ret_str += f"the following tricks:\n"
        for trick in self._tricks:
            ret_str += f"- {trick}\n"
        return ret_str


fido = Dog("Fido", 10, ["Sit", "Stay", "Rol Over", "Type"])


class MultiTypeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, collections.deque):
            return {"__deque__": list(o)}
        elif isinstance(o, Dog):
            # Python knows how to encode a dictionary
            return {"__Dog__": o.__dict__}
        else:
            json.JSONEncoder.default(o)


def multiple_type_decoder(o):
    if "__deque__" in o:
        return collections.deque(o["__deque__"])
    # unpack dictionary to object
    elif "__Dog__" in o:
        # That itself is a dictionary, extract each those
        dec_obj = o["__Dog__"]
        name = dec_obj["_name"]
        age = dec_obj["_age"]
        tricks = list(dec_obj["_tricks"])
        ret_obj = Dog(name, age, tricks)
        return ret_obj
    else:
        return o


with open("data.txt", "w") as f:
    json.dump(fido, f, cls=MultiTypeEncoder)

with open("data.txt", "r") as f:
    my_obj = json.load(f, object_hook=multiple_type_decoder)
    print(type(my_obj))
    print(my_obj)

"""
box_enc = json.dumps(fido, f, cls=MultiTypeEncoder)
box_dec = json.loads(box_enc, object_hook=multiple_type_decoder)

"""