exam_a = float(input("Enter the score for exam A: "))
exam_b = float(input("Enter the score for exam B: "))
exam_c = float(input("Enter the score for exam C: "))

average = (exam_a + exam_b + exam_c) / 3

print(f"Average Score: {average:.2f}")

if average >= 6:
    print("Student is approved! 🎉")
else:
    print("Student is not approved. 😔")
