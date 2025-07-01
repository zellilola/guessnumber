"""
Josephus Problem Solution

The Josephus problem is a classic problem in computer science and mathematics.
Given n people standing in a circle waiting to be executed, every k-th person 
is eliminated from the circle. The problem asks for the position of the last 
remaining person.

This module provides multiple implementations:
1. Recursive approach
2. Iterative approach using list
3. Mathematical formula approach
4. Queue-based approach
"""

from collections import deque
import math


def josephus_recursive(n, k):
    """
    Solve Josephus problem using recursion.
    
    Args:
        n (int): Number of people in the circle (1-indexed)
        k (int): Every k-th person is eliminated
    
    Returns:
        int: Position of the survivor (1-indexed)
    
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack
    """
    if n == 1:
        return 1
    return (josephus_recursive(n - 1, k) + k - 1) % n + 1


def josephus_iterative(n, k):
    """
    Solve Josephus problem using iterative approach with list.
    
    Args:
        n (int): Number of people in the circle
        k (int): Every k-th person is eliminated
    
    Returns:
        int: Position of the survivor (1-indexed)
    
    Time Complexity: O(n*k) in worst case
    Space Complexity: O(n)
    """
    people = list(range(1, n + 1))
    position = 0
    
    while len(people) > 1:
        # Calculate the index of the person to eliminate
        position = (position + k - 1) % len(people)
        people.pop(position)
    
    return people[0]


def josephus_queue(n, k):
    """
    Solve Josephus problem using queue (deque).
    
    Args:
        n (int): Number of people in the circle
        k (int): Every k-th person is eliminated
    
    Returns:
        int: Position of the survivor (1-indexed)
    
    Time Complexity: O(n*k)
    Space Complexity: O(n)
    """
    queue = deque(range(1, n + 1))
    
    while len(queue) > 1:
        # Rotate the queue k-1 times to get the k-th person at front
        for _ in range(k - 1):
            queue.append(queue.popleft())
        # Remove the k-th person
        queue.popleft()
    
    return queue[0]


def josephus_mathematical(n, k):
    """
    Solve Josephus problem using mathematical formula (0-indexed).
    
    Args:
        n (int): Number of people in the circle
        k (int): Every k-th person is eliminated
    
    Returns:
        int: Position of the survivor (1-indexed)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    result = 0
    for i in range(2, n + 1):
        result = (result + k) % i
    return result + 1  # Convert to 1-indexed


def josephus_simulation(n, k, show_steps=False):
    """
    Solve Josephus problem with detailed simulation showing each elimination.
    
    Args:
        n (int): Number of people in the circle
        k (int): Every k-th person is eliminated
        show_steps (bool): Whether to print elimination steps
    
    Returns:
        tuple: (survivor_position, elimination_order)
    """
    people = list(range(1, n + 1))
    elimination_order = []
    position = 0
    
    if show_steps:
        print(f"Initial circle: {people}")
        print(f"Every {k}-th person will be eliminated\n")
    
    step = 1
    while len(people) > 1:
        # Calculate the index of the person to eliminate
        position = (position + k - 1) % len(people)
        eliminated = people.pop(position)
        elimination_order.append(eliminated)
        
        if show_steps:
            print(f"Step {step}: Eliminated person {eliminated}")
            print(f"Remaining: {people}")
            print()
        
        step += 1
    
    survivor = people[0]
    if show_steps:
        print(f"Survivor: Person {survivor}")
    
    return survivor, elimination_order


def benchmark_methods(n, k):
    """
    Benchmark different methods for solving Josephus problem.
    
    Args:
        n (int): Number of people
        k (int): Step size
    """
    import time
    
    methods = [
        ("Recursive", josephus_recursive),
        ("Iterative", josephus_iterative),
        ("Queue", josephus_queue),
        ("Mathematical", josephus_mathematical)
    ]
    
    print(f"Benchmarking Josephus problem with n={n}, k={k}")
    print("-" * 50)
    
    results = {}
    for name, method in methods:
        start_time = time.time()
        try:
            result = method(n, k)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            results[name] = (result, execution_time)
            print(f"{name:12}: Result = {result:4}, Time = {execution_time:.4f} ms")
        except RecursionError:
            print(f"{name:12}: RecursionError (n too large)")
        except Exception as e:
            print(f"{name:12}: Error - {e}")
    
    return results


def main():
    """
    Demonstrate different approaches to solve the Josephus problem.
    """
    print("=" * 60)
    print("JOSEPHUS PROBLEM SOLVER")
    print("=" * 60)
    
    # Example 1: Classic Josephus problem
    n, k = 7, 3
    print(f"\nExample 1: n={n}, k={k}")
    print("-" * 30)
    
    print("Method comparison:")
    methods = [
        ("Recursive", josephus_recursive),
        ("Iterative", josephus_iterative),
        ("Queue", josephus_queue),
        ("Mathematical", josephus_mathematical)
    ]
    
    for name, method in methods:
        result = method(n, k)
        print(f"{name:12}: {result}")
    
    # Example 2: Show simulation
    print(f"\nExample 2: Detailed simulation (n={n}, k={k})")
    print("-" * 40)
    survivor, elimination_order = josephus_simulation(n, k, show_steps=True)
    print(f"Elimination order: {elimination_order}")
    
    # Example 3: Benchmark with larger numbers
    print(f"\nExample 3: Performance benchmark")
    print("-" * 30)
    benchmark_methods(1000, 3)
    
    # Example 4: Interactive mode
    print(f"\nExample 4: Different test cases")
    print("-" * 30)
    test_cases = [(5, 2), (10, 3), (41, 3), (100, 7)]
    
    for n, k in test_cases:
        result = josephus_mathematical(n, k)
        print(f"n={n:3}, k={k}: Survivor at position {result}")


if __name__ == "__main__":
    main()