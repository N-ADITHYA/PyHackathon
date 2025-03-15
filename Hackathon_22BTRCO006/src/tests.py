import unittest
from src.voice_recognition import listen

class TestVoiceRecognition(unittest.TestCase):
    def test_listen_output(self):
        self.assertIsInstance(listen(), str)  # Check if the output is a string

if __name__ == "__main__":
    unittest.main()
