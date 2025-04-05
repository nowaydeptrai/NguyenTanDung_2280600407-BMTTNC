import base64

def main():
    try:
        # Mở tệp văn bản chứa chuỗi mã hóa base64
        with open("data.txt", "r", encoding="utf-8") as file:
            encoded_string = file.read().strip()

        # Giải mã base64
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode("utf-8")

        # In chuỗi sau khi giải mã
        print("Chuỗi sau khi giải mã:", decoded_string)

    except Exception as e:
        print("Lỗi:", e)

if __name__ == "__main__":
    main()
