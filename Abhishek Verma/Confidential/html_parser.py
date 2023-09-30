from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

# Read the number of lines in the HTML code snippet
n = int(input())

# Initialize the parser
parser = MyHTMLParser()

# Read and parse each line of HTML code
html_code = ""
for _ in range(n):
    line = input()
    html_code += line

parser.feed(html_code)
