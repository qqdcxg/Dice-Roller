import random


def roll_single_die() -> int:
    """模拟掷一个六面骰子，返回 1~6 的随机整数。"""
    return random.randint(1, 6)


def get_die_face_name(value: int) -> str:
    """返回对应骰子点数的图案名称。"""
    if value not in range(1, 7):
        raise ValueError("骰子点数必须是 1 到 6 之间")
    return f"die_{value}"


def get_die_face_positions(value: int) -> tuple[tuple[int, int], ...]:
    """返回骰子点数对应的点位坐标，用于界面绘制。"""
    if value not in range(1, 7):
        raise ValueError("骰子点数必须是 1 到 6 之间")

    positions = {
        1: ((40, 40),),
        2: ((24, 24), (56, 56)),
        3: ((24, 24), (40, 40), (56, 56)),
        4: ((24, 24), (24, 56), (56, 24), (56, 56)),
        5: ((24, 24), (24, 56), (40, 40), (56, 24), (56, 56)),
        6: ((24, 24), (24, 40), (24, 56), (56, 24), (56, 40), (56, 56)),
    }
    return positions[value]


def roll_dice(times: int) -> float:
    """模拟掷骰子 times 次，返回平均点数。"""
    total = 0
    for _ in range(times):
        total += roll_single_die()
    return total / times


def main():
    try:
        n = int(input("请输入掷骰子的次数: "))
        if n <= 0:
            print("次数必须是正整数，请重新运行程序。")
            return
        avg = roll_dice(n)
        print(f"掷骰子 {n} 次，平均点数为: {avg:.4f}")
    except ValueError:
        print("输入无效，请输入一个整数。")


if __name__ == "__main__":
    main()