performance_data = {
    "Sales": {
        "Alice": [80, 85, 88, 90],
        "Bob": [70, 75, 78, 80],
        "Charlie": [60, 65, 70, 72]
    },
    "Engineering": {
        "David": [90, 92, 94, 95],
        "Eve": [85, 88, 87, 90],
        "Frank": [88, 87, 86, 85]
    },
    "HR": {
        "Grace": [70, 72, 74, 76],
        "Heidi": [65, 68, 70, 73],
        "Ivan": [60, 62, 64, 66]
    }
}

average_1 = {}
for depart, employ in performance_data.items() :
    average_1[depart] = {}
    for name, score in employ.items():
        average = sum(score) / len(score)
        average_1[depart][name] = average
        
print("Average Performance Scores: ", average_1)

top_2 = {}
for depart, employ in average_1.items():
    top_name = max(employ, key=employ.get)
    top_score = employ[top_name]
    top_2[depart] = (top_name, top_score)
    
print("Top Performers: ", top_2)

average_3 = {}
for depart, employ in average_1.items():
    sum_ = []
    for name, score in employ.items():
        sum_.append(score)
    average_ = sum(sum_) / len(sum_)
    average_3[depart] = average_
    
name_3 = max(average_3, key=average_3.get)
score_3 = average_3[name_3]
print("Best Department: ", name_3, score_3)

improvers_4 = {}
for depart, employ in performance_data.items():
    name_4 = []
    for name, score in employ.items():
        count = 0
        for i in range(len(score) - 1):
            if score[i] < score[i + 1]:
                count += 1
        if count == len(score) - 1:
            name_4.append(name)
    improvers_4[depart] = name_4

print("Continuous Improvers: ", improvers_4)

print()
print("Summary Report:")

for depart, employ in average_1.items():
    print("Department: ", depart)
    for name, ave_score in employ.items():
        print(f'  {name} Average Score = {ave_score}')
    print(f'Top performer: {top_2[depart][0]} with Average Score = {top_2[depart][1]}')