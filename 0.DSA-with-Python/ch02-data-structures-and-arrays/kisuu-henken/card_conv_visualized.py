import string

# ある10進数の整数を10進数からn(2~36)進数に基数変換するプログラムです。


def cd_conv(x: int, target_base: int) -> str:
    result = ""
    chars = (
        string.digits + string.ascii_uppercase
    )  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

    if target_base < 2 or target_base > 36:
        raise ValueError("Target Base must be between 2 and 36.")

    if x == 0:
        return "0"
    elif x < 0 or x % 1 != 0:
        raise ValueError("Value must be positive integer.")

    else:
        m = len(str(target_base))
        n = len(str(x))
        print()
        print(f"{target_base:{m}} | {x:{n}}")
        while x > 0:
            print(f"{' '*m} +{'-'*(n+2)}")
            if x // target_base:
                print(
                    f"{target_base:{m}} | {x//target_base:{n}}  ... {chars[x%target_base]}"
                )
            else:
                print(f"{x//target_base:{n+m+3}}  ... {chars[x%target_base]} ")

            result += chars[x % target_base]
            x //= target_base

    print()
    return result[::-1]


if __name__ == "__main__":
    print("10進数の整数をn進数へ基数変換します。")

    while True:
        while True:
            no = int(input("変換する非負の整数: "))
            if no > 0 and no % 1 == 0:
                break

        while True:
            cd = int(input("何進数に変換しますか(2~36)?: "))
            if 2 <= cd <= 36 and cd % 1 == 0:
                break

        print(f"10進数{no}の {cd}進数 は {cd_conv(no, cd)} です。")

        repeat = input("再度計算しますか？（Y...はい/N...いいえ）: ")
        if repeat in {"N", "n"}:
            break
