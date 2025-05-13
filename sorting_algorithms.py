pre_list = [4599, 3102, 1024, 9980, 2912, 1569, 4205, 9811, 1001, 7638, 4733, 1989, 5555, 5000, 3861]

def merge_sort(pre_list):
    if len(pre_list) > 1:
        mid = len(pre_list) // 2
        left_half = pre_list[:mid]
        right_half = pre_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                pre_list[k] = left_half[i]
                i += 1
            else:
                pre_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            pre_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            pre_list[k] = right_half[j]
            j += 1
            k += 1

    print("Sorting it out...")
    print(*pre_list, sep=", ")
    print("DONE!\n")
    main()

def insertion_sort(pre_list):
    for i in range(1, len(pre_list)):
        key = pre_list[i]
        j = i - 1
        while j >= 0 and key < pre_list[j]:
            pre_list[j + 1] = pre_list[j]
            j -= 1
        pre_list[j + 1] = key

    print("Sorting it out...")
    print(*pre_list, sep=", ")
    print("DONE!\n")
    main()

def selection_sort(pre_list):
    for i in range(len(pre_list)):
        smallest = i
        for j in range(i + 1, len(pre_list)):
            if pre_list[j] < pre_list[smallest]:
                smallest = j
        pre_list[i], pre_list[smallest] = pre_list[smallest], pre_list[i]

    print("Sorting it out...")
    print(*pre_list, sep=", ")
    print("DONE!\n")
    main()

def main():
    print("WELCOME TO OUR SHOP")
    print("-" * 19)
    print("Sort the items in the list\n")
    print("Choose an option")
    print("1 - Selection Sort")
    print("2 - Insertion Sort")
    print("3 - Merge Sort")
    print("4 - Exit Program\n")
    try:
        input_choice = int(input("Choice: "))
        if input_choice == 1:
            selection_sort(pre_list)
        elif input_choice == 2:
            insertion_sort(pre_list)
        elif input_choice == 3:
            merge_sort(pre_list)
        elif input_choice == 4:
            exit()
        else:
            print("Invalid choice. Please try again.")
            main()
    except ValueError:
        print("Invalid input. Please enter a number.")
        main()

main()