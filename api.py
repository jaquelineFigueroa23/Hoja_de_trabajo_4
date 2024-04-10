from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/nombres', methods=['GET'])
def get_data():
    # Datos quemados
    data = {
        "Nombre": "Jaqueline Mariela Figueroa",
        "Carnet": "9490-21-4689"
    }
    data2 ={
        "Nombre": "Gerardo Antonio Ovado",
        "Carnet": "9490-21-7"
    }
    data3 ={
        "Nombre": "Nery Otoniel Colorado",
        "Carnet": "9490-22-4867"
    }
    data4 ={
        "Nombre": "Javier Pirir Gomez",
        "Carnet": "9490-22-15282"
    }
    return jsonify({"data": data, "data2": data2, "data3":data3, "data4":data4 })

if __name__ == '__main__':
    app.run(debug=True)
