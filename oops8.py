def  myfunc():

    try:

        for i in ['a','v','c']:
            print(i**2)
    except:
        print("An error occurred")
    finally:
        print("The try except is finished")

myfunc()    