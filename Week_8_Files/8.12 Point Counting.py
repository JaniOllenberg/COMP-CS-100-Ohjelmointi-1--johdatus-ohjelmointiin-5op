"""
COMP.CS.100 Programming 1
Count together all points of contestants.
Jani Ollenberg
H288244
"""
def main():
    scores_filename = input("Enter the name of the score file: ")
    scores_file = open(scores_filename, mode="r")
    scores_list = scores_file.readlines()
    
    # This works but lets see if i can do it with only dictionary.
    # list_names = []
    # for line in sorted(scores_list):
    #     name, score = line.split()
    #     if name not in list_names:
    #         list_names.append(name)
    # dict_scores = {}
    # for name in list_names:
    #     score_sum = 0
    #     for line in scores_list:
    #         name_all, score = line.split()
    #         if name == name_all:
    #             score_sum += int(score)
    #     dict_scores[name] = score_sum

    # Simpler version with only dictionary
    dict_scores = {}
    for line in sorted(scores_list):
        name, score = line.split()
        score = int(score)
        if name not in dict_scores:
            dict_scores[name] = score
        else:
            dict_scores[name] += score

    print("Contestant score:")
    for name in dict_scores:
        print(name, dict_scores[name])

if __name__ == "__main__":
    main()