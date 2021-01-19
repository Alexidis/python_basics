import lesson1 as l1
import lesson2 as l2
import lesson3 as l3
import lesson4 as l4
import lesson5 as l5
import lesson6 as l6
import lesson7 as l7
import lesson8 as l8

if __name__ == '__main__':
    # первая практика
    l1.p1_print_simple()
    l1.p2_sec_to_time()
    l1.p3_wild_s()
    l1.p4_greatest_digit_1()
    l1.p4_greatest_digit_2()
    l1.p4_greatest_digit_3()
    l1.p4_greatest_digit_4()
    l1.p5_some_economics()
    print(l1.p6_fitness_tracker())

    # вторая практика
    l2.p1_print_variables()
    l2.p2_elem_replacement()
    l2.p3_show_season_list()
    l2.p3_show_season_dict()
    l2.p4_separate_string()
    l2.p5_get_ratings()
    l2.p6_pivot_table()

    # третья практика
    l3.p1_div_func()
    l3.p2_user_form_printer()
    l3.p3_greatest_sum()
    l3.p4_my_pow1()
    l3.p4_my_pow2()
    l3.p5_sum_quit()
    l3.p6_int_func()

    # четвертая практика
    l4.p1_calc_salary()
    l4.p2_greatest_prev()
    l4.p3_twenty_multiples()
    l4.p4_unique_list()
    l4.p5_list_production()
    l4.p6_iter_creator()
    l4.p7_inner_fact()

    # пятая практика
    l5.p1_programmatic_file()
    l5.p2_file_counter()
    l5.p3_oneC_like()
    l5.p4_numbers_translator()
    l5.p5_file_num_sum()
    l5.p6_school_scheduler()
    l5.p7_profit_calculator()

    # шестая практика
    traffic_light = l6.p1_TrafficLight()
    traffic_light.auto_switch()

    route666 = l6.p2_Road(6600, 60)
    print(f'Масса асфальта для покрытия дороги666 равна {route666.calc_asphalt_mass(6)}')

    new_worker = l6.p3_Position('Филиппов', 'Артем', 'Специалист', 15100, 35700)
    print(f'Приняли сотрудника {new_worker.get_full_name()}, на должность {new_worker.position}'
          f' с ЗП {new_worker.get_total_income()}')

    town_car = l6.p4_TownCar('Toyota', 'Белый', 30, 8, 5, 60)
    work_car = l6.p4_WorkCar('KIA', 'Черный', 20, 10, 3, 40)
    sport_car = l6.p4_SportCar('Ferrari', 'Желтый', 35, 7, 1)
    racers = [town_car, work_car, sport_car]
    mega_race = l6.p4_Race(racers, 300)
    mega_race.start_race()

    pen = l6.p5_Pen('Ручка')
    pencil = l6.p5_Pencil('Карандаш')
    handle = l6.p5_Handle('Маркер')
    pen.draw()
    pencil.draw()
    handle.draw()

    # седьмая практика
    matrix_a = l7.p1_Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
    matrix_b = l7.p1_Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    matrix_c = matrix_a + matrix_b
    print(matrix_c)

    men_coat = l7.p2_Coat('Мужское пальто', 12)
    print(f'На пальто для мужчины ростом {men_coat.height} необходимо {men_coat.fabric_consumption()} метров ткани')
    men_coat.height += 5
    print(f'А на пальто для мужчины ростом {men_coat.height} необходимо {men_coat.fabric_consumption()} метров ткани')

    kid_suit = l7.p2_Suit('Детский костюм', 30)
    print(f'На костюм размером {kid_suit.size} для ребенка необходимо {kid_suit.fabric_consumption()} метров ткани')
    kid_suit.size += 5
    print(f'А на костюм размером {kid_suit.size} для ребенка необходимо {kid_suit.fabric_consumption()} метров ткани')

    cell = l7.p3_Cell(7)
    cell2 = l7.p3_Cell(5)
    cell3 = cell + cell2
    print(cell3.make_order(5))

    cell3 = cell - cell2
    print(cell3.make_order(1))

    cell3 = cell * cell2
    print(cell3.make_order(7))

    cell3 = cell / cell2
    print(cell3.make_order(1))

    # восьмая практика
    date_str = input('Введите дату в формате ДД.ММ.ГГГ ')
    if l8.p1_Date.validate(date_str):
        date = l8.p1_Date(date_str)
        numerologic = date.to_int("Day") + date.to_int("Month") + date.to_int("Year")
        print(f'Сумма чисел в веденой вами дте равна {numerologic}')
    else:
        print(f'Вы ввели не корректную дату')

    (dividend, divisor) = input('Введите делимое и делитель через проьел ').split(' ')
    try:
        if not float(divisor):
            raise l8.p2_ZeroDivisionException
        quotient = float(dividend) / float(divisor)
        print('Вы не смогли сломать програму')
    except l8.p2_ZeroDivisionException:
        print('На ноль делить нельзя')
