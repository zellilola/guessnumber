"""
Test suite for Josephus Problem implementations.
"""

import unittest
from josephus_problem import (
    josephus_recursive,
    josephus_iterative,
    josephus_queue,
    josephus_mathematical,
    josephus_simulation
)


class TestJosephusProblem(unittest.TestCase):
    """Test cases for all Josephus problem implementations."""
    
    def setUp(self):
        """Set up test cases with known solutions."""
        # Test cases: (n, k, expected_result)
        self.test_cases = [
            (1, 1, 1),    # Edge case: single person
            (1, 5, 1),    # Edge case: single person with large k
            (2, 1, 2),    # Two people, eliminate every person
            (2, 2, 1),    # Two people, eliminate every 2nd person
            (3, 2, 3),    # Classic small case
            (5, 2, 3),    # Five people, every 2nd eliminated
            (7, 3, 4),    # Seven people, every 3rd eliminated
            (10, 3, 4),   # Ten people, every 3rd eliminated
            (41, 3, 31),  # Historical Josephus problem (41 soldiers, every 3rd)
            (100, 7, 50), # Larger test case
        ]
    
    def test_recursive_solution(self):
        """Test the recursive implementation."""
        for n, k, expected in self.test_cases:
            with self.subTest(n=n, k=k):
                result = josephus_recursive(n, k)
                self.assertEqual(result, expected,
                               f"Recursive: n={n}, k={k}, got {result}, expected {expected}")
    
    def test_iterative_solution(self):
        """Test the iterative implementation."""
        for n, k, expected in self.test_cases:
            with self.subTest(n=n, k=k):
                result = josephus_iterative(n, k)
                self.assertEqual(result, expected,
                               f"Iterative: n={n}, k={k}, got {result}, expected {expected}")
    
    def test_queue_solution(self):
        """Test the queue-based implementation."""
        for n, k, expected in self.test_cases:
            with self.subTest(n=n, k=k):
                result = josephus_queue(n, k)
                self.assertEqual(result, expected,
                               f"Queue: n={n}, k={k}, got {result}, expected {expected}")
    
    def test_mathematical_solution(self):
        """Test the mathematical formula implementation."""
        for n, k, expected in self.test_cases:
            with self.subTest(n=n, k=k):
                result = josephus_mathematical(n, k)
                self.assertEqual(result, expected,
                               f"Mathematical: n={n}, k={k}, got {result}, expected {expected}")
    
    def test_simulation_solution(self):
        """Test the simulation implementation."""
        for n, k, expected in self.test_cases:
            with self.subTest(n=n, k=k):
                result, elimination_order = josephus_simulation(n, k, show_steps=False)
                self.assertEqual(result, expected,
                               f"Simulation: n={n}, k={k}, got {result}, expected {expected}")
                # Check that elimination order has correct length
                self.assertEqual(len(elimination_order), n - 1,
                               f"Elimination order should have {n-1} elements, got {len(elimination_order)}")
    
    def test_all_methods_consistency(self):
        """Test that all methods give the same result for the same input."""
        methods = [
            josephus_recursive,
            josephus_iterative,
            josephus_queue,
            josephus_mathematical,
            lambda n, k: josephus_simulation(n, k, show_steps=False)[0]
        ]
        
        for n, k, expected in self.test_cases:
            results = []
            for method in methods:
                try:
                    result = method(n, k)
                    results.append(result)
                except RecursionError:
                    # Skip recursive method for large n
                    continue
            
            # All results should be the same
            self.assertTrue(all(r == results[0] for r in results),
                          f"Inconsistent results for n={n}, k={k}: {results}")
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Test n=1 (single person)
        self.assertEqual(josephus_mathematical(1, 1), 1)
        self.assertEqual(josephus_mathematical(1, 100), 1)
        
        # Test k=1 (eliminate every person sequentially)
        self.assertEqual(josephus_mathematical(5, 1), 5)
        self.assertEqual(josephus_mathematical(10, 1), 10)
        
        # Test k > n (k=7 with n=5 should still work correctly)
        self.assertEqual(josephus_mathematical(5, 7), 4)
    
    def test_elimination_order(self):
        """Test that elimination order is correct for known cases."""
        # Test case: n=5, k=2
        # Circle: 1, 2, 3, 4, 5
        # Expected elimination order: 2, 4, 1, 5, survivor=3
        survivor, elimination_order = josephus_simulation(5, 2, show_steps=False)
        self.assertEqual(survivor, 3)
        self.assertEqual(elimination_order, [2, 4, 1, 5])
        
        # Test case: n=7, k=3
        # Expected elimination order: 3, 6, 2, 7, 5, 1, survivor=4
        survivor, elimination_order = josephus_simulation(7, 3, show_steps=False)
        self.assertEqual(survivor, 4)
        self.assertEqual(elimination_order, [3, 6, 2, 7, 5, 1])


def run_performance_test():
    """Run a simple performance test comparing all methods."""
    import time
    
    print("\nPerformance Test Results:")
    print("-" * 40)
    
    test_cases = [
        (100, 3),
        (1000, 7),
        (5000, 13)
    ]
    
    methods = [
        ("Mathematical", josephus_mathematical),
        ("Iterative", josephus_iterative),
        ("Queue", josephus_queue),
    ]
    
    for n, k in test_cases:
        print(f"\nn={n}, k={k}:")
        for name, method in methods:
            start_time = time.time()
            result = method(n, k)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(f"  {name:12}: {execution_time:8.4f} ms (result: {result})")


if __name__ == "__main__":
    # Run unit tests
    print("Running Josephus Problem Tests...")
    unittest.main(verbosity=2, exit=False)
    
    # Run performance tests
    run_performance_test()