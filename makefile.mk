# Instalacja zależności
deps:
    pip install -r requirements.txt

# Analiza statyczna kodu za pomocą lintera
lint:
    pylint *.py

# Uruchomienie aplikacji
run:
    python main.py

# Uruchomienie testów
test:
    python -m unittest