# ������� 7. ������� 10.
# ������������ ������� ���������� ����� ��� ������ 6, � ������������ �
# ������� ����� ������� �� ������� ���������� ������ �� ������� ����������
# �������.
# ������������ ������ ��������� 
# 24.06.2016

import random

guessesTaken = 0

print("������, ������� ���� �� ����� ������������� �����")
x = random.choice(["��������", "������-�������", "������"])

while guessesTaken < 10:
      print("� ��������: ")
      guess = input()

      guessesTaken = guessesTaken + 1
      
      if guess != x:
          print("�������.")
      if guess == x:
          break

if guess == x:
      print("�����! ����� �������:", guessesTaken)
      if guessesTaken == 1:
          print("������ ����������:", 100)
      if guessesTaken == 2:
          print("������ ����������:", 90)
      if guessesTaken == 3:
          print("������ ����������:", 80)
      if guessesTaken == 4:
          print("������ ����������:", 70)
      if guessesTaken == 5:
         print("������ ����������:", 60)
      if guessesTaken == 6:
          print("������ ����������:", 50)
      if guessesTaken == 7:
          print("������ ����������:", 40)
      if guessesTaken == 8:
          print("������ ����������:", 30)
      if guessesTaken == 9:
          print("������ ����������:", 20)
      if guessesTaken == 10:
          print("������ ����������:", 10)
if guess != x:
      print("������� ���������.")
      print("�� �� ������� ������.")

input("\n\n������� Enter ��� ������.")