import unittest
import json
from app import poem_summary

class AgenticSummaryTest(unittest.TestCase):

    def setUp(self):
        self.app = poem_summary.test_client()
        self.app.testing = True

    def test_agentic_summary_valid_inputs(self):
        payload = {
            "poem" : "शिक्षण से दरिद्रता हटाई जा सकती है, ुस्तकों से अपेक्षा लगाई जा सकती है"
        }

        response = self.app.post('/agentic-summary',
                                 data=json.dumps(payload),
                                 content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)

        self.assertIn("language-detected", data)
        self.assertIn("summary-en", data)
        self.assertIn("summary-native", data)


    def test_agentic_summary_invalid_inputs(self):
        payload = {"poem": "   "}  # whitespace-only

        response = self.app.post('/agentic-summary',
                                 data=json.dumps(payload),
                                 content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("message", data)
        self.assertEqual(data["message"], "No poem")

if __name__ == '__main__':
    unittest.main()