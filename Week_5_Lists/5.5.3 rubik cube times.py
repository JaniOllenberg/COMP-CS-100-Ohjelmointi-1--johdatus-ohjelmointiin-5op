"""
COMP.CS.100 Programming 1
5.5.3 take 5 times and remove slowest and fastest and print average.
Jani Ollenberg
H288244
"""
def main():
    list_of_times = [1, 2, 3, 4, 5]
    for i in range(1, 6):
        list_of_times[i-1] = float(input(f"Enter the time for \
performance {i}: "))
    minimum_score = min(list_of_times)
    list_of_times.remove(minimum_score)
    maximum_score = max(list_of_times)
    list_of_times.remove(maximum_score)
    average = 0
    for i in list_of_times:
        average += i
    average = average / len(list_of_times)
    print(f"The official competition score is {average:.2f} seconds.")
if __name__ == "__main__":
    main()