import codecs
with codecs.open(file_name, 'r', encoding='utf-8',
                 errors='ignore') as fdata:

qpa = float(input("������� �������� ������. ������ ���������� ��������: "))
qt = float(input("������� �������� ������. ��� �����: "))
qk = float(input("������� �������� ������. ��� �����: "))
Qc = float(input("������� �������� ������������������: "))
t = float(input("������� ����� �����: "))
at = float(input("������� ������� ���������: "))

Qp = Qc * (2 * t)
npa = Qp/qpa
