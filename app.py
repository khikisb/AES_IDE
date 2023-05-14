import streamlit as st
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt_AES_IDE(plaintext, key):
    cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode("utf8"), AES.block_size)
    return cipher.encrypt(padded_plaintext)


def decrypt_AES_IDE(ciphertext, key):
    cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    return unpad(padded_plaintext, AES.block_size).decode("utf8")


def app():
    st.title("AES-IDE Encryption and Decryption")

    # Get user input
    plaintext = st.text_input("Masukkan Plain Text")
    key = st.text_input("Masukkan kunci harus 16 kata")

    if plaintext and key:
        # Proses enkripsi
        ciphertext = encrypt_AES_IDE(plaintext, key)
        st.write("Ciphertext: ", ciphertext)

        # Proses dekripsi
        st.write("Plaintext awal adalah : ", plaintext)
        decryptedtext = decrypt_AES_IDE(ciphertext, key)
        st.write("Plaintext hasil dekripsi: ", decryptedtext)


if __name__ == "__main__":
    app()
