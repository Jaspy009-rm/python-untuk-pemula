# Class dengan method yang memakai parameter self
class Cat:
    color = "hitam"

    def say(myself):
        print("My color is %s" % myself.color)

cat1 = Cat()
cat1.say()  # My color is hitam