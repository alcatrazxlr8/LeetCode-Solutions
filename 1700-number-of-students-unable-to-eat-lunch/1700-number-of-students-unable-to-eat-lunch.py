class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle_count = 0
        square_count = 0
        
        for student in students:
            if student == 0:
                circle_count += 1
            else:
                square_count += 1
                
        for sandwich in sandwiches:
            if sandwich == 0 and circle_count == 0:
                return square_count
            
            if sandwich == 1 and square_count == 0:
                return circle_count
            
            if sandwich == 0:
                circle_count -= 1
            else:
                square_count -= 1
                
        return 0