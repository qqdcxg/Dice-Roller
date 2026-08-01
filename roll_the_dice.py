import random

def roll_dice(times: int) -> float:
    """模拟掷骰子 times 次，返回平均点数"""
    total = 0
    for _ in range(times):
        total += random.randint(1, 6)   # 生成1~6的随机整数
    return total / times

def main():
    try:
        n = int(input("请输入掷骰子的次数: "))
        if n <= 0:
            print("次数必须是正整数，请重新运行程序。")
            return
        avg = roll_dice(n)
        # 保留两位小数输出，也可以直接输出更多位
        print(f"掷骰子 {n} 次，平均点数为: {avg:.4f}")
    except ValueError:
        print("输入无效，请输入一个整数。")

if __name__ == "__main__":
    main()