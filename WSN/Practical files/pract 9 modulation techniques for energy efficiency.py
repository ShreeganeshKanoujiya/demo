import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# FUNCTION DEFINITIONS FOR BER OF MODULATIONS

def ber_bpsk(EbN0):
    """BER of BPSK in AWGN"""
    return 0.5 * erfc(np.sqrt(EbN0))

def ber_qpsk(EbN0):
    """BER of QPSK (same as BPSK)"""
    return 0.5 * erfc(np.sqrt(EbN0))

def ber_ask(EbN0):
    """BER of 2-ASK"""
    return 0.5 * erfc(np.sqrt(EbN0 / 2))

def ber_fsk(EbN0):
    """BER of non-coherent BFSK"""
    return 0.5 * np.exp(-EbN0 / 2)

def ber_qam16(EbN0):
    """BER approx for 16-QAM"""
    return 0.75 * erfc(np.sqrt((3 / 15) * EbN0))


# SIMULATION PARAMETERS

EbN0_dB = np.arange(0, 15, 1)
EbN0 = 10 ** (EbN0_dB / 10)


# CALCULATE BER

ber_BPSK = ber_bpsk(EbN0)
ber_QPSK = ber_qpsk(EbN0)
ber_ASK = ber_ask(EbN0)
ber_FSK = ber_fsk(EbN0)
ber_16QAM = ber_qam16(EbN0)


# PLOT COMPARISON

plt.figure(figsize=(10, 6))

plt.semilogy(EbN0_dB, ber_BPSK, 'o-', label='BPSK')
plt.semilogy(EbN0_dB, ber_QPSK, 's-', label='QPSK')
plt.semilogy(EbN0_dB, ber_ASK, 'd-', label='ASK (2-ASK)')
plt.semilogy(EbN0_dB, ber_FSK, 'x-', label='FSK (Non-coherent)')
plt.semilogy(EbN0_dB, ber_16QAM, '^-', label='16-QAM')

plt.grid(True, which='both')
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("Comparison of Modulation Techniques for Energy Efficiency")
plt.legend()
plt.ylim(1e-6, 1)

plt.show()


# PRINT ENERGY EFFICIENCY SUMMARY

print("=== ENERGY EFFICIENCY (Lower Eb/N0 -> Better) ===")
print(f"BPSK BER @ 10 dB: {ber_BPSK[10]:.5f}")
print(f"QPSK BER @ 10 dB: {ber_QPSK[10]:.5f}")
print(f"ASK BER @ 10 dB: {ber_ASK[10]:.5f}")
print(f"FSK BER @ 10 dB: {ber_FSK[10]:.5f}")
print(f"16-QAM BER @ 10 dB: {ber_16QAM[10]:.5f}")