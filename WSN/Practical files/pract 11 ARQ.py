import random

frames = 20
loss_prob = 0.2

print("=== STOP AND WAIT ARQ ===")

sent = 0
retrans = 0

for f in range(1, frames + 1):
    success = False
    while not success:
        sent += 1
        if random.random() < loss_prob:
            retrans += 1
        else:
            success = True

efficiency_sw = frames / sent

print("Total Frames Sent:", sent)
print("Retransmissions:", retrans)
print("Efficiency:", efficiency_sw)


print("\n=== GO BACK N ARQ ===")

window = 4
sent = 0
retrans = 0
i = 1

while i <= frames:
    for w in range(window):
        if i + w > frames:
            break

        sent += 1

        if random.random() < loss_prob:
            retrans += window
            sent += window
            break

    i += window

efficiency_gbn = frames / sent

print("Total Frames Sent:", sent)
print("Retransmissions:", retrans)
print("Efficiency:", efficiency_gbn)


print("\n=== SELECTIVE REPEAT ARQ ===")

sent = 0
retrans = 0

for f in range(1, frames + 1):
    sent += 1
    if random.random() < loss_prob:
        retrans += 1
        sent += 1

efficiency_sr = frames / sent

print("Total Frames Sent:", sent)
print("Retransmissions:", retrans)
print("Efficiency:", efficiency_sr)