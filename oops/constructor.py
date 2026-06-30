class person:
    def __init__(self, n, o):
        # print("I am a constructor method called when object initiated")
        self.name=n
        self.occu=o

    def info(self):
        print(f"{self.name} is a {self.occu}")

obj=person("ankit", "sde") # self passed automatically
obj.info()
