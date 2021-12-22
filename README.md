# SilkyArcTool
## English
Dual languaged (rus+eng) GUI tool for packing and unpacking archives of Silky Engine. This type of .arc archive also used in Ai6WIN engine (and possibly in Ai5WIN) by Silky. If you want to work with Silky Engine's .mes scripts, use [mesScriptAsseAndDisassembler](https://github.com/TesterTesterov/mesScriptAsseAndDisassembler) instead.

Why this tool was created, if there are other tools that can work with this type of archive? The answer is simple: because there was no actually good enough tools. One tool can only extract the data, other -- only pack, but without using original compression, that resulting in outrageous big output archives. My tool solves all the issues -- not only it can extract archives, but also pack them from files, compressing it by algorithm (variation of LZSS), extraction of which was implemented by Silky Engine. Through the tool has one problem -- it works quite slow, especially for packing, so you may need to wait for some minutes (due to implementation compression algorithm on Python).

## Русский
Двуязычное средство (рус+англ) для распаковки и запаковки архивов Silky Engine. Сей вид архива также используется в движке Ai6WIN (и, возможно, в Ai5WIN) от Silky. Ежели вам нужно работать со скриптами .mes Silky Engine, используйте [mesScriptAsseAndDisassembler](https://github.com/TesterTesterov/mesScriptAsseAndDisassembler).

Почему же это средство было создано, ежель и так есть средства, что могут работать с сим типом архива? Ответ прост: ни одно из тех существующих средств не является достаточно хорошим. Одно может только извлекать, другое -- только запаковывать, однако ж без использования оригинального алгоритма сжатия, из-за чего архивы получаются большими сверх всякой меры. Но моё средство исправляет эти проблемы: оно может как распаковывать данные, так и запаковывать их, причём сжимая файлы так, как их хочет видеть Silky Engine (разновидностью LZSS). Единственная, однако, проблема у средства есть -- несколько медленно работает оно, особенно при запаковке, так что может придётся прождать несколько минут (ввиду реализации алгоритма сжатия на Python).

# Usage
## English
![image](https://user-images.githubusercontent.com/66121918/147122698-36aa4d55-3d18-43ee-a86d-f2d73367be86.png)
1. Run the tool (main.py or .exe).
2. Print filename (with extension!!!) or choose it by clicking on button "...".
3. Print directory or choose it by clicking on button "...".
4. Print "0", if thou want to unpack, or "1", if thou want to pack.
5. Just wait until it done.

## Русский
![image](https://user-images.githubusercontent.com/66121918/147131060-480cdf33-33dd-4ffa-9aa5-035962923512.png)
1. Запустите пакет средств (main.py иль .exe).
2. Введите имя архива (с расширением!!!) или выберите его, нажав на кнопку "...".
3. Введите имя директории файлов или выберите его, нажав на кнопку "...".
4. Введите "0", коли распаковать желаете, али "1", коли запаковать желаете.
5. Ждите завершения.

# Tested on:

## On English
- [Hikari no Umi no Apeiria \~Casablanca no Kishi\~](https://vndb.org/v21857).

## На русском
- [Апейрия живописных морей: Рыцари Касабланки](https://vndb.org/v21857).
