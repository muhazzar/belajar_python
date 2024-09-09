dud={
    "sm":"samsu",
    "gt":"garpit",
    "kl":"kolak"
}

roko=dud.copy()

print(f"dud: {dud}")
print(f"roko: {roko}\n")

dud["gt"]="signatuer"

print(f"dud: {dud}")
print(f"roko: {roko}\n")

#pop dict
poop=dud.pop("gt")
print(poop)
print(dud)



poitem=dud.popitem()
print(f"\ndata terakhir: {poitem}")
print(dud)