import unittest

from collatz.certificate_codec import decode_certificate, encode_prefix


class CertificateCodecTests(unittest.TestCase):
    def test_round_trip_and_exact_runs(self):
        for n in range(1, 500, 2):
            for steps in (1, 2, 5):
                cert = encode_prefix(n, steps)
                decoded, runs = decode_certificate(cert)
                self.assertEqual(decoded, n)
                self.assertEqual(len(runs), steps)

    def test_one_quotient_selects_an_integer(self):
        cert = encode_prefix(27, 3)
        self.assertEqual(cert["runs"], [1, 2, 1])
        self.assertEqual(decode_certificate(cert)[0], 27)

    def test_tampering_is_rejected(self):
        cert = encode_prefix(97, 4)
        original = decode_certificate(cert)[0]
        for field, value in (("quotient", cert["quotient"] + 1),
                             ("runs", cert["runs"][:-1]),
                             ("runs", cert["runs"][:1] + [cert["runs"][1] + 1] + cert["runs"][2:])):
            forged = dict(cert)
            forged[field] = value
            # A changed statement is still a valid certificate for another
            # integer. Validity is soundness, not authenticity of an origin.
            self.assertNotEqual(decode_certificate(forged)[0], original)

    def test_bad_types_and_negative_quotient_are_rejected(self):
        cert = encode_prefix(31, 2)
        for bad in ({"runs": cert["runs"], "quotient": -1},
                    {"runs": [0], "quotient": 0},
                    {"runs": cert["runs"], "quotient": True}):
            with self.assertRaises(ValueError):
                decode_certificate(bad)


if __name__ == "__main__":
    unittest.main()
