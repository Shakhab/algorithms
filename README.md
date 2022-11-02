# Алгоритмы

Решение задач по алгоритмам на языке Python

---

## 1. Введение в алгоритмы

---
<details>
<summary>
<a href="Basic_algorithms/A.A+B.py">A. A+B</a>
</summary>

#### Условие
В этой задачи вам придётся прочитать два числа и сложить их. Результат необходимо вывести на стандартный поток вывода или в файл, указанный в условии задачи.

#### Формат ввода
В первой строке задано первое число, во второй – второе. Оба числа лежат в диапазоне от −10^9 до 10^9.

#### Формат вывода
Выведите единственное число – результат сложения двух чисел.

#### Пример
<table><tbody>
  <tr>
    <td><b>Ввод</b></td>
    <td><b>Вывод</b></td>
  </tr>
  <tr>
    <td valign='top'>
12<br>
90<br>

</td>
  <td valign='top'>
102<br>
</td>
  </tr>
</tbody></table>

</details>

---

<details>
<summary>
<a href="Basic_algorithms/B.Zipper_Closure.py">B. Застёжка-молния</a>
</summary>

#### Условие
Даны два массива чисел длины n. Составьте из них один массив длины 2n, в котором числа из входных массивов чередуются (первый — второй — первый — второй — ...). При этом относительный порядок следования чисел из одного массива должен быть сохранён.

#### Формат ввода
В первой строке записано целое число n –— длина каждого из массивов, 1 ≤ n ≤ 1000.

Во второй строке записано n чисел из первого массива, через пробел.

В третьей строке –— n чисел из второго массива.

Значения всех чисел –— натуральные и не превосходят 1000.

#### Формат вывода
Выведите 2n чисел из объединённого массива через пробел.

#### Пример
<table><tbody>
  <tr>
    <td><b>Ввод</b></td>
    <td><b>Вывод</b></td>
  </tr>
  <tr>
    <td valign='top'>
3<br>
1 2 3<br>
4 5 6<br>

</td>
  <td valign='top'>
1 4 2 5 3 6<br>
</td>
  </tr>
</tbody></table>

</details>

---

<details>
<summary>
<a href="Basic_algorithms/C.Moving_Average.py">C. Скользящее среднее</a>
</summary>

#### Условие
Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.

Измерения велись n секунд.

В секунду i поступает qi запросов.

Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.

#### Формат ввода
В первой строке передаётся натуральное число n, количество секунд, в течение которых велись измерения. 1 ≤ n ≤ 105

Во второй строке через пробел записаны n целых неотрицательных чисел qi, каждое лежит в диапазоне от 0 до 103.

В третьей строке записано натуральное число k (1 ≤ k ≤ n) —– окно сглаживания.

Примечание для Go:

Заметьте, что в данной задаче достаточно большой размер ввода. Поэтому необходимо задавать размер буфера для сканнера хотя бы 600 Кб.

#### Формат вывода
Выведите через пробел результат применения метода скользящего среднего к серии измерений. Должно быть выведено n - k + 1 элементов, каждый элемент -— вещественное (дробное) число.

#### Пример
<table><tbody>
  <tr>
    <td><b>Ввод</b></td>
    <td><b>Вывод</b></td>
  </tr>
  <tr>
    <td valign='top'>
7<br>
1 2 3 4 5 6 7<br>
4<br>

</td>
  <td valign='top'>
2.5 3.5 4.5 5.5<br>
</td>
  </tr>
</tbody></table>

</details>

---

<details>
<summary>
<a href="Basic_algorithms/D.Two_Chips.py">D. Две фишки</a>
</summary>

#### Условие
Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков. Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.

Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи. Помогите ей написать программу для поиска нужных фишек.

#### Формат ввода
В первой строке записано количество фишек n, 2 ≤ n ≤ 10^4.

Во второй строке записано n целых чисел —– очки на фишках Риты в диапазоне от -10^5 до 10^5.

В третьей строке —– загаданное Гошей целое число k, -10^5 ≤ k ≤ 10^5.

#### Формат вывода
Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.

Если таких пар несколько, то можно вывести любую из них.

Если таких пар не существует, то вывести «None».

#### Пример
<table><tbody>
  <tr>
    <td><b>Ввод</b></td>
    <td><b>Вывод</b></td>
  </tr>
  <tr>
    <td valign='top'>
6<br>
-1 -1 -9 -7 3 -6<br>
2<br>

</td>
  <td valign='top'>
-1 3<br>
</td>
  </tr>
</tbody></table>

</details>

---

<details>
<summary>
<a href="Basic_algorithms/E.Two_Chips_1.py">E. Две фишки - 2</a>
</summary>

#### Условие
Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков. Фишки лежат на столе в порядке неубывания очков на них. Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.

Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи. Помогите ей написать программу для поиска нужных фишек.

#### Формат ввода
В первой строке записано количество фишек n, 2 ≤ n ≤ 10^5.

Во второй строке записано n целых чисел в порядке неубывания —– очки на фишках Риты в диапазоне от -10^5 до 10^5.

В третьей строке —– загаданное Гошей целое число k, -10^5 ≤ k ≤ 10^5.

#### Формат вывода
Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.

Если таких пар несколько, то можно вывести любую из них.

Если таких пар не существует, то вывести «None».

#### Пример
<table><tbody>
  <tr>
    <td><b>Ввод</b></td>
    <td><b>Вывод</b></td>
  </tr>
  <tr>
    <td valign='top'>
6<br>
-9 -7 -6 -1 -1 3<br>
2<br>

</td>
  <td valign='top'>
-1 3<br>
</td>
  </tr>
</tbody></table>

</details>

---

<details>
<summary>
<a href="Basic_algorithms/two_chip_extra.py">E. Две фишки экстра</a>
</summary>

#### Условие
Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков. Фишки лежат на столе в порядке неубывания очков на них. Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.

Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи. Помогите ей написать программу для поиска нужных фишек.

#### Формат ввода
В первой строке записано количество фишек n, 2 ≤ n ≤ 10^5.

Во второй строке записано n целых чисел в порядке неубывания —– очки на фишках Риты в диапазоне от -10^5 до 10^5.

В третьей строке —– загаданное Гошей целое число k, -10^5 ≤ k ≤ 10^5.

#### Формат вывода
Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.

Если таких пар несколько, то можно вывести любую из них.

Если таких пар не существует, то вывести «None».

#### Пример
<table><tbody>
  <tr>
    <td><b>Ввод</b></td>
    <td><b>Вывод</b></td>
  </tr>
  <tr>
    <td valign='top'>
6<br>
-9 -7 -6 -1 -1 3<br>
2<br>

</td>
  <td valign='top'>
-1 3<br>
</td>
  </tr>
</tbody></table>

</details>

---
