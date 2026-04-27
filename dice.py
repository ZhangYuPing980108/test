#!/usr/bin/env python3
"""
骰子程式 - 支援投擲一個或多個骰子
"""

import random


class Dice:
    """骰子類別"""
    
    def __init__(self, sides=6):
        """
        初始化骰子
        
        Args:
            sides: 骰子面數 (預設6)
        """
        self.sides = sides
    
    def roll(self):
        """
        投擲一次骰子
        
        Returns:
            int: 投擲結果 (1-sides)
        """
        return random.randint(1, self.sides)
    
    def roll_multiple(self, count):
        """
        投擲多次骰子
        
        Args:
            count: 投擲次數
            
        Returns:
            list: 每次投擲的結果
        """
        return [self.roll() for _ in range(count)]


def main():
    """主程式 - 互動式骰子投擲"""
    print("=== 骰子程式 ===")
    print("選擇要執行的操作:")
    print("1. 投擲一個6面骰子")
    print("2. 投擲多個骰子")
    print("3. 自訂骰子面數")
    print("4. 結束")
    
    while True:
        choice = input("\n請選擇 (1-4): ").strip()
        
        if choice == "1":
            dice = Dice()
            result = dice.roll()
            print(f"🎲 投擲結果：{result}")
        
        elif choice == "2":
            try:
                count = int(input("投擲幾次？ "))
                if count <= 0:
                    print("請輸入正整數")
                    continue
                dice = Dice()
                results = dice.roll_multiple(count)
                print(f"投擲結果：{results}")
                print(f"總和：{sum(results)}")
            except ValueError:
                print("請輸入有效的數字")
        
        elif choice == "3":
            try:
                sides = int(input("骰子有幾面？ "))
                count = int(input("投擲幾次？ "))
                if sides <= 0 or count <= 0:
                    print("請輸入正整數")
                    continue
                dice = Dice(sides)
                results = dice.roll_multiple(count)
                print(f"投擲結果：{results}")
                print(f"總和：{sum(results)}")
            except ValueError:
                print("請輸入有效的數字")
        
        elif choice == "4":
            print("謝謝使用，再見！")
            break
        
        else:
            print("無效選擇，請重新輸入")


if __name__ == "__main__":
    main()
