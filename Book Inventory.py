allBooks = {}
singleBooks = {}
bookQuantity = 0
allDates = {}
holdAllBooks = {}
singleDate = {}
monthDate = {}
yearDate = {}
infoSales = {}
numberOfSalesTakenPlace = {}
salesTakenPlaceDaily = {}
while True:
    print("Welcome to Ezy Book Store, select the following option to continue: \n1. Add a new shipment")
    print("2. Add a new sales \n3. Display revenue")
    print("4. Check inventory of books \n0. Exit program")
    option = input("Please enter your option: ")
    try:
        option = int(option)
        if option == 0:                   # stops everything
            break
        elif option == 1:
            isbn = input("Enter serial number of book:")
            while True:
                if isbn in allBooks:
                    quantity = input("Enter quantity of book to add or subtract:")  # is used to change quantity of books correctly if quantity added is wrong
                    try:
                        quantity = int(quantity)
                        print("Quantity is valid.")
                        books = allBooks[isbn]
                        books['quantity'] = quantity + books['quantity']
                        break
                        # invalid if quantity added is less than or equal to zero
                    except:
                        print("You have entered an invalid quantity.")
                        continue
                else:        # if isbn is new
                    try:
                        if isbn.isspace():  # check if input is empty
                            print("Serial number of book is invalid.")
                            continue
                        else:
                            singleBooks['ISBN'] = isbn
                            while True:
                                title = input("Enter title of book: ")
                                if title.isspace():
                                    print("Title of book is invalid.")
                                    continue
                                else:
                                    singleBooks['title'] = title
                                    break
                            while True:
                                author = input("Enter Author of book: ")
                                if author.isspace():
                                    print("Author name is invalid")
                                    continue
                                else:
                                    singleBooks['author'] = author
                                    break
                            while True:
                                price = input("Enter price of book:")
                                try:
                                    price = float(price)
                                    if price > 0:
                                        singleBooks['price'] = price
                                        break
                                    else:
                                        print("You have entered an invalid price.")
                                except:
                                    print("You have entered an invalid price.")
                            while True:
                                quantity = input("Enter quantity of book: ")
                                try:
                                    quantity = int(quantity)
                                    if quantity < 0:
                                        print("Quantity is invalid.")
                                        continue
                                    else:
                                        singleBooks['quantity'] = quantity
                                        break
                                except:
                                    print("Quantity is invalid.")
                            allBooks[isbn] = singleBooks
                            holdAllBooks = allBooks
                            singleBooks = {}
                            quantity = 0
                            break
                    except:
                        print("You have entered an invalid serial number.")

        elif option == 2:
            numberOfSalesTakenPlaceNumber = 0
            totalSellQuantity = 0
            totalSales = 0
            if allBooks == {}:
                print("There is no book for sale.")             # if no books in inventory
                continue
            else:
                while True:
                    singleDateInput = input("Enter date of sales (DD): ")        # options
                    monthDateInput = input("Enter month of sales(MM): ")
                    yearDateInput = input("Enter year of sales(YYYY): ")
                    if singleDateInput.isspace() and monthDateInput.isspace() and yearDateInput.isspace():
                        print("Please do not leave any dates blank.")
                        continue
                    elif singleDateInput.isalnum() and monthDateInput.isalnum() and yearDateInput.isalnum()\
                        and len(singleDateInput) == 2 and len(monthDateInput) == 2 and len(yearDateInput) == 4\
                            and int(monthDateInput) <= 12 and int(singleDateInput) > 0 and int(monthDateInput)> 0:
                        singleDateInput = int(singleDateInput)
                        monthDateInput = int(monthDateInput)
                        yearDateInput = int(yearDateInput)
                        while True:
                            isbn = input("Enter isbn of book: ")
                            infoSales['isbn'] = isbn
                            if isbn in allBooks:
                                sellQuantity = input("Enter quantity of books to sell: ")
                                try:
                                    sellQuantity = int(sellQuantity)
                                    books = allBooks[isbn]
                                    if books['quantity'] == 0:
                                        print("There is no more books titled", books['title'])
                                        break
                                    elif sellQuantity > books['quantity']:
                                        print("More books sold than existing ones.")
                                        continue
                                    elif sellQuantity == 0:
                                        print("Number of books sold is zero.")
                                        continue
                                    else:
                                        books = allBooks[isbn]
                                        print('Quantity is valid.')
                                        sales = sellQuantity * books['price']
                                        infoSales['dailySales'] = sales
                                        sales = int(sales)
                                        books['quantity'] = books['quantity'] - sellQuantity
                                        infoSales['Quantity sold'] = sellQuantity
                                        print("Sale of book is:${:.2f}".format(infoSales['dailySales']))
                                        infoSales['title'] = books['title']
                                        infoSales['price'] = books['price']
                                        salesTakenPlaceDaily[isbn] = infoSales
                                        singleDate[singleDateInput] = salesTakenPlaceDaily
                                        monthDate[monthDateInput] = singleDate
                                        yearDate[yearDateInput] = monthDate
                                        allDates['Read as YYYY/MM/DD,isbn,infoSales'] = yearDate
                                        if books['quantity'] == 0:
                                            print("There is no more books titled", books['title'])
                                        else:
                                            print("There are", books['quantity'], "books left.")
                                    # dateSingleBooks['date'] = date
                                except:
                                    print("Please enter a valid quantity.")
                            elif isbn.isspace():
                                print("Serial number of book is empty.")
                                continue
                            elif isbn in allBooks and yearDateInput in allDates and monthDateInput in allDates and singleDateInput in allDates:  # to update dailySales and quantity sold on same day
                                sellQuantity = input("Enter quantity of books to sell: ")
                                try:
                                    sellQuantity = int(sellQuantity)
                                    books = allBooks[isbn]
                                    totalDailySales = salesTakenPlaceDaily['dailySales']
                                    totalDailyQuantity = salesTakenPlaceDaily['Quantity sold']
                                    if books['quantity'] == 0:
                                        print("There is no more books titled", books['title'])
                                        break
                                    elif sellQuantity > books['quantity']:
                                        print("More books sold than existing ones.")
                                        continue
                                    elif sellQuantity == 0:
                                        print("Number of books sold is zero.")
                                        continue
                                    else:
                                        print('Quantity is valid.')
                                        sales = sellQuantity * books['price']
                                        sales = int(sales)
                                        totalDailySales['dailySales'] = totalDailySales['dailySales']+sales
                                        infoSales['dailySales'] = totalDailySales['dailySales']
                                        books['quantity'] = books['quantity'] - sellQuantity
                                        totalDailyQuantity['Quantity sold'] = totalDailyQuantity['Quantity sold']+sellQuantity
                                        infoSales['Quantity sold'] = totalDailyQuantity['Quantity sold']
                                        print("Sale of book is:${:.2f}".format(infoSales['dailySales']))
                                        if books['quantity'] == 0:
                                            print("There is no more books titled", books['title'])
                                        else:
                                            print("There are", books['quantity'], "books left.")
                                except:
                                    print("Please enter a valid quantity.")
                            else:
                                print("ISBN is not found.")
                                continue
                            break
                    else:
                        print("Please enter a correct date.")
                        continue
                    break
        elif option == 3:
            if yearDate != {}:
                chooseReport = input("Check monthly(MM) or daily sales(DD) or yearly(YYYY) report?")
                if chooseReport == 'DD':
                    checkYearDateInput = int(input("Enter year (YYYY):"))
                    if checkYearDateInput in allDates['Read as YYYY/MM/DD,isbn,infoSales']:
                        print("Year", checkYearDateInput, "exists.")
                        checkMonthDateInput = int(input("Enter month (MM):"))
                        if checkMonthDateInput in yearDate[checkYearDateInput]:
                            print("Month", checkMonthDateInput, "exists.")
                            checkDateInput = int(input("Enter date (DD):"))
                            if checkDateInput in monthDate[checkMonthDateInput]:
                                print("Date", checkDateInput, "exists.")
                                Sales = 0
                                totalSales = 0
                                for checkDateInput in singleDate:
                                    Sales = infoSales['dailySales']
                                    totalSales = totalSales + Sales
                                print("Total daily sales of",checkDateInput, "/", checkMonthDateInput, "/", checkYearDateInput,"is ${:.2f}".format(totalSales))
                            else:
                                print("Date does not exist.")
                                continue
                        else:
                            print("Month does not exist.")
                            continue
                    else:
                        print("Year does not exist.")
                        continue
                elif chooseReport == 'MM':
                    checkYearDateInput = int(input("Enter year (YYYY):"))
                    if checkYearDateInput in allDates['Read as YYYY/MM/DD,isbn,infoSales']:
                        print("Year", checkYearDateInput,"exists.")
                        checkMonthDateInput = int(input("Enter month (MM):"))
                        if checkMonthDateInput in yearDate[checkYearDateInput]:
                            print("Month", checkMonthDateInput, "exists.")
                            Sales = 0
                            totalSales = 0
                            for checkMonthDateInput in monthDate:
                                Sales = infoSales['dailySales']
                                totalSales = totalSales + Sales
                            print("Total monthly sales of", checkMonthDateInput, "/", checkYearDateInput, "is ${:.2f}".format(totalSales))
                        else:
                            print("Month does not exist.")
                    else:
                        print("Year does not exist.")
                elif chooseReport == 'YYYY':
                    checkYearDateInput = int(input("Enter year (YYYY):"))
                    if checkYearDateInput in allDates['Read as YYYY/MM/DD,isbn,infoSales']:
                        print("Year exists")
                        Sales = 0
                        totalSales = 0
                        for checkYearDateInput in yearDate:
                            Sales = infoSales['dailySales']
                            totalSales = totalSales + Sales
                        print("Total yearly sales of", checkYearDateInput, "is ${:.2f}".format(totalSales))
                    else:
                        print('No sales taken place during the year', checkYearDateInput, '.')
                else:
                    print('Please enter a correct choice.')
            else:
                print("There are no sales yet.")
        elif option == 4:
            if allBooks == {}:              # if no records at all
                print("No books yet")
            else:
                print("Checking all remaining books in inventory.")
                print(allBooks)
                print("Checking all sales of books.")
                print(allDates)
    except:
        print("Please enter a valid option.")          # loops back if entered wrong option
        continue
