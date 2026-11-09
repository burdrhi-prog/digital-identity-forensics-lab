import unittest
from case_study_report import evaluate,report
class FictionalCaseStudyTests(unittest.TestCase):
    def test_counts(self):
        events,pairs=evaluate()
        self.assertEqual(len(events),4)
        self.assertEqual(len(pairs),3)
    def test_excludes_other_account(self):
        _,pairs=evaluate()
        self.assertFalse(any('F-004' in pair[:2] for pair in pairs))
    def test_gaps(self):
        _,pairs=evaluate()
        self.assertEqual(sorted(p[2] for p in pairs),[4,5,9])
    def test_report_has_source_pointers(self):
        r=report()
        self.assertIn('ART-001:row-2',r)
        self.assertIn('Unresolved',r)
if __name__=='__main__':
    unittest.main()
