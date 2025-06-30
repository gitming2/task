from task1 import Student

## 문제 2: 성적 계산 기능 추가
class GradedStudent(Student):
    def __init__(self, name, age, grade):
        super().__init__(name, age, grade)
        self.scores = []
    
    def add_score(self, score):
        self.scores.append(score)
    
    def calculate_average(self):
        # scores 리스트의 평균을 계산하여 반환하는 메서드를 작성하세요.
        # YOUR CODE HERE
        sum_score = 0
        for i in range(len(self.scores)):
            sum_score += self.scores[i]
            average = sum_score / len(self.scores)
        print(f"당신의 평균은 {average}입니다.")

    def study(self, hours):
        super().study(hours)
        # 공부한 시간에 비례하여 임의의 점수를 생성하고 add_score 메서드를 호출하세요. 
        # 기본점수 : 60점, 최대 추가 점수 : 40점 
        # 최대 공부시간 8시간으로 시간에 비례해서 점수 추가
        # YOUR CODE HERE
        if hours < 8:
            random_score = 60 + hours * 5
            self.add_score(random_score)
        else:
            random_score = 100
            self.add_score(random_score)

# GradedStudent 클래스의 객체를 생성하고, 여러 번 study 메서드를 호출한 후 평균 점수를 계산해보세요.
# YOUR CODE HERE
def main():
    grst = GradedStudent("홍박사", 15, 2)

    for i in range(5):
        h = int(input("시간을 입력하세요:"))
        sum = grst.study(h)
        print(grst.scores[i])
    grst.calculate_average()


if __name__ == "__main__":
    main()