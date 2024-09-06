import numpy as np


def binomial(x, n, p):
    combinations = np.math.factorial(n) / np.math.factorial(x) * np.math.factorial(n-x)
    return combinations * np.power(p, x) * np.power(1-p, n-x) 

def encoder_indentity(msg):
    return msg

def noisy_channel(msg, p):
    noise_mask = (np.random.random(len(msg)) < p).astype(int)
    print("noise mask:".ljust(12), noise_mask)
    return np.bitwise_xor(msg, noise_mask)

def decoder_indentity(msg):
    return msg


msg = np.random.randint(0, 2, 2)
msg_enc = encoder_indentity(msg)
msg_noisy = noisy_channel(msg_enc, 0.1)
msg_dec = decoder_indentity(msg_noisy)

print("msg".ljust(12), msg)
print("msg_enc".ljust(12), msg_enc)
print("msg_noisy".ljust(12), msg_noisy)
print("msg_dec".ljust(12), msg_dec)
