# xorEncryptDecryptASC

Echipa noastra: Brabetzii

Echipa adversa: BitFlip

Cheia: arhsistcalc2021


Partea 1

Am folosit programul findkeywinput.py in care am aplicat xor intre primele 15 caractere din input cu cele din output pentru a obtine o posibila cheie de maxim 15 caractere.
Pentru a verifica daca cheia este cea corecta, rulam programul decrypt pentru cheile obtinute din primele 10-15 caractere pana cand una din ele transforma textul in cel initial.

Partea 2

Am folosit programul freq.py ce este bazat pe Frequency analysis(https://en.wikipedia.org/wiki/Frequency_analysis) pe chei de lungime 10-15.
Pentru fiecare gaseam caracterul care apare de cele mai multe ori pe pozitiile multiplu de k, unde k < lungimea cheii. Apoi am aplicat xor pentru fiecare din aceste caractere cu 32(codul ascii pentru spatiu), deoarece acesta apare cel mai des in texte.
Pentru a verifica daca cheia este cea corecta, rulam programul decrypt pentru cheile obtinute din primele 10-15 caractere pana cand una din ele transforma textul in cel initial.
