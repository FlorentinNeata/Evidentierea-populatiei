# Evidentierea-populatiei

### Scopul Proiectului

Acest proiect are drept scop crearea unei aplicații web care permite gestionarea și interogarea datelor stocate într-o bază de date MySQL. Proiectul utilizează un stack tehnologic compus din MySQL pentru stocarea datelor, Flask (un micro-framework Python) pentru logica de backend și HTML/CSS pentru interfața de utilizator.

### Componentele Proiectului

1. **Baza de Date MySQL**:
   - Proiectul utilizează MySQL pentru a stoca și gestiona datele structurate. Baza de date include mai multe tabele relaționate între ele, cum ar fi `Persoane`, `Institutii`, `Angajati` și `Casatorie`.
   - Datele inițiale sunt inserate în tabele, iar structura bazei de date facilitează realizarea de operațiuni complexe și interogări avansate.

2. **Interfața Web cu HTML și CSS**:
   - Pagina web este realizată folosind HTML pentru structura conținutului și CSS pentru stilizarea acestuia. Interfața este intuitivă și ușor de utilizat, oferind acces la funcționalitățile de gestionare a datelor.
   - Formularele HTML permit adăugarea, modificarea și ștergerea înregistrărilor din baza de date, iar tabelele HTML afișează datele într-un mod clar și organizat.

3. **Backend cu Flask și Python**:
   - Flask este utilizat pentru a crea un server web care gestionează cererile HTTP și comunică cu baza de date MySQL.
   - Python este utilizat pentru a implementa logica aplicației, inclusiv operațiunile CRUD (Create, Read, Update, Delete) și diverse interogări SQL.
   - Backend-ul gestionează interacțiunea dintre utilizator și baza de date, asigurând funcționalitatea aplicației web.

### Funcționalitățile Aplicației

#### Gestionarea Datelor

- **Adăugare Înregistrări**: Utilizatorii pot adăuga noi înregistrări în tabelele bazei de date, cum ar fi persoane, instituții, angajați și căsătorii, prin intermediul formularelor HTML.
- **Modificare Înregistrări**: Înregistrările existente pot fi actualizate printr-un formular de editare, care permite modificarea datelor pentru o persoană selectată.
- **Ștergere Înregistrări**: Utilizatorii pot șterge înregistrările din baza de date prin apăsarea unui buton de ștergere asociat fiecărei înregistrări.
- **Vizualizare Tabele**: Datele din baza de date sunt afișate într-un format tabular, permițând utilizatorilor să vadă informațiile într-un mod organizat și accesibil.

#### Interogări și Raportări

- **Interogări Personalizate**: Aplicația permite realizarea unor interogări avansate pentru a extrage informații specifice din baza de date. De exemplu, utilizatorii pot căuta persoane sub 30 de ani angajate în instituții private sau persoane între 30 și 50 de ani care sunt căsătorite și angajate.
- **Rapoarte Statistice**: Utilizatorii pot vizualiza rapoarte statistice, cum ar fi numărul de persoane din fiecare categorie sau numărul de angajați din diferite instituții.
- **Sortare și Filtrare**: Datele pot fi sortate după criterii cum ar fi numele sau vârsta, și pot fi filtrate pentru a găsi rapid informațiile necesare.

#### Caracteristici Specifice

- **Căutare și Filtrare**: Utilizatorii pot căuta persoane și informații specificate prin formulare de căutare și filtre, care permit găsirea rapidă a datelor relevante.
- **Afișare Date Avansate**: Aplicația oferă posibilitatea de a vizualiza date complexe, cum ar fi persoanele care nu sunt angajate și nu sunt căsătorite, împreună cu informații detaliate despre categoriile și instituțiile la care sunt afiliate.

### Beneficiile Aplicației

- **Soluție Completă și Integrată**: Integrarea perfectă între MySQL, Flask și HTML/CSS oferă o soluție robustă și scalabilă pentru gestionarea datelor.
- **Flexibilitate și Extensibilitate**: Structura modulară a aplicației permite adăugarea de noi funcționalități și adaptarea rapidă la cerințele utilizatorilor.
- **Ușurință în Utilizare**: Interfața web este ușor de utilizat, permițând gestionarea eficientă a datelor și realizarea de interogări complexe fără necesitatea de a avea cunoștințe avansate de programare.

### Tehnologii Utilizate

- **Python și Flask**: Utilizate pentru backend și gestionarea cererilor HTTP.
- **MySQL**: Pentru stocarea și gestionarea datelor.
- **HTML și CSS**: Pentru crearea și stilizarea interfeței de utilizator.
- **JavaScript**: Poate fi folosit pentru a adăuga funcționalități interactive pe partea de client.

