class AcessBase:
    def __init__(self, type_, strength):
        self.type=type_
        self.strength=strength


# accessing type 1

class chid(AcessBase):
    def __init__(self, type_, strength, spiceLevel):
        self.type=type_
        self.strength=strength    # not an efficient way of creating constructor copying type and strength again
        self.spiceLevel=spiceLevel


#  accessing type 2

class chid(AcessBase):
    def __init__(self, type_, strength, spiceLevel):
        AcessBase.__init__(self, type_, strength)
        self.spiceLevel=spiceLevel


#   accessing type 3   (best way to access using super)

class chid(AcessBase):
    def __init__(self, type_, strength, spiceLevel):
        super().__init__(type, strength)
        self.spiceLevel=spiceLevel