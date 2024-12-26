# 📚 Game Theory and Operations Research <br> (Course Task)
<div style="text-align: center; font-size: 30px;">
    Реализация двух задач:
</div>

### 1. MILP: Simplex Method + Branch and Bound (benchmark: MIPLIB);<br><br> 2. PSO (Python) + Schaffer function N.4;
#
#
## 🍃 MILP: SM + BrAB
<div style="text-align: center; font-size: 15px;">
    Coming soon...
</div>

#
#
## 🐝PSO: fun. Schaffer N.4
*   ## 📊results + 🔬analysis
<div style="text-align: center; font-size: 25px;">

    Работа алгоритма при 200 итерациях:
<img src="PSO/images/pso_schaffer_animation.gif" style="max-width: 100%;" alt="pso_process" />

    Траектория значения функции при итерациях:
<img src="PSO/images/pso_fval_convergence.png" style="max-width: 100%;" alt="fval_convergence" />

    Траектория x_0 при итерациях:
<img src="PSO/images/pso_val0_convergence.png" style="max-width: 100%;" alt="val0_convergence" />
    
    Траектория x_1 при итерациях:
<img src="PSO/images/pso_val1_convergence.png" style="max-width: 100%;" alt="val1_convergence" />
</div>

### Функция Шаффера номер 4 :
$$
f(x) = 0.5 + \frac{\cos^2\left(\sin\left(\left|x_0^2 - x_1^2\right|\right)\right) - 0.5}{\left(1 + 0.001 \cdot \left(x_0^2 + x_1^2\right)\right)^2}
$$
### Точными значениями глобального миниммума функции были выбраны: (**[Wiki]('https://ru.wikipedia.org/wiki/Тестовые_функции_для_оптимизации)**)
$$
f(0, 1.25313) = 0.292579
$$
### Реализация алгоритма в этом репозитории выдает следующие значения при 200 итерациях:

$$
f(-4.33038583e-04, 1.25312983e+00) = 0.29257863220358526
$$

### В некоторых случаях, алгоритм может выдавать переменные с другим знаком - это нормально из-за симметрии функци и элемента случайности алгоритма
