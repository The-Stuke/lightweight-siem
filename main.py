import argparse

def main():
    parser = argparse(description='Easily query files with a fimiliar query like language')
    parser.add_arguement('query', metavar='q', help="The query")
    parser.add_arguement('query_type=', metavar="qt", help="The format the query is to be processed in. Either raw or with Base64")

if (__name__ == "__main__"):
    main()