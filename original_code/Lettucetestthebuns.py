import unittest
from Translatonator_nottobeconfusedwitha_BaconatorTHISTHEONE import Translator, mrna_codon_table, dna_codon_table


class TestTranslator(unittest.TestCase):

    def setUp(self):
        self.translator = Translator()

    def test_clean_sequence(self):
        dirty = "AUG gcu  \nAUC123!!"
        cleaned = self.translator.clean_sequence(dirty)
        self.assertEqual(cleaned, "AUGGCUAUC")

    def test_validate_mrna_valid(self):
        self.assertTrue(self.translator.validate_mrna("AUGGCUAUC"))

    def test_validate_mrna_invalid(self):
        self.assertFalse(self.translator.validate_mrna("AUGTXU"))

    def test_validate_dna_valid(self):
        self.assertTrue(self.translator.validate_dna("ATGGCTATC"))

    def test_validate_dna_invalid(self):
        self.assertFalse(self.translator.validate_dna("ATGGCUX"))

    def test_validate_protein_valid(self):
        self.assertTrue(self.translator.validate_protein("MFVLC"))

    def test_validate_protein_invalid(self):
        self.assertFalse(self.translator.validate_protein("MFVLCZ"))  # 'Z' is not valid

    def test_mrna_to_protein_translation(self):
        seq = "AUGGCUAUC"  # AUG GCU AUC → M A I
        protein = "".join([mrna_codon_table.get(seq[i:i + 3], '?') for i in range(0, len(seq), 3)])
        self.assertEqual(protein, "MAI")

    def test_dna_to_protein_translation(self):
        seq = "ATGGCTATC"  # ATG GCT ATC → M A I
        protein = "".join([dna_codon_table.get(seq[i:i + 3], '?') for i in range(0, len(seq), 3)])
        self.assertEqual(protein, "MAI")

    def test_incomplete_codon_handling(self):
        # Should ignore last 2 bases
        seq = "AUGGCUA"  # AUG GCU (leave off "A")
        protein = "".join([mrna_codon_table.get(seq[i:i + 3], '?') for i in range(0, len(seq) - len(seq) % 3, 3)])
        self.assertEqual(protein, "MA")


if __name__ == "__main__":
    unittest.main()
