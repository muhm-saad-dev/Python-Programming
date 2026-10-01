def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

        
    except Exception as e:
        print(e) 
        return


    finally:
        print("Hey I am inside of finally") # The finally block will run weather it is return abuve it or not, means it runs breaking all ruls in python


main()