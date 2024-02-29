#!/usr/bin/env python3

class Dog:
    def __init__(self,name,breed="Mutt") :
        self.name=name
        self.breed=breed
    def showing_self(self):
        print(f"Showing {self}")
        return self
fido=Dog("Fido")
print(fido.name)
snoopy=Dog("Snoopy","pet")
print(snoopy.name,snoopy.breed)

