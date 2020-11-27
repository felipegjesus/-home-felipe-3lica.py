#valores das barras da treliça#
ab = float(input('Insira a barra AB: '))
bf = float(input('Insira a barra BF: '))
af = float(input('Insira a barra AF: '))
bc = float(input('Insira a barra BC: '))
fe = float(input('Insira a barra FE: '))
be = float(input('Insira a barra BE: '))
cd = float(input('Insira a barra CD: '))
ce = float(input('Insira a barra CE: '))
ed = float(input('Insira a barra ED: '))

#mostra as medidas#
print('AB:{} BF:{} AF:{}'.format(ab, bf, af))
print('BC:{} CE:{} FE:{} BF:{} BE:{}'.format(bc, ce, fe, bf, be))
print('CE:{} CD:{} ED:{}'.format(ce, cd, ed))

#pontos fixos#
print('O eixo está definido em A')

#inserir as forças#
f1 = float(input('Insira a Força 1: '))
f2 = float(input('Insira a Força 2: '))

#mostra as forças#
print('Força 1 vale:{} N'.format(f1))
print('Força 2 vale:{} N'.format(f2))

#calcular as reações Ay e Dy#
dy = (((af+fe)*f2)+(af*f1))/(af+fe+ed)
print('A reação Dy vale:{} N'.format(dy))
ay = (f1+f2-dy)
print('A reação Ay vale:{} N'.format(ay))

#secão da treliça#
#calculo das reações em abf#
#calcular as forças ef, eb, bc, af, ab#
print('Seccionando e calculando as reações no triâgulo ABF, temos:')
senbe = fe/be
cosbe = bf/be
fbe = ((ay-f1)/cosbe)
fef = ((ay*af)/bf)
fbc = ((fef)+(fbe*senbe))
fab = ((ab*ay)/bf)
faf = ((af*ay)/bf)

def imprime (forca, valor):
  print('A força '+ forca +' vale:{} N'.format(valor))


imprime('Fbe',fbe)
imprime('Fef',fef)
imprime('Fbc',fbc)
imprime('Fab',fab)
imprime('Faf',faf)

#print('A força Fef vale:{}N'.format(fef))
#print('A força Fbc vale:{}N'.format(fbc))
#print('A força Fab vale:{}N'.format(fab))
#print('A força Faf vale:{}N'.format(faf))
