import string
import math

liczba_figur=int(input())
liczby=[]
wyniki=0

for index in range (0,liczba_figur):
  liczba=input().split()
  
  for liczba_figur in range (0,len(liczba)):
    liczba[liczba_figur]=float(liczba[liczba_figur])
  liczby.append(liczba)

for promien_bok in liczby:
  if len(promien_bok)==1:
    pi=math.pi
    wynik=pi*(promien_bok[0])**2
    wyniki+=wynik

  if len(promien_bok)==2:
    wynik=promien_bok[0]*promien_bok[1]
    wyniki+=wynik

  if len(promien_bok)==3:
    a=promien_bok[0]
    b=promien_bok[1]
    c=promien_bok[2]
    p=1/2*(a+b+c)
    pole=(p*(p-a)*(p-b)*(p-c))**(1/2)
    wyniki+=pole

  if len(promien_bok)>3:
    print("Błąd: można podać maksymalnie 3 liczby")
    break
   
print(round(wyniki,2))