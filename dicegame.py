from lib.utitilities import DiceThrower

def main():
    while True:
        thrower = DiceThrower()
        thrower.throw()
        com = sum(thrower.dice_list)
        thrower.throw()
        usr = sum(thrower.dice_list)
        
        if com == usr:
            print("Jafntefli!")
        elif com > usr:
            print("Ég vann!")
        else:
            print("Þú vannst!")
        
        ans = input("Viltu spila aftur? (Y/n)) ")
        if ans.lower() == "n":
            break

if __name__ == '__main__':
    main()