#!/usr/bin/env python3
"""
Interactive Josephus Problem Solver

This script provides a user-friendly interface to solve the Josephus problem
with custom inputs and view detailed results.
"""

import sys
from josephus_problem import (
    josephus_recursive,
    josephus_iterative,
    josephus_queue,
    josephus_mathematical,
    josephus_simulation,
    benchmark_methods
)


def get_positive_integer(prompt, min_value=1):
    """Get a positive integer from user input with validation."""
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Please enter a number >= {min_value}")
        except ValueError:
            print("Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)


def display_results(n, k):
    """Display results using all methods."""
    print(f"\n{'='*60}")
    print(f"JOSEPHUS PROBLEM SOLUTION")
    print(f"n = {n} people, k = {k} (eliminate every {k}-th person)")
    print(f"{'='*60}")
    
    methods = [
        ("Recursive", josephus_recursive),
        ("Iterative", josephus_iterative),
        ("Queue-based", josephus_queue),
        ("Mathematical", josephus_mathematical)
    ]
    
    print("\nResults from different methods:")
    print("-" * 35)
    
    for name, method in methods:
        try:
            if name == "Recursive" and n > 1000:
                print(f"{name:12}: Skipped (too large for recursion)")
            else:
                result = method(n, k)
                print(f"{name:12}: Position {result}")
        except RecursionError:
            print(f"{name:12}: RecursionError (n too large)")
        except Exception as e:
            print(f"{name:12}: Error - {e}")


def show_simulation(n, k):
    """Show detailed simulation of the elimination process."""
    print(f"\n{'='*60}")
    print(f"DETAILED SIMULATION")
    print(f"{'='*60}")
    
    if n > 20:
        response = input(f"Show step-by-step elimination for {n} people? (y/n): ").lower()
        show_steps = response == 'y'
    else:
        show_steps = True
    
    survivor, elimination_order = josephus_simulation(n, k, show_steps=show_steps)
    
    if not show_steps:
        print(f"Initial circle: People 1 to {n}")
        print(f"Every {k}-th person eliminated")
        print(f"Survivor: Person {survivor}")
    
    print(f"\nElimination order: {elimination_order}")
    print(f"Survivor: Person {survivor}")


def run_benchmark(n, k):
    """Run performance benchmark."""
    print(f"\n{'='*60}")
    print(f"PERFORMANCE BENCHMARK")
    print(f"{'='*60}")
    
    benchmark_methods(n, k)


def print_help():
    """Print help information about the Josephus problem."""
    help_text = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    JOSEPHUS PROBLEM HELP                     ║
    ╚══════════════════════════════════════════════════════════════╝
    
    The Josephus problem is a classic problem in mathematics and computer 
    science. Here's how it works:
    
    • n people stand in a circle
    • Starting from person 1, count k positions
    • The k-th person is eliminated from the circle
    • Continue counting k positions from the next person
    • Repeat until only one person remains
    
    Example with n=7, k=3:
    Circle: [1, 2, 3, 4, 5, 6, 7]
    
    Count 3 from position 1: eliminate person 3
    Circle: [1, 2, 4, 5, 6, 7]
    
    Count 3 from position 4: eliminate person 6
    Circle: [1, 2, 4, 5, 7]
    
    And so on... until person 4 survives.
    
    This implementation provides multiple algorithms:
    • Recursive: O(n) time, O(n) space
    • Iterative: O(n*k) time, O(n) space  
    • Queue-based: O(n*k) time, O(n) space
    • Mathematical: O(n) time, O(1) space (fastest)
    """
    print(help_text)


def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print(f"\n{'='*60}")
        print(f"JOSEPHUS PROBLEM INTERACTIVE SOLVER")
        print(f"{'='*60}")
        print("1. Solve Josephus problem")
        print("2. Show detailed simulation")
        print("3. Run performance benchmark")
        print("4. Help / About the problem")
        print("5. Exit")
        print("-" * 60)
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                n = get_positive_integer("Enter number of people (n): ")
                k = get_positive_integer("Enter step size (k): ")
                display_results(n, k)
                
            elif choice == '2':
                n = get_positive_integer("Enter number of people (n): ")
                k = get_positive_integer("Enter step size (k): ")
                show_simulation(n, k)
                
            elif choice == '3':
                n = get_positive_integer("Enter number of people for benchmark (n): ")
                k = get_positive_integer("Enter step size (k): ")
                run_benchmark(n, k)
                
            elif choice == '4':
                print_help()
                
            elif choice == '5':
                print("Thank you for using the Josephus Problem Solver!")
                break
                
            else:
                print("Invalid choice. Please enter 1-5.")
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except EOFError:
            print("\nExiting...")
            break


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)