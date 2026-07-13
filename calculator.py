def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return x / y

def main():
    print("=== 파이썬 계산기 ===")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")
    print("0. 종료")

    while True:
        choice = input("\n원하는 연산을 선택하세요 (0~4): ").strip()

        if choice == "0":
            print("계산기를 종료합니다.")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("잘못된 선택입니다. 0~4 중에서 선택하세요.")
            continue

        try:
            num1 = float(input("첫 번째 숫자: ").strip())
            num2 = float(input("두 번째 숫자: ").strip())
        except ValueError:
            print("숫자만 입력하세요.")
            continue

        try:
            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)

            print(f"결과: {result}")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    main()