# SilkyArcTool
## English
Dual languaged (rus+eng) GUI tool for packing and unpacking archives of Silky Engine. **It is not the same arc as used in Ai6WIN and AI5WIN. For AI6WIN .arc archives use [AI6WINArcTool](https://github.com/TesterTesterov/AI6WINArcTool) instead, for AI5WIN's use [AI5WINArcTool](https://github.com/TesterTesterov/AI5WINArcTool)!** If you want to work with Silky Engine's .mes scripts, use [mesScriptAsseAndDisassembler](https://github.com/TesterTesterov/mesScriptAsseAndDisassembler) instead.

Why this tool was created, if there are other tools that can work with this type of archive? The answer is simple: because there was no actually good enough tools. One tool can only extract the data, other -- only pack, but without using original compression, that resulting in outrageous big output archives. My tool solves all the issues -- not only it can extract archives, but also pack them from files, compressing it by algorithm (variation of LZSS), extraction of which was implemented by Silky Engine. Through the tool has one problem -- it works quite slow, especially for packing, so you may need to wait for some minutes (due to implementation compression algorithm on Python).

## Русский
Двуязычное средство (рус+англ) для распаковки и запаковки архивов Silky Engine. **Не стоит путать его с разновидностями .arc, используемым в AI6WIN и AI5WIN. Для них используйте другие средства: [AI6WINArcTool](https://github.com/TesterTesterov/AI6WINArcTool) и [AI5WINArcTool](https://github.com/TesterTesterov/AI5WINArcTool) соответственно!** Ежели вам нужно работать со скриптами .mes Silky Engine, используйте [mesScriptAsseAndDisassembler](https://github.com/TesterTesterov/mesScriptAsseAndDisassembler).

Почему же это средство было создано, ежель и так есть средства, что могут работать с сим типом архива? Ответ прост: ни одно из тех существующих средств не является достаточно хорошим. Одно может только извлекать, другое -- только запаковывать, однако ж без использования оригинального алгоритма сжатия, из-за чего архивы получаются большими сверх всякой меры. Но моё средство исправляет эти проблемы: оно может как распаковывать данные, так и запаковывать их, причём сжимая файлы так, как их хочет видеть Silky Engine (разновидностью LZSS). Единственная, однако, проблема у средства есть -- несколько медленно работает оно, особенно при запаковке, так что может придётся прождать несколько минут (ввиду реализации алгоритма сжатия на Python).

# Usage
## English
![image](https://user-images.githubusercontent.com/66121918/147558363-f100541f-9555-41cf-9154-1a39d5da9991.png)
1. Run the tool (main.py or .exe).
2. Print filename (with extension!!!) or choose it by clicking on button "...".
3. Print directory or choose it by clicking on button "...".
4. To unpack push the button "Unpack archive", to pack -- "Pack archive" or "Pack archive (no compression)".
5. Just wait until it done.

## Русский
![image](https://user-images.githubusercontent.com/66121918/147558230-702f168c-7209-41c3-9b36-781f667f08f3.png)
1. Запустите пакет средств (main.py иль .exe).
2. Введите имя архива (с расширением!!!) или выберите его, нажав на кнопку "...".
3. Введите имя директории файлов или выберите его, нажав на кнопку "...".
4. Нажмите на кнопку, соответствующую желаемому действию ("Распаковать архив", "Запаковать архив" и "Запаковать архив (без сжатия)").
5. Ждите завершения.

# Tested on:

## On English
- [Hikari no Umi no Apeiria \~Casablanca no Kishi\~](https://vndb.org/v21857).
- [Kimagure Temptation 18+ Patch](https://vndb.org/r84708).

## На русском
- [Апейрия живописных морей: Рыцари Касабланки](https://vndb.org/v21857).
- [Соблазнение по прихоти: 18+ патч](https://vndb.org/r84708).
