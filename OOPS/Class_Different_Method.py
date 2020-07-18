class MultipleMethod:
    value = 100 # class level variable

    def instance_method(self):
        print('instance method')
    
    @classmethod
    def class_method(cls):
        print('class_method ', cls.value)
    @staticmethod
    def static_method():
        print('static_method')
    
a = MultipleMethod()
a.instance_method()
a.class_method()
MultipleMethod.static_method()