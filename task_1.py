from pathlib import Path
import shutil

def recursive_folder_copy(source: Path, output: Path):
    try:

        for item in source.iterdir():
            if item.is_dir():
                recursive_folder_copy(item, output)
            else:
                extension = item.suffix[1:]
                (output / extension).mkdir(parents=True, exist_ok=True)
                shutil.copy(item, output / extension / item.name)
    except Exception as e:
        print(f'Виникла помилка. Деталі: {e}')
            
def main():
    source_input = input('Введіть назву папку, з якої необхідно скопіювати дані:')
    output_input = input('Введіть назву папку, в яку необхідно скопіювати дані:')
        
    if not source_input or not output_input:
        print("Помилка: обидві назви папок мають бути введені.")
        return
    
    source_path = Path(source_input)
    output_path = Path(output_input)
 
    if not source_path.exists():
        print("Такої папки не існує.")
        return
    if not source_path.is_dir():
        print("Шлях має містити назву папки.")
        return
    if not output_path.exists():
        output_path.mkdir(parents=True, exist_ok=True)

    recursive_folder_copy(source_path, output_path)
    print("Дані скопійовані успішно :)")

if __name__ == "__main__":
    main()