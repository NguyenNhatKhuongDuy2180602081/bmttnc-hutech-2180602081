from flask import Flask, request, jsonify
from caesar.caesar_cipher import CaesarCipher
from vigenere import VigenereCipher
app = Flask(__name__)

#CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()


@app.route("/api/caesar/encrypt", methods = ["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encypted_text})

@app.route("/api/caesar/decrypt", methods = ["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decypted_text})

#VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods = ['POST'])
def vigenere_encrypted():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods = ['POST'])
def vigenere_decrypted():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)