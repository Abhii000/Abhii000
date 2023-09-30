def score_words(words):
    x=n
    y=words
    vowel=list('aeiouyYAEIOU')
    list1=[]
    list2=[]
    for a in range(x):

        for j in y[a]:
            if j in vowel:
                list1.append(j)
                #print(j)
        m=len(list1)
        #print(n)
        if m%2==0:

            list2.append(2)
        else:
            list2.append(1)
        list1=[]

    return sum(list2)


n = int(input())
words = input().split()
print(score_words(words))