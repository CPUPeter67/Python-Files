import importlib.util
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).with_name("RandomProject.py")
spec = importlib.util.spec_from_file_location("RandomProject", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class GameHelpersTest(unittest.TestCase):
    def test_add_item_to_inventory_is_unique(self):
        inventory = []
        inventory = module.add_item_to_inventory(inventory, "glasses")
        inventory = module.add_item_to_inventory(inventory, "glasses")
        self.assertEqual(inventory, ["glasses"])

    def test_update_suspense_level_caps_at_boundaries(self):
        suspense = module.update_suspense_level(4, "raise")
        self.assertEqual(suspense, 5)

        suspense = module.update_suspense_level(0, "lower")
        self.assertEqual(suspense, 0)

    def test_should_welcome_back_only_for_matching_name(self):
        self.assertTrue(module.should_welcome_back("Chik", "Chik"))
        self.assertFalse(module.should_welcome_back("Mia", "Chik"))


if __name__ == "__main__":
    unittest.main()
