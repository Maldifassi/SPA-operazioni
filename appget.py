from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Server web - codice per restituire la homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

# Server API per richiesta GET
@app.route('/calcola', methods=['GET'])
def calcola():
    # Prende i dati dalla query string della richiesta GET
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    operazione = request.args.get('operazione')

    # Verifica che tutti i parametri siano presenti
    if num1 is None or num2 is None or operazione is None:
        return jsonify(risultato='mancano i dati')

    # Esegue l'operazione selezionata
    if operazione == 'addizione':
        risultato = num1 + num2
    elif operazione == 'sottrazione':
        risultato = num1 - num2
    elif operazione == 'moltiplicazione':
        risultato = num1 * num2
    elif operazione == 'divisione':
        if num2 == 0:
            return jsonify(risultato='Errore: divisione per zero')
        risultato = num1 / num2
    else:
        return jsonify(risultato='operazione non valida')

    # Restituisce il risultato al front-end
    return jsonify(risultato=risultato)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)