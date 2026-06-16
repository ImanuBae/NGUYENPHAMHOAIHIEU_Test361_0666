import math


class TranspositionCipher:
    def encrypt(self, plain_text: str, key: int) -> str:
        self._validate_key(key)
        if not plain_text:
            return ""

        cipher_columns = []
        for column in range(key):
            current = column
            column_text = []
            while current < len(plain_text):
                column_text.append(plain_text[current])
                current += key
            cipher_columns.append("".join(column_text))

        return "".join(cipher_columns)

    def decrypt(self, cipher_text: str, key: int) -> str:
        self._validate_key(key)
        if not cipher_text:
            return ""

        total_chars = len(cipher_text)
        rows = math.ceil(total_chars / key)
        long_columns = total_chars % key

        if long_columns == 0:
            long_columns = key

        columns = []
        start = 0
        for column in range(key):
            column_length = rows if column < long_columns else rows - 1
            columns.append(cipher_text[start:start + column_length])
            start += column_length

        plain_text = []
        for row in range(rows):
            for column in range(key):
                if row < len(columns[column]):
                    plain_text.append(columns[column][row])
        return "".join(plain_text)

    def _validate_key(self, key: int) -> None:
        if key < 2:
            raise ValueError("Key phai la so nguyen lon hon hoac bang 2.")
