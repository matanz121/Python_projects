

def fun1():
    num_of_parts = None
    amount_of_parts = None
    totalSum = 0
    totalParts = 0
    while num_of_parts != 0:
        num_of_parts = int(input("Enter the number of Parts (0 to quit): "))
        if num_of_parts == 0:
            print(f"The total sum is {totalSum} NIS")
            print(f"The total parts replaced is {totalParts}")
            break
        else:
            amount_of_parts = int(input("Enter the Sum: "))
            discount_price = 0
            if num_of_parts == 1 and  amount_of_parts >= 3000:
                discount_price = amount_of_parts * 0.9
            elif num_of_parts == 2:
                discount_price = amount_of_parts * 0.85
            elif num_of_parts >= 3:
                discount_price = amount_of_parts * 0.78
            else:
                discount_price = amount_of_parts
            print(f"The amount the customers pays after the discount {discount_price} NIS\n")
            totalSum += discount_price
            totalParts += num_of_parts

def fun2(int_list, N):
    over_n_list = []
    n_count = 0
    for i in int_list:
        if i > N:
            over_n_list.append(i)
        elif i == N:
            n_count += 1

    print(f"Array members A over {N}: {over_n_list}")
    print(f"Number {N} appears {n_count} times")

if __name__ == '__main__':
    n_list = [10, 20, 100, 15, 90, 4, 6, 15]
    N = 15
    fun2(n_list, N)

