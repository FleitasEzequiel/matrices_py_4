from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suma', methods=['POST','OPTIONS'])
def multiply():
    try:
        print("holas1")
        data = request.get_json()# Retrieve JSON data from the request
        print(data)
        return jsonify(data)
        print(data)
        matrix1 = data['matriz1']
        matrix2 = data['matriz2']
        # Validar que las matrices no estén vacías
        if not matrix1 or not matrix2:
            return jsonify({'error': 'Las matrices no pueden estar vacías'}), 400
        
        # Validar que todas las filas tengan el mismo número de columnas
        cols1 = len(matrix1[0])
        if any(len(row) != cols1 for row in matrix1):
            return jsonify({'error': 'Todas las filas de la Matriz 1 deben tener el mismo número de columnas'}), 400
        
        cols2 = len(matrix2[0])
        if any(len(row) != cols2 for row in matrix2):
            return jsonify({'error': 'Todas las filas de la Matriz 2 deben tener el mismo número de columnas'}), 400
        
        # Verificar que las dimensiones sean compatibles para multiplicación
        if cols1 != len(matrix2):
            return jsonify({
                'error': 'Las matrices no se pueden multiplicar. ' +
                         'El número de columnas de la Matriz 1 debe ser igual al número de filas de la Matriz 2.'
            }), 400
        
        # Inicializar matriz resultado
        result = []
        rows1 = len(matrix1)
        cols2 = len(matrix2[0])
        
        # Multiplicación de matrices
        for i in range(rows1):
            result_row = []
            for j in range(cols2):
                sum_val = 0
                for k in range(cols1):
                    sum_val += matrix1[i][k] * matrix2[k][j]
                result_row.append(sum_val)
            result.append(result_row)
        
        return jsonify({'result': result})
    
    except Exception as e:
        return jsonify({'error': f'Error al multiplicar matrices: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4500,debug=True)