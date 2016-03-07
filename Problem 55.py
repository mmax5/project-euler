
def is_palindrome(s):
    start = 0
    end = len(s)-1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def is_lychrel(s):
    n = s
    i = 0
    while i < 50:
        n = n + int(str(n)[::-1])
        if is_palindrome(str(n)):
            return True
        i += 1
    return False


def main():
    count = 0
    for i in range(0, 10000):
        if is_lychrel(i):
            pass
        else:
            count += 1
    print count

if __name__ == "__main__":
    main()
