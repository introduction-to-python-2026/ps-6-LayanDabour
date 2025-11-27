def create_codon_dict(file_path):
  codon_to_ameno={}
  with open(file_path, "r") as file:
    rows = file.readlines()
  for row in rows[:]:
    cell = row.strip().split('\t')
    codon = cell[0]
    ameno = cell[2]
    codon_to_ameno[codon] = ameno
  return codon_to_ameno  


