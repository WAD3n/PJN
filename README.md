# PJN lab2

Nie działa od tygodnia ślęcze nad dokumentacją bibliotki spacy ponieważ otrzymmuję błąd :

 File "C:\Users\gluch\Documents\GitHub\PJN\main.py", line 55, in <module>
    lan = spacy.load('pl_core_news_lg')
  File "C:\Users\gluch\Documents\GitHub\PJN\venv\lib\site-packages\spacy\__init__.py", line 54, in load
    return util.load_model(
  File "C:\Users\gluch\Documents\GitHub\PJN\venv\lib\site-packages\spacy\util.py", line 439, in load_model
    raise IOError(Errors.E050.format(name=name))
OSError: [E050] Can't find model 'pl_core_news_lg'. It doesn't seem to be a Python package or a valid path to a data directory.

Język polski jest niekompatybilny z używaną przeze mnie biblioteką próbowałem na dwóch różnych urządzeniach z czego na głownym do pracy w ogóle niektórych bibliotek nie mogłem zainstalować jakiś windmil error otrzymałem stąd zmiana urządzenia.

Próbowałem pobrać starsze wersję języka polskiego oraz downgreadować bibliotekę spacy ale to nic nie dało.

Program przesyłam w formie, w której wydaje mi się że powinien działać ale niemożliwym jest jakiekolwiek zwizualizowanie / rozwiązanie niejodnoznaczności słow, ponieważ
nie mogę skompilować programu ....

Najmocniej przepraszam za opóźnienie w dostarczeniu pracy ale ilość wylanego potu i krwi / straconych nerwów przy tworzeniu tej abominacji(programu) powinna zadość uczynić. Jeszcze raz najmocniej przepraszam.
