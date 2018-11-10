while True:
    try:
        number = int(input("What's your fav number hoss?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number!")
    except ZeroDivisionError:
        print("Sorry hoss it can't be zero!")
    #except:
    #    print("LOL") This will catch all types of exception errors
    finally:
        print("Loop complete")