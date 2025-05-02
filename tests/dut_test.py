import cocotb
from cocotb.triggers import Timer
import random

async def run_test_cases(dut, test_cases, description):
    """Helper function to run test cases."""
    dut._log.info(f"Running {description} tests...")
    for i, (a_val, b_val, expected_output) in enumerate(test_cases):
        dut._log.info(f"Test case {i+1}: a={a_val}, b={b_val}")
        dut.a.value = a_val
        dut.b.value = b_val
        await Timer(1, units='ns')

        actual_output = dut.y.value
        dut._log.info(f"  Expected output={expected_output}, Actual output={actual_output}")
        assert actual_output == expected_output, \
            f"{description} test failed (Case {i+1}): a={a_val}, b={b_val} produced {actual_output}, expected {expected_output}"
    dut._log.info(f"{description} tests passed.")


@cocotb.test()
async def dut_test(dut):
    dut._log.info("Starting XOR gate test")

    # Exhaustive Test Cases
    exhaustive_cases = [
        (0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)
    ]
    await run_test_cases(dut, exhaustive_cases, "Exhaustive")

    # Randomized Test Cases
    num_random_tests = 10
    randomized_cases = []
    for _ in range(num_random_tests):
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        expected_output = a ^ b
        randomized_cases.append((a, b, expected_output))

    await run_test_cases(dut, randomized_cases, "Randomized")

    dut._log.info("All XOR gate test cases finished successfully.")
