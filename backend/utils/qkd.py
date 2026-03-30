import random

def generate_bits(n):
    return [random.randint(0, 1) for _ in range(n)]

def generate_bases(n):
    return [random.choice(['Z', 'X']) for _ in range(n)]

def measure(bits, bases_sender, bases_receiver):
    measured = []
    for i in range(len(bits)):
        if bases_sender[i] == bases_receiver[i]:
            measured.append(bits[i])
        else:
            measured.append(random.randint(0, 1))
    return measured


# 🔐 FINAL QKD KEY GENERATOR (FIXED)
def generate_qkd_key(required_length):
    final_key = []

    while len(final_key) < required_length:
        n = required_length * 2  # generate extra bits for filtering

        bits = generate_bits(n)
        bases = generate_bases(n)
        bob_bases = generate_bases(n)

        measured = measure(bits, bases, bob_bases)

        # Basis matching (sifting)
        for i in range(n):
            if bases[i] == bob_bases[i]:
                final_key.append(measured[i])

            if len(final_key) >= required_length:
                break

    # Return EXACT required length
    return ''.join(map(str, final_key[:required_length]))