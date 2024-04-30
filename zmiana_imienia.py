def zmien_imie(imie):
    imie_zmienione = imie.replace("Natalia", "Tobiasz")
    return imie_zmienione

def test_zmien_imie():
    imie_test = "Natalia"
    imie_zmienione = zmien_imie(imie_test)
    assert imie_zmienione == "Tobiasz", "Błąd: Niepoprawna zmiana imienia"

test_zmien_imie()