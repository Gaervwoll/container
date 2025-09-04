import os
import sys
from typing import Optional
import Main



def clear_screen() -> None:
	os.system("cls" if os.name == "nt" else "clear")

def print_header(current_dir: str) -> None:
	print("================= Container =================")
	print(f"Выбранная директория данных: {current_dir}")
	print("========================================================\n")

def choose_directory(current_dir: str) -> str:
	print("Введите путь к директории с данными (пусто — оставить без изменений):")
	inp = input("> ").strip().strip('"')
	if not inp:
		return current_dir
	if not os.path.isdir(inp):
		print("Путь не существует или не является директорией. Оставляю прежнее значение.")
		input("Нажмите Enter для продолжения...")
		return current_dir
	return inp

def main(argv: Optional[list] = None) -> int:
	data_dir = os.path.join(os.getcwd(), "data")

	while True:
		clear_screen()
		print_header(data_dir)
		print("Меню:")
		print("  1) Выбрать директорию с данными")
		print("  2) Запустить ")
		print("  0) Выход")
		choice = input("Выбор > ").strip()

		if choice == "1":
			data_dir = choose_directory(data_dir)
		elif choice == "2":
			run_analysis(data_dir)
		elif choice == "0":
			print("Выход...")
			break
		else:
			print("Неизвестная команда.")
			input("Нажмите Enter для продолжения...")
	return 0

if __name__ == "__main__":
	sys.exit(main())