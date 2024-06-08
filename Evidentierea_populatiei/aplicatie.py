from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__)


DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'qwertyuiop',
    'database': 'test'
}

def get_db_connection():
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    return conn

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/persoane', methods=['GET', 'POST'])
def persoane():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        id_persoana = request.form['id_persoana']
        nume = request.form['nume']
        prenume = request.form['prenume']
        varsta = request.form['varsta']
        categorie = request.form['categorie']
        institutie = request.form['institutie'] or None
        cursor.execute(
            'INSERT INTO Persoane (ID_Persoana, Nume, Prenume, Varsta, ID_Categorie, ID_Institutie) VALUES (%s, %s, %s, %s, %s, %s)', 
            (id_persoana, nume, prenume, varsta, categorie, institutie))
        conn.commit()
        return redirect(url_for('persoane'))
    cursor.execute('SELECT * FROM Persoane')
    persoane = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('persoane.html', persoane=persoane)


@app.route('/persoane/edit/<int:id>', methods=['GET', 'POST'])
def edit_persoana(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        nume = request.form['nume']
        prenume = request.form['prenume']
        varsta = request.form['varsta']
        categorie = request.form['categorie']
        institutie = request.form['institutie'] or None
        cursor.execute(
            'UPDATE Persoane SET Nume = %s, Prenume = %s, Varsta = %s, ID_Categorie = %s, ID_Institutie = %s WHERE ID_Persoana = %s',
            (nume, prenume, varsta, categorie, institutie, id))
        conn.commit()
        return redirect(url_for('persoane'))
    cursor.execute('SELECT * FROM Persoane WHERE ID_Persoana = %s', (id,))
    persoana = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('edit_persoana.html', persoana=persoana)


@app.route('/persoane/delete/<int:id>', methods=['POST'])
def delete_persoana(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Persoane WHERE ID_Persoana = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('persoane'))

@app.route('/casatorii')
def casatorii():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Casatorie')
    casatorii = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('casatorii.html', casatorii=casatorii)

@app.route('/angajati')
def angajati():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Angajati')
    angajati = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('angajati.html', angajati=angajati)

@app.route('/institutii')
def institutii():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Institutii')
    institutii = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('institutii.html', institutii=institutii)

@app.route('/adolescenti')
def adolescenti():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT ID_Persoana,Nume,Prenume,Varsta FROM Persoane WHERE ID_Categorie = 1')
    adolescenti = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('adolescenti.html', adolescenti=adolescenti)

@app.route('/adulti')
def adulti():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT ID_Persoana,Nume,Prenume,Varsta FROM Persoane WHERE ID_Categorie = 2')
    adulti = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('adulti.html', adulti=adulti)

@app.route('/batrani')
def batrani():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT ID_Persoana,Nume,Prenume,Varsta FROM Persoane WHERE ID_Categorie = 3')
    batrani = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('batrani.html', batrani=batrani)


#INTEROGARI



@app.route('/interogari/<string:query_type>')
def interogari(query_type):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    data = None

#1
    if query_type == 'persoane_sub_30_privat':
        cursor.execute("""
         SELECT 
            P.Nume,
            P.Prenume,
            P.Varsta,
            I.Nume_Institutie
        FROM 
            Persoane P
        INNER JOIN 
            Institutii I ON P.ID_Institutie = I.ID_Institutie
        WHERE 
            P.Varsta < 30
            AND I.Tip = 'Privat'
        """)
        data = cursor.fetchall()
#2
    elif query_type == 'persoane_30_50_angajate_casatorite':
        cursor.execute("""
        SELECT 
            P.Nume,
            P.Prenume,
            P.Varsta
        FROM 
            Persoane P
        INNER JOIN 
            Angajati A ON P.ID_Persoana = A.ID_Persoana
        INNER JOIN 
            Casatorie C ON P.ID_Persoana = C.ID_Sot OR P.ID_Persoana = C.ID_Sotie
        WHERE 
            P.Varsta BETWEEN 30 AND 50;
        """)
        data = cursor.fetchall()
#3
    elif query_type == 'persoane_neangajate_necasatorite':
        cursor.execute("""
       SELECT
    P.ID_Persoana,
    P.Nume,
    P.Prenume,
    P.Varsta,
    C.Descriere AS Categorie,
    I.Nume_Institutie,
    I.Adresa AS Adresa_Institutie,
    I.Tip AS Tip_Institutie,
    A.Data_Angajare,
    A.Salariu,
    CASE
        WHEN P.ID_Persoana = S.ID_Sot THEN 'Sot'
        WHEN P.ID_Persoana = S.ID_Sotie THEN 'Sotie'
        ELSE 'Necasatorit'
    END AS Rol_In_Casatorie,
    S.Data_Casatorie
FROM 
    Persoane P
LEFT JOIN 
    Categorii C ON P.ID_Categorie = C.ID_Categorie
LEFT JOIN 
    Angajati A ON P.ID_Persoana = A.ID_Persoana
LEFT JOIN 
    Institutii I ON A.ID_Institutie = I.ID_Institutie
LEFT JOIN 
    Casatorie S ON P.ID_Persoana = S.ID_Sot OR P.ID_Persoana = S.ID_Sotie;

        """)
        data = cursor.fetchall()
#4
    elif query_type == 'persoane_peste_medie':
        cursor.execute("""
        SELECT 
    P.Nume,
    P.Prenume,
    P.Varsta
FROM 
    Persoane P
WHERE 
    P.Varsta > (SELECT AVG(Varsta) FROM Persoane);

        """)
        data = cursor.fetchall()
#5
    elif query_type == 'persoane_casatorite_institutii':
        cursor.execute("""
        SELECT 
            P.Nume,
            P.Prenume,
            I.Nume_Institutie AS Nume_Institutie
        FROM 
            Persoane P
        INNER JOIN 
            Casatorie C ON P.ID_Persoana = C.ID_Sot OR P.ID_Persoana = C.ID_Sotie
        LEFT JOIN 
            Angajati A ON P.ID_Persoana = A.ID_Persoana
        LEFT JOIN 
            Institutii I ON A.ID_Institutie = I.ID_Institutie;
        """)
        data = cursor.fetchall()
#6
    elif query_type == 'numar_persoane_categorie':
        cursor.execute("""
        SELECT 
            C.Descriere AS Categorie,
            COUNT(P.ID_Persoana) AS Numar_Persoane
        FROM 
            Categorii C
        LEFT JOIN 
            Persoane P ON C.ID_Categorie = P.ID_Categorie
        GROUP BY 
            C.Descriere;
        """)
        data = cursor.fetchall()
#7
    elif query_type == 'numar_angajati_per_institutie':
        cursor.execute("""
        SELECT 
            I.Nume_Institutie AS Nume_Institutie,
            COUNT(A.ID_Angajat) AS Numar_Angajati
        FROM 
            Institutii I
        LEFT JOIN 
            Angajati A ON I.ID_Institutie = A.ID_Institutie
        GROUP BY 
            I.ID_Institutie;
        """)
        data = cursor.fetchall()
#8
    elif query_type == 'numar_angajati_edu':
        cursor.execute("""
        SELECT 
            I.Nume_Institutie AS Nume_Institutie,
            COUNT(A.ID_Angajat) AS Numar_Angajati
        FROM 
            Institutii I
        LEFT JOIN 
            Angajati A ON I.ID_Institutie = A.ID_Institutie
        WHERE 
            I.Tip = 'Educatie'
        GROUP BY 
            I.ID_Institutie;
        """)
        data = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('interogari.html', query_type=query_type, data=data)


def get_persoane_sorted(sort_by='varsta'):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True) 
    if sort_by == 'nume':
        cursor.execute("SELECT * FROM Persoane ORDER BY Nume ASC")
    else:
        cursor.execute("SELECT * FROM Persoane ORDER BY Varsta ASC")
    persoane = cursor.fetchall()
    conn.close()
    return persoane

@app.route('/lista')
def lista_persoane():
    sort_by = request.args.get('sort_by', 'varsta')
    persoane = get_persoane_sorted(sort_by)
    return render_template('persoane.html', persoane=persoane, sort_by=sort_by)

@app.route('/nume_lung')
def get_cel_mai_lung_nume():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Nume FROM Persoane ORDER BY LENGTH(Nume) DESC LIMIT 1")
    persoana = cursor.fetchone()
    conn.close()
    return jsonify({'nume': persoana['Nume'] if persoana else None})



if __name__ == '__main__':
    app.run(debug=True)
