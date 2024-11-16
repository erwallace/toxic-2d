import torch
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator


class MolToMorganFingerprints:
    def __init__(
        self,
        radius: int = 2,
        n_bits: int = 256,
        includeChirality: bool = True,
        use_counts: bool = True,
    ) -> None:
        self.radius = radius
        self.n_bits = n_bits
        self.includeChirality = includeChirality
        self.use_counts = use_counts

    def __call__(self, mol: Chem.Mol) -> torch.Tensor:
        generator = rdFingerprintGenerator.GetMorganGenerator(
            radius=self.radius, nBits=self.n_bits, includeChirality=self.includeChirality
        )
        if self.use_counts:
            fp = generator.GetCountFingerprintAsNumPy(mol)
        else:
            fp = generator.GetFingerprintAsNumPy(mol)
        return torch.Tensor(fp)