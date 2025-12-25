import hashlib
import time

print("START")

nickname = "leaf"

for difficulty in [4, 5]:
    print("DIFFICULTY =", difficulty)

    prefix = "0" * difficulty
    nonce = 0
    start_time = time.time()

    while True:
        text = nickname + str(nonce)
        hash_result = hashlib.sha256(text.encode()).hexdigest()

        if hash_result.startswith(prefix):
            end_time = time.time()
            print("TEXT:", text)
            print("HASH:", hash_result)
            print("TIME:", round(end_time - start_time, 4), "sec")
            break

        nonce += 1
