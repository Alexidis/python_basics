import lesson4_1 as l1
import lesson4_2 as l2
import lesson4_3 as l3
import lesson4_4 as l4
import lesson4_5 as l5
import lesson4_6 as l6
import lesson4_7 as l7

if __name__ == '__main__':
    l1.argv = input('Введите выработку в часах, ставку за час и премию сотрудника ').split()
    print(f'Зарплата с бонусом составляет: {l1.calc_salary()}')

    l2_list = input('Введите список ').split()
    print(l2.greatest_prev(l2_list))

    print(f'Список чисел кратных 20 или 21 в интервале от 20 до 240 {l3.twenty_multiples()}')

    l4_list = input('Введите список ').split()
    print(f'Список уникальных значенй {l4.unique_list(l4_list)}')

    l5_low_bound, l5_high_bound, = input('Введите верхнюю и нижнюю границы ').split()
    print(f'{l5.list_production(int(l5_low_bound), int(l5_high_bound))}')

    l6_low_bound = int(input('Введите начальное значение итератора '))
    count_itr = l6.count_iter_creator(l6_low_bound)
    print(f'Из итератора получился список {list(count_itr)}')

    l6_list = input('Введите список для повторения ').split()
    cycle_itr = l6.cycle_iter_creator(l6_list)
    print(f'Из итератора получился список {list(cycle_itr)}')

    l7_item = int(input('Введите число факториал которого необходимо вычислить '))
    i = 1
    for el in l7.inner_fact(l7_item):
        print(f'На {i}-ом шаге значение факториала равно {el}')
        i += 1
