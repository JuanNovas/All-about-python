# -- @classmethod -- 

# Decorator for methods
# Makes the method callable from the class
# The first parameter is the class itself not an instance, even if called with an instance


class ExampleClass():
    
    def normal_method(self):
        pass
    
    @classmethod
    def class_method(cls):
        pass
    
    
    
# Real example:

## Django Model
### Github: https://github.com/No-Country-simulation/s18-03-m-python-react/blob/dev/Backend/assistances/models.py
class Asistance():
    
    @classmethod
    def get_report(cls, month: int=None, employee_id: int=None) -> dict:
        # Logic to get a report
        data = {}
        return data