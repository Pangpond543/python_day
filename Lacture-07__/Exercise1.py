survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"],
]

all_set = [set(lang) for lang in survey_results]

all_languages = set.intersection(*all_set)
print("Languages chosen by all participants: ", all_languages)

# dict_ = {}
# only = set()
# two = set()
# for l in range(len(survey_results)):
#     for l2 in range(len(survey_results[l])):
#         dict_[survey_results[l][l2]] = dict_.get(survey_results[l][l2], 0) + 1
# for l, v in dict_.items():
#     if v == 1 :
#         only.add(l)
#     elif v == 2:
#         two.add(l)

all_lang = set.union(*all_set)

only = {lang for lang in all_lang if sum(lang in s for s in all_set) == 1}

print("Languages only chosen by one participant: ", only)

number_of_lang = len(set.union(*all_set))
print("Number of unique languages: ", number_of_lang)

two = {lang for lang in all_lang if sum(lang in s for s in all_set) == 2}

print("Languages only chosen by one participant: ", two)

result = []

for i in range(len(all_set)):
    for j in range(i + 1, len(all_set)):
        if all_set[i] == all_set[j] :
            result.append([i + 1, j + 1])       
print("Participants with the same set of languages: ", result)
