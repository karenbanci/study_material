# BEGIN CLASS Phone -------------------------------------------
class Phone:
    """ Phone as a base class for later inheritance """

    # class ("static") members and intended constants
    DEFAULT_NUM = "0000000000"
    VALID_PH_NUM_LEN = 10

    # initializer ("constructor") method ------------------------
    def __init__(self, num=DEFAULT_NUM):
        # instance attributes (see mutator for details)
        if not self.set_number(num):
            self.set_number(self.DEFAULT_NUM)

    # mutator method(s) -------------------------------------
    def set_number(self, num):
        # valid_phone_num() tests the length and if good, "purifies"
        ph_w_junk_stripped = self.valid_phone_num(num)
        if ph_w_junk_stripped is None:
            return False

        # if a not None the return value is perfect
        self.number = ph_w_junk_stripped
        return True

    # accessor method(s) ---------------------------------
    def get_number(self):
        return self.number

    # stringizer and console output ---------------------
    def __str__(self):
        """ turn '1234567890' into '(123)456-7890' """

        # build slowly for clarity -- could be done in one long statement
        ret_str = "("
        ret_str += self.number[0:3]
        ret_str += ")"
        ret_str += self.number[3:6]
        ret_str += "-"
        ret_str += self.number[6:]

        return ret_str

    def show(self):
        print(self)

    # for demonstration ------------------------------------------
    def dialing(self):
        return "Now dialing " + str(self) + "\n"

    def redialing(self, num_times):
        ret_str = "Trying number " + str(num_times) + " times ...\n"

        for k in range(num_times):
            ret_str += self.dialing()
        ret_str += "done.\n"

        return ret_str

    # helper for vetting Phone numbers  --------------------------
    @staticmethod
    def extract_numeric_digits(the_num):
        """ store only digits '213-555-1212' becomes '2135551212'
            returns None if non-string, else
            the string minus non-numerics """
        if type(the_num) != str:
            return None
        # else
        the_length = len(the_num)
        number = ""
        for k in range(0, the_length):
            next_digit = the_num[k]
            if next_digit.isdigit():
                number = number + next_digit
        return number

    @classmethod
    def valid_phone_num(cls, the_num):
        """ returns the purified number if valid, else None """
        # first check that it's a string
        if type(the_num) != str:
            return None
        # throw away non-numerics
        pure_number = cls.extract_numeric_digits(the_num)
        # check length
        if len(pure_number) != cls.VALID_PH_NUM_LEN:
            return None
        return pure_number


# client (as a function) -----------------------------------
def main():
    bad_phone = Phone("bad bad number")
    default_phone = Phone()
    good_phone_1 = Phone("( 213)  123 - 3333  ")
    good_phone_2 = Phone("444 555-5333")

    # show the Contacts right after instantiation ---------------
    print("\nBefore mutators -------------------:")
    print("Bad Phone:" + str(bad_phone))
    print("Default Phone:" + str(default_phone))
    print("Good Phone 1:" + str(good_phone_1))
    print("Good Phone 2:" + str(good_phone_2))

    # (try to) mutate a few attributes of bad phone
    bad_phone.set_number("(605)  555-1212")  # should work
    bad_phone.set_number("123-3333")  # should fail

    # (try to) mutate a few attributes of default phone
    default_phone.set_number("1346bad really bad")  # should fail
    default_phone.set_number("123-456-7890")  # should work

    # show the Phones  after mutator calls  -----------------------
    print("\nAfter mutators -------------------:")
    print("Bad Phone:" + str(bad_phone))
    print("Default Phone:" + str(default_phone))

    # test the accessor   ---------------------------------------
    print("\nTesting accessors -------------------:")
    print(" ... on bad phone: ", bad_phone.get_number())
    print(" ... on default phone: ", default_phone.get_number())

    # test the dialer and redialer   ---------------------------
    print("\ndialing() -------------------:")
    print("good phone 1 ...\n  "
          "   " + good_phone_1.dialing())
    print("good phone 2 ...\n  "
          "   " + good_phone_2.dialing())
    print()

    print("\nredialing() -------------------:")
    print("good phone 1 ...\n  "
          "   " + good_phone_1.redialing(3))
    print("good phone 2 ...\n  "
          "   " + good_phone_2.redialing(3))
    print()

# -------------- main program -------------------
if __name__ == "__main__":
    main()

""" -------------------------- RUN ----------------------------

Before mutators -------------------:
Bad Phone:(000)000-0000
Default Phone:(000)000-0000
Good Phone 1:(213)123-3333
Good Phone 2:(444)555-5333

After mutators -------------------:
Bad Phone:(605)555-1212
Default Phone:(123)456-7890

Testing accessors -------------------:
 ... on bad phone:  6055551212
 ... on default phone:  1234567890

dialing() -------------------:
good phone 1 ...
     Now dialing (213)123-3333

good phone 2 ...
     Now dialing (444)555-5333



redialing() -------------------:
good phone 1 ...
     Trying number 3 times ...
Now dialing (213)123-3333
Now dialing (213)123-3333
Now dialing (213)123-3333
done.

good phone 2 ...
     Trying number 3 times ...
Now dialing (444)555-5333
Now dialing (444)555-5333
Now dialing (444)555-5333
done.


-------------------------------------------------------------- """