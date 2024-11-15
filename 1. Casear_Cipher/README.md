# Caesar Cipher Encoder/Decoder

A simple command-line implementation of the Caesar Cipher encryption technique in Python. This program allows users to encode and decode messages using the classical Caesar shift cipher method.

## 🔍 Overview

The Caesar Cipher is one of the simplest and most widely known encryption techniques. It works by shifting each letter in the plaintext by a certain number of positions down the alphabet. This implementation includes both encoding and decoding capabilities with a custom ASCII art banner.

## 🚀 Features

- Encode and decode messages using Caesar Cipher algorithm
- Support for custom shift values
- Handles spaces and special characters
- Circular shifting (wraps around the alphabet)
- Interactive command-line interface
- Attractive ASCII art banner

## 📁 Files

- `caesar_cipher.py`: Main implementation of the Caesar Cipher algorithm
- `Art_cipher.py`: Contains ASCII art logo for the program

## 💻 Usage

1. Run the program:
   ```bash
   python caesar_cipher.py
   ```

2. Follow the prompts:
   - Choose 'encode' to encrypt or 'decode' to decrypt
   - Enter your message
   - Specify the shift number
   - Choose whether to continue with another message

## 📝 Example

```
Input:
- Direction: encode
- Message: hello
- Shift: 5

Output:
- The encode message is: mjqqt
```

## ⚙️ Technical Details

- The program uses a double alphabet list to handle wraparound without complex modulo operations
- Special characters and spaces are preserved in the output
- The shift value is automatically adjusted if it exceeds 26 (length of alphabet)
- Input is automatically converted to lowercase for processing

## 🤝 Contributing

Feel free to fork this repository and submit pull requests. You can also open issues for bugs or feature suggestions.

## 📜 License

This project is open source and available for educational purposes.