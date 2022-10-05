def parse_query(query):
    query = query.split("|")
    temp_query = []
    for element in query:
        temp_element = element.strip(" ").strip("\n").strip('\r')
        temp_element = temp_element.split(" ", 1)
        temp_query.append({"command": temp_element[0], "args": temp_element.split(" ")})
    return temp_query