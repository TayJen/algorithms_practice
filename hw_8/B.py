def main():
    t = int(input())
    while t:
        n = int(input())
        print(' '.join(map(str, [i * 2 for i in range(n, n+n)])))

        t -= 1


if __name__ == "__main__":
    main()
