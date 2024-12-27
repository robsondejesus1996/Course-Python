nome_completo = "Robson de Jesus"

nome_completo_aspas = """ Robson 
de 
Jesus"""

nome_completo_quebra = ("Robson \
                        de Jesus")


print('Nome completo ', nome_completo)
print('Nome completo ' + nome_completo)
print('Nome completo ' + "Robson" + "De Jesus")
print('Nome completo ' + "Robson", "de Jesus")
print('Nome completo ' , nome_completo_aspas)
print('Nome completo ', nome_completo_quebra)
print("Nome completo %s" % nome_completo)
print(f"Nome completo {nome_completo} ")
print("Nome completo: {}".format(nome_completo))
