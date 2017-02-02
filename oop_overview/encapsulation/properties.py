class PropertySoursce:

    def __init__(self, attribute):
        self.__attribute = attribute

    @propotry
    def attribute(self):
        return self.__attribute

    @attribute
    def __set__(self, attribute):
        self.__attribute = attribute


test = PropertySoursce('attribute')
print(test.attribute)
test.attribute = 'new attribute'
print(test.attribute)