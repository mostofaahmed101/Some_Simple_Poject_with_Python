a,b,c = float(input("a=? ")), float(input("b=? ")), float(input("c=? "))
if a+b>c and b+c>a and c+a>b:
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c)**0.5)
    print("Area of Triangle: ", area)

else:
    print("Triangle is not possible")