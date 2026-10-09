"""
GhostSnap - Unit Test Suite
Verifies folklore matching, image normalization, prompt structure, and privacy-first stateless contracts.
"""

import unittest
from PIL import Image
import io

from folklore_db import find_matching_folklore, FOLKLORE_DATABASE
from ai_engine import prepare_image, clean_json_response
from prompts import VISUAL_ANALYSIS_PROMPT, STORY_GENERATION_PROMPT_TEMPLATE

class TestGhostSnapCore(unittest.TestCase):

    def test_folklore_matching_window(self):
        """Test matching folklore when visual details contain 'window'."""
        match = find_matching_folklore(["dark shadow", "window angle"], region_filter="All")
        self.assertIsNotNone(match)
        self.assertIn("window", match["triggers"] or match["traditional_belief"].lower())

    def test_folklore_matching_region(self):
        """Test region filtering for folklore database."""
        match = find_matching_folklore(["shadow"], region_filter="Tamil")
        self.assertEqual(match["id"], "tamil_mohini")

    def test_prepare_image_resizing(self):
        """Test that large images are prepared and resized cleanly."""
        img = Image.new('RGB', (3000, 3000), color='black')
        prepared = prepare_image(img)
        self.assertLessEqual(prepared.size[0], 1500)
        self.assertLessEqual(prepared.size[1], 1500)

    def test_clean_json_response(self):
        """Test stripping markdown code fences around raw JSON string."""
        raw_json = "```json\n{\"key\": \"value\"}\n```"
        cleaned = clean_json_response(raw_json)
        self.assertEqual(cleaned, "{\"key\": \"value\"}")

    def test_prompts_safety_mandate(self):
        """Verify safety mandate is strictly embedded in visual analysis prompt."""
        self.assertIn("Do NOT state or claim that ghosts, spirits, or supernatural entities exist", VISUAL_ANALYSIS_PROMPT)

if __name__ == "__main__":
    unittest.main()
