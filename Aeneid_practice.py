raw_text = 'arma virumque cano Troiae qui primus ab oris\nItaliam fato profugus Laviniaque venit\nlitora multum ille et terris iactatus et alto'
line_list = raw_text.split('\n')

Aeneid_1 = {}

for line_number, text in enumerate(line_list):
  Aeneid_1[line_number+1] = text.split()

print Aeneid_1
print Aeneid_1[1][2][-1]