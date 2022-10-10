def table(queryResults, commandArgs):
    
    # Format for renaming
    try:
        if( "As" in commandArgs or "as" in commandArgs ):
            commandArgs = list(map(lambda x: x.replace('As', 'as'), commandArgs))
            try:
                while True:
                    get_as_index = commandArgs.index('as')
                    coupler = commandArgs[get_as_index-1] + commandArgs[get_as_index] + commandArgs[get_as_index+1]
                    commandArgs = commandArgs[:get_as_index-2] + ' ' +coupler + ' ' + commandArgs[get_as_index+2:]
            except:
                exit
    except:
        print("Issue with 'as' keyword")
        quit()
    
    # Start to parse data
    try:
        # Setup placeholder variables
        newQueryResults, tableHeaders, headerIndexes = [], [], []
        
        # Go through command args to pull common names
        for element in commandArgs:
            if(' ' in element):
                tableHeaders.append(element.split(' ')[0])
            else:
                tableHeaders.append(element)
        
        # Find indexes of headers to parse rows of results
        for header in tableHeaders:
            try:
                headerIndexes.append(queryResults[0].index(header))
            except:
                print("Error: No column/field named: " + str(header))
                quit()


        for i in range(len(queryResults)-1):
            tempRow = []
            for index in headerIndexes:
                tempRow.append(queryResults[i+1][index])
            
        return tempRow
    except:
        print("Tabling error")

