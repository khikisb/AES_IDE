import streamlit as st
from Cryptodome.Cipher import IDEA
from Cryptodome.Util.Padding import pad, unpad

def encrypt_AES_IDE(plaintext, key):
    cipher = IDEA.new(key.encode("utf8"))
    padded_plaintext = pad(plaintext.encode("utf8"), IDEA.block_size)
    return cipher.encrypt(padded_plaintext)

def decrypt_AES_IDE(ciphertext, key):
    cipher = IDEA.new(key.encode("utf8"))
    padded_plaintext = cipher.decrypt(ciphertext)
    return unpad(padded_plaintext, IDEA.block_size).decode("utf8")

def app():
    st.set_page_config(page_title="Enkripsi & Dekripsi AES-IDE", page_icon=":lock:")
    st.title("Kelompok 1")
    st.title("(Enkripsi & Dekripsi AES-IDE)")

    st.title("Enkripsi Plaintext AES Metode IDEA")
    # Input Plaintext dan Kunci untuk Enkripsi
    plaintext_enkripsi = st.text_input("Masukkan Plain Text untuk Enkripsi: ")
    key_enkripsi = st.text_input("Masukkan kunci untuk Enkripsi (16 karakter): ")
    # Tombol Enkripsi
    if st.button("Enkripsi"):
        if len(key_enkripsi) == 16:
            # Proses enkripsi
            ciphertext = encrypt_AES_IDE(plaintext_enkripsi, key_enkripsi)
            st.write("Ciphertext: ", ciphertext.hex())
        else:
            st.error("Kunci harus memiliki 16 karakter!")
            
    st.title("Deskripsi Chippertext AES Metode IDEA")    
            
    # Input Ciphertext dan Kunci untuk Dekripsi
    ciphertext_deskripsi = st.text_input("Masukkan Ciphertext untuk Deskripsi: ")
    key_deskripsi = st.text_input("Masukkan kunci untuk Deskripsi (16 karakter): ")


    # Tombol Dekripsi
    if st.button("Dekripsi"):
        if len(key_deskripsi) == 16:
            if ciphertext_deskripsi:
                # Proses dekripsi
                ciphertext_bytes = bytes.fromhex(ciphertext_deskripsi)
                decryptedtext = decrypt_AES_IDE(ciphertext_bytes, key_deskripsi)
                st.write("Plaintext hasil dekripsi: ", decryptedtext)
            else:
                st.error("Tidak ada ciphertext yang dienkripsi!")
        else:
            st.error("Kunci harus memiliki 16 karakter!")

if __name__ == "__main__":
    app()
