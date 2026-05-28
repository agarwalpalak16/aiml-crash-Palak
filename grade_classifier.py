def classify(name,score):
    if score>=95:
        grade ="A"
    elif score>=90 and score<95:
        grade="B"
    elif score>=85 and score<90:
        grade ="C"

    elif score>=80and score<85:
        grade ="D"
    else:
        grade= "E"
    print(f"{name} scored {score} -> grade:{grade}")
students=[
    {"name":"palak","score":95},
    {"name":"riyanshi","score":90},
    {"name":"nidhi","score":85},
    {"name":"akshara","score":80},
    {"name":"shalini","score":75}
]
for s in students:
     classify(s["name"] , s["score"])