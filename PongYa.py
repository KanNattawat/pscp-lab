""" pscp """

def main(num):
    """ main """
    if int(num) % 3 == 0 or num[-1] == "3":
        print("PONG")
    else:
        print(num)

main(input())
