#!/usr/bin/env python3
def array_of_names(var):
    full_names = []
    for firstname, lastname in var.items():
        full_names.append(firstname.capitalize() + " " + lastname.capitalize())
    return full_names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
