import lesson1 as l1
import lesson2 as l2
import lesson3 as l3
import lesson4 as l4
import lesson5 as l5
import lesson6 as l6

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

    pen = l6.p5_Pen('Ручка')
    pencil = l6.p5_Pencil('Карандаш')
    handle = l6.p5_Handle('Маркер')
    pen.draw()
    pencil.draw()
    handle.draw()




