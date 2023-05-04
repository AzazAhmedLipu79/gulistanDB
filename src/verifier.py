def verifier(data: dict, columns: tuple) -> bool:
    if set(data.keys()) != set(columns):
        print(f"Dataset {data} keys are not the same as {columns}")
        return False
    else:
        print(f"Dataset {data} format PASSED successfully")
        return True
