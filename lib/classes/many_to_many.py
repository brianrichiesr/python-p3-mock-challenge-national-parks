import re

class NationalPark:

    def __init__(self, name):
        self.original_value = None
        self.flag = False
        self.name = name
    
    @property
    def original_value(self):
        return self._original_value
    
    @original_value.setter
    def original_value(self, original_value):
        self._original_value = original_value
    
    @property
    def flag(self):
        return self._flag
    
    @flag.setter
    def flag(self, flag):
        self._flag = flag
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if self.flag:
            self._name = self.original_value
        elif not isinstance(name, str) or len(name) <= 3:
            self._name = self.original_value
        else:
            self._name = name
            self.flag = True
            self.original_value = name        

        
    def trips(self):
        return [result for result in Trip.all if result.national_park == self]
    
    def visitors(self):
        return list({result.visitor for result in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visit_dict = {}
        for result in self.trips():
            if hasattr(visit_dict, result.visitor.name):
                visit_dict[result.visitor.name] + 1
            else:
                visit_dict[result.visitor.name] = 1
        x = [key for key, value in visit_dict.items() if value == max(visit_dict.values())]

        for traveller in Visitor.all:
            if traveller.name == x[0]:
                return traveller


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.start_original_value = None
        self.end_original_value = None
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)
    
    @property
    def start_original_value(self):
        return self._start_original_value
    
    @start_original_value.setter
    def start_original_value(self, start_original_value):
        self._start_original_value = start_original_value
    
    @property
    def end_original_value(self):
        return self._end_original_value
    
    @end_original_value.setter
    def end_original_value(self, end_original_value):
        self._end_original_value = end_original_value
    
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        
        pattern = r"^\w+\s\d{1,2}\w{2}$"
        if not isinstance(start_date, str):
            self._start_date = self.start_original_value
        elif not re.search(pattern, start_date):
            self._start_date = self.start_original_value
        else:
            self._start_date = start_date
            self.start_original_value = start_date
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):

        pattern = r"^\w+\s\d{1,2}\w{2}$"
        if not isinstance(end_date, str):
            self.end_date = self.end_original_value
        elif not re.search(pattern, end_date):
            self.end_date = self.end_original_value
        else:
            self._end_date = end_date
            self.end_original_value = end_date

        


class Visitor:

    all = []

    def __init__(self, name):
        self.original_value = None
        self.name = name
        type(self).all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            self._name = self._original_value
        elif not 1 <= len(name) <= 15:
            self._name = self._original_value
        else:
            self._name = name
            self._original_value = name
    
    @property
    def original_value(self):
        return self._original_value
    
    @original_value.setter
    def original_value(self, original_value):
        self._original_value = original_value
        
    def trips(self):
        return [result for result in Trip.all if result.visitor is self]
    
    def national_parks(self):
        return list({result.national_park for result in self.trips()})
    
    def total_visits_at_park(self, park):
        return len([result for result in Trip.all if result.national_park == park])