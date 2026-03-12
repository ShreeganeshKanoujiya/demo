import numpy as np

# Hamming (7,4) Encoder
def encode(data):
    d1, d2, d3, d4 = data

    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4

    return np.array([p1, p2, d1, p3, d2, d3, d4])


# Hamming Decoder
def decode(code):
    p1, p2, d1, p3, d2, d3, d4 = code

    s1 = p1 ^ d1 ^ d2 ^ d4
    s2 = p2 ^ d1 ^ d3 ^ d4
    s3 = p3 ^ d2 ^ d3 ^ d4

    error_position = s1 + 2 * s2 + 4 * s3

    if error_position != 0:
        code[error_position - 1] ^= 1

    return np.array([d1, d2, d3, d4])


# Simulation
N = 1000
error_prob = 0.1

errors_without_fec = 0
errors_with_fec = 0

for _ in range(N):

    data = np.random.randint(0, 2, 4)

    # Without FEC
    noisy = data.copy()
    for i in range(4):
        if np.random.rand() < error_prob:
            noisy[i] ^= 1

    errors_without_fec += np.sum(data != noisy)

    # With FEC
    encoded = encode(data)
    noisy_code = encoded.copy()

    for i in range(7):
        if np.random.rand() < error_prob:
            noisy_code[i] ^= 1

    decoded = decode(noisy_code)
    errors_with_fec += np.sum(data != decoded)

print("Errors without FEC:", errors_without_fec)
print("Errors with FEC:", errors_with_fec)