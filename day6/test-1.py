full_name = lambda fn, ln: fn.strip().title() + " "+ln.strip().title()

print(full_name("venkatram ", "Veerareddy"))

scifi_authors = [
    "Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthus C.Clarke" , "Frank Herbert"
]

scifi_authors.sort(key=lambda name:name.split(" ")[-1])

print(scifi_authors)