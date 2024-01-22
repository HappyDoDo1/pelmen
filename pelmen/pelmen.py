import codecs
with codecs.open(file_name, 'r', encoding='utf-8',
                 errors='ignore') as fdata:

qpa = float(input("¬ведите значение произв. одного пелменного автомата: "))
qt = float(input("¬ведите значение произв. дл€ теста: "))
qk = float(input("¬ведите значение произв. дл€ фарша: "))
Qc = float(input("¬ведите суточную производительность: "))
t = float(input("¬ведите врем€ смены: "))
at = float(input("¬ведите процент пельмений: "))

Qp = Qc * (2 * t)
npa = Qp/qpa
