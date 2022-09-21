def menu ()->None:
    option = ''
    while (option != 0):
        print("------ Select an Option ------\n")
        print("1) Series \n")
        print("2) Series with Date \n")
        print("3) Series with Dictionary\n")
        print("4) Serie operation \n")
        print("5) Serie modification \n")
        print("0) Exit \n")

        option = int(input('Select an option please: '))

        if (option == 1):
            import series
        elif (option == 2):
            import serieWithDate
        elif (option == 3):
            import seriesWithDictionary
        elif (option == 4):
            import serieOperation
        elif (option == 5):
            import seriesModification


menu()