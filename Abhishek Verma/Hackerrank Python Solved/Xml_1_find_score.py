'''x=int(input())
abhi=[]
for i in range(x):
    k=[j for j in input().split(" ")]
    for new in k:
        if "='" in new:
            abhi.append(new)
    
    


print(len(abhi))'''
import sys
import xml.etree.ElementTree as etree
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    count = 0
    for element in node.iter():
        count += len(element.attrib)
    return count

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
