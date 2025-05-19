import sys, os
import csv
from rdkit import Chem
import tensorflow as tf
import pandas as pd
import numpy as np


root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)

from descriptors import fps_plus_others


infile = sys.argv[1]
outfile = sys.argv[2]

MODELPATH = os.path.join(root, "..", "..", "checkpoints", "2020_DNN_v44_epoch_78_r0.892_rms0.359.h5")
model = tf.keras.models.load_model(MODELPATH)

smiles = []
with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        smiles += [r[0]]


mols = []
idxs = []
for i, smi in enumerate(smiles):
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        continue
    mols += [mol]
    idxs += [i]

preds = []

for mol in mols:
    df = pd.DataFrame()
    df['Descriptors'] = fps_plus_others(mol)
    X_new = np.array(list(df['Descriptors']))
    X_new = X_new.reshape(1, -1)
    y_pred = model.predict(X_new, verbose=1)
    preds += [y_pred[0][0]]

y = [None]*len(smiles)
for i, p in zip(idxs, preds):
    y[i] = p


with open(outfile, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["cLogP".lower()])
    for r in y:
        writer.writerow([r])
