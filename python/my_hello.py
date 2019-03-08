#!/usr/bin/env python


class my_hello_class:
    ''' Test class

    Only basic constructor
    '''

    def adding_header_to_msg(self, new_string):
        if not isinstance(new_string, str):
            print("Parameter not a string")
            return ""

        header = "address: 0x0101;"
        return (header + new_string)

hello_object = my_hello_class()

print(my_hello_class.__doc__)