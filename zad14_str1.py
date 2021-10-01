"""
Dat je cetvorocifreni prirodan broj. Ako su mu cifra jedinica i cifra hiljada jednake,
štampati kvadrat dvocifrenog broja koji se dobije kada se uklone cifra jedinica i cifra
hiljada. Ako te dvije cifre nisu jednake, štampati zbir kvadrata svih cifara.
"""

def cetvorocifreni_broj(abcd):
    jedinica = abcd % 10
    desetica = (abcd // 10) % 10
    stotina = (abcd // 100) % 10
    hiljada = abcd // 1000
    if jedinica == hiljada:
        bc = desetica + stotina * 10
        return bc ** 2
    else:
        return jedinica ** 2 + desetica ** 2 + stotina ** 2 + hiljada ** 2

x = int(input('Unesite cetvorocifren broj: '))
print('Rezultat je: ', cetvorocifreni_broj(x))