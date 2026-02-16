pl = {
    'GOK': 90000,
    'GIN': 120000,
    'FRZ': 530000,
    'VEG': 40000,
    'REC': 90000
}

levpow = {
    j:i for i,j in pl.items()
 
}
repetido = {(i*2):j for i,j in pl.items()}
print (levpow)
kaioken = {i:(j*2) for i,j in pl.items()}
print('kaio-KEN', kaioken)