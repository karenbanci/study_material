x_int = 0b11010
y_int = 0b10011
print(f"The both integer numbers {x_int} and {y_int}")

x_int = 0x2DA1
y_int = 0xA378
print(f"\nThe both without conversion numbers {x_int} and {y_int}")

x_int = 0b11010
y_int = 0b10011
print("\nfirst number in decimal and binary form:   {:4} {:>20}". \
      format(x_int, bin(x_int)))
print("\nsecond number in decimal and binary form:  {:4} {:>20}". \
      format(y_int, bin(y_int)))
print()

x_int = 0x2DA1
y_int = 0xA378
print("\nfirst number in decimal and hex form:   {:4} {:>20}". \
      format(x_int, hex(x_int)))
print("\nsecond number in decimal and hex form:  {:4} {:>20}". \
      format(y_int, hex(y_int)))

""" -------------------------- RUN -----------------------------

first number in decimal and binary form:     26              0b11010
second number in decimal and binary form:    19              0b10011

first number in decimal and hex form:   11681               0x2da1
second number in decimal and hex form:  41848               0xa378

-------------------------------------------------------------- """

x_int = 0b11010
y_int = 0b10011
print("first number in decimal and binary form:   {:4} {:>20}". \
      format(x_int, bin(x_int)[2:]))
print("second number in decimal and binary form:  {:4} {:>20}". \
      format(y_int, bin(x_int)[2:]))
print()

x_int = 0x2DA1
y_int = 0xA378
print("first number in decimal and hex form:   {:4} {:>20}". \
      format(x_int, hex(x_int)[2:]))
print("second number in decimal and hex form:  {:4} {:>20}". \
      format(y_int, hex(y_int)[2:]))

""" -------------------------- RUN -----------------------------

first number in decimal and binary form:     26                11010
second number in decimal and binary form:    19                11010

first number in decimal and hex form:   11681                 2da1
second number in decimal and hex form:  41848                 a378

-------------------------------------------------------------- """