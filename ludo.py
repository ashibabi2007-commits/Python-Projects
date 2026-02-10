import random
p1=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
p2=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
p3=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
p4=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
p5=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
p6=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
p7=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
p8=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
print(f"Player 1 score: {p1}")
print(f"Player 2 score: {p2}")
print(f"Player 1 score: {p3}")
print(f"Player 2 score: {p4}")
print(f"Player 1 score: {p5}")
print(f"Player 2 score: {p6}")
print(f"Player 1 score: {p7}")
print(f"Player 2 score: {p8}")

if p1>p2 and p1>p3 and p1>p4 and p1>p5 and p1>p6 and p1>p7 and p1>p8:
    print("Player 1 Wins!")
elif p2>p1 and p2>p3 and p2>p4 and p2>p5 and p2>p6 and p2>p7 and p2>p8:
    print("Player 2 Wins!")
elif p3>p1 and p3>p2 and p3>p4 and p3>p5 and p3>p6 and p3>p7 and p3>p8:
    print("Player 2 Wins!")
elif p4>p1 and p4>p3 and p4>p2 and p4>p5 and p4>p6 and p4>p7 and p4>p8:
    print("Player 2 Wins!")
elif p5>p1 and p5>p3 and p5>p4 and p5>p2 and p5>p6 and p5>p7 and p5>p8:
    print("Player 2 Wins!")
elif p6>p1 and p6>p3 and p6>p4 and p6>p5 and p6>p2 and p6>p7 and p6>p8:
    print("Player 2 Wins!")
elif p7>p1 and p7>p3 and p7>p4 and p7>p5 and p7>p6 and p7>p2 and p7>p8:
    print("Player 2 Wins!")
else:
    print("It's a tie!")