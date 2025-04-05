from blockchain import Blockchain

# Khởi tạo blockchain
my_blockchain = Blockchain()

# Nhập số lượng giao dịch cần thêm
num_transactions = int(input("Nhập số lượng giao dịch: "))

# Nhập từng giao dịch
for i in range(num_transactions):
    sender = input(f"Giao dịch {i+1} - Người gửi: ")
    receiver = input(f"Giao dịch {i+1} - Người nhận: ")
    amount = float(input(f"Giao dịch {i+1} - Số tiền: "))
    my_blockchain.add_transaction(sender, receiver, amount)

# Mining một block
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blockchain.add_transaction('Genesis', 'Miner', 1)
new_block = my_blockchain.create_block(new_proof, previous_hash)

# In toàn bộ blockchain
for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("----------------------------------")

# Kiểm tra tính hợp lệ
print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))
