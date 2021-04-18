# lex_auth_01269442027919769669

# Global variables
child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]


def calculate_total_chocolates():
    total = 0
    for i in chocolates_received:
        total = total + i
    return total
    # Remove pass and write your logic here to find and return the total number of chocolates


def reward_child(child_id_rewarded, extra_chocolates):
    f=0
    if extra_chocolates < 1:
        print("Extra chocolates is less than 1")
        return 0

    for i in range(0, len(child_id)):
        if child_id_rewarded == child_id[i]:
            chocolates_received[i] = chocolates_received[i] + extra_chocolates
            f = 1
    if f == 0:
        print("Child id is invalid")
    else:
        print(chocolates_received)

    # Remove pass and write your logic here

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    # print("Child id is invalid")
    # print(chocolates_received)


print(calculate_total_chocolates())
# Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20, 2)