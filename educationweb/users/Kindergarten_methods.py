class Kindergarten_methods():
    def __init__(self,kindergarten):
        self.kindergarten=kindergarten
    def create(self,teacher):
        self.kindergarten.myTeacher=teacher
        self.kindergarten.save()

    def Change_Kindergarten(self,kid):
        kid.garten=self.kindergarten
        kid.save()

        
    def add_kid(self,kid):
        kid.garten=self.kindergarten
        kid.save()

    def Kick_From_Kindergarten(self,kid):
        kid.garten.kid_set.remove(kid)

    
