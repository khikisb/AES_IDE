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
    st.set_page_config(page_title="Enkripsi & Dekripsi AES-IDE", page_icon=":lock:")
    st.title("Enkripsi & Dekripsi AES-IDE")

    # Input Plaintext dan Kunci
    plaintext = st.text_input("Masukkan Plain Text : ")
    key = st.text_input("Masukkan kunci (16 karakter) : ")

    # Variabel ciphertext
    ciphertext = b""

    # Tombol Enkripsi
    if st.button("Enkripsi"):
        if len(key) == 16:
            # Proses enkripsi
            ciphertext = encrypt_AES_IDE(plaintext, key)
            st.write("Ciphertext: ", ciphertext)
        else:
            st.error("Kunci harus memiliki 16 karakter!")

    # Tombol Dekripsi
    if st.button("Dekripsi"):
        if len(key) == 16:
            # Proses dekripsi
            if ciphertext:
                decryptedtext = decrypt_AES_IDE(ciphertext, key)
                st.write("Plaintext hasil dekripsi: ", decryptedtext)
            else:
                st.error("Tidak ada ciphertext yang dienkripsi!")
        else:
            st.error("Kunci harus memiliki 16 karakter!")

if __name__ == "__main__":
    app()
