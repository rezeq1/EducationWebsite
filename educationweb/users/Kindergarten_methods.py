class Kindergarten_methods():
    def __init__(self,kindergarten):
        self.kindergarten=kindergarten
    def create(self,teacher):
        self.kindergarten.myTeacher=teacher
        self.kindergarten.save()


        
    def add_kid(self,kid):
        kid.garten=self.kindergarten
        kid.save()
    
