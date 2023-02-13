import cProfile

def recursive(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (recursive(n - 2) + recursive(n-1))


if __name__ == "__main__":
    i: int = 0
    while i < 40:
        print (f"#########################################\n{i}\n#########################################")
        cProfile.run(f'recursive({i})')
        i = i + 1
