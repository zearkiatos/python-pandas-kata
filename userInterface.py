def menu() -> None:
    option = ''
    while (option != 0):
        print("------ Select an Option ------\n")
        print("1) Series \n")
        print("2) Series with Date \n")
        print("3) Series with Dictionary\n")
        print("4) Serie operation \n")
        print("5) Serie modification \n")
        print("6) Increase Notes \n")
        print("7) DataFrames \n")
        print("8) DataFrames - Orders \n")
        print("9) Best Students \n")
        print("10) Dataframe fixer \n")
        print("11) Exchange \n")
        print("12) Depure Soccer Game \n")
        print("13) Agroups \n")
        print("14) Dataframe merge \n")
        print("15) Calculate universities capacities \n")
        print("16) Histograms \n")
        print("17) Bars \n")
        print("18) Boxplot \n")
        print("19) Custom boxplot \n")
        print("20) Dispersion Graph \n")
        print("21) Matrix dispersion \n")
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
        elif (option == 6):
            import seriesModification
        elif (option == 7):
            import dataFrames
        elif (option == 8):
            import dataFramesOrders
        elif (option == 9):
            import bestStudents
        elif (option == 10):
            import dataFrameFixer
        elif (option == 11):
            import exchange
        elif (option == 12):
            import depureSoccerGame
        elif (option == 13):
            import agroups
        elif (option == 14):
            import dataframeMerge
        elif (option == 15):
            import universityCapacity
        elif (option == 16):
            import historgram
        elif (option == 17):
            import bars
        elif (option == 18):
            import boxplots
        elif (option == 19):
            import customBoxplot
        elif (option == 20):
            import dispersionGraph
        elif (option == 21):
            import dispersionMatrix


menu()
