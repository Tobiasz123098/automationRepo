import json
import unittest

def zmien_strukture_jsona(dane)
    # Zmiana struktury JSON-a
    nowa_struktura = {
        osoba {
            imie dane[imie],
            nazwisko dane[nazwisko],
            wiek dane[wiek]
        }
    }
    return nowa_struktura

# Przykładowe dane w formacie JSON
dane_json = '{imie Natalia, nazwisko Kowalska, wiek 30}'

# Konwersja danych z JSON-a do słownika
dane = json.loads(dane_json)

# Zmiana struktury JSON-a
nowa_struktura_json = zmien_strukture_jsona(dane)

# Konwersja nowej struktury z powrotem do formatu JSON
nowa_struktura_json_json = json.dumps(nowa_struktura_json, indent=4)

# Wyświetlenie zmienionej struktury JSON-a
print(nowa_struktura_json_json)


class TestZmianyStrukturyJSON(unittest.TestCase)
    def test_zmiana_struktury_jsona(self)
        dane_testowe = {imie Natalia, nazwisko Kowalska, wiek 30}
        oczekiwana_struktura = {
            osoba {
                imie Natalia,
                nazwisko Kowalska,
                wiek 30
            }
        }
        self.assertEqual(zmien_strukture_jsona(dane_testowe), oczekiwana_struktura)


if __name__ == '__main__'
    unittest.main()