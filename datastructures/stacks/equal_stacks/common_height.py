

class Cylinder(list):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = sum(self)

    def pop(self, *args, **kwargs):
        top = super().pop(*args, **kwargs)
        self.height -= top
        


class CossackOfCylinders(list):

    def __init__(self, cylinders_data):
        for cyl in cylinders_data:
            self.append(Cylinder(cyl))

    
    def heights_same(self):
        return all([ cyl.height == self[0].height 
                        for cyl in self ])


    def remove_top(self):
        highest_cylinder = max( self, key = lambda x: x.height )
        highest_cylinder.pop()


def highest_common(cylinders_data):

    cylinders = CossackOfCylinders(cylinders_data)

    while(not cylinders.heights_same()):
        cylinders.remove_top()

    return cylinders[0].height
        

