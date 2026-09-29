import hashlib
import datetime

class Block:
    def __init__(self, index, data, prev_hash=""):
        self.index = index
        self.timestamp = datetime.datetime.now().isoformat()
        self.timestamp_readable = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Menghitung SHA-256 hash dari gabungan isi blok termasuk nonce."""
        payload = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}{self.nonce}"
        return hashlib.sha256(payload.encode('utf-8')).hexdigest()

    def mine_block(self, difficulty):
        """Mekanisme Proof of Work: Mencari hash yang diawali dengan '0' sebanyak difficulty."""
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self):
        # Difficulty default set ke 3 (bisa diubah untuk pengujian difficulty)
        self.difficulty = 0
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block: Inisialisasi Rantai Pasok Farmasi", "0")
        genesis_block.mine_block(self.difficulty)
        return genesis_block

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        prev_block = self.get_latest_block()
        new_block = Block(len(self.chain), data, prev_block.hash)
        # Menambang (mining) blok baru sesuai difficulty
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """Mengecek integritas seluruh rantai blockchain."""
        target = "0" * self.difficulty

        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # 1. Cek apakah isi data di dalam blok diubah (hash tidak cocok)
            if current_block.hash != current_block.calculate_hash():
                return False

            # 2. Cek apakah pointer prev_hash merujuk ke hash blok sebelumnya yang benar
            if current_block.prev_hash != previous_block.hash:
                return False

            # 3. Cek apakah hash memenuhi kriteria PoW (difficulty)
            if current_block.hash[:self.difficulty] != target:
                return False

        return True