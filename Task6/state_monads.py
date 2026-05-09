from pymonad.tools import curry
from pymonad.state import State

# Стейт монады используются для составления чеклиста предполётной проверки самолёта

@curry(2)
def is_fuel_pumps_working(simulate_value: bool, check_list: list[str]):
    def check(current_state: bool):
        # Логика проверки уровня топлива
        fuel_check_result = simulate_value
        result_state = current_state and fuel_check_result
        return check_list + [f'Pumps: {fuel_check_result}'], result_state 
    return State(check)
   
@curry(2) 
def has_engine_oil(simulate_value: bool, check_list: list[str]):
    def check(current_state: bool):
        # Логика проверки уровня масла
        oil_check_result = simulate_value
        result_state = current_state and oil_check_result
        return check_list + [f'Engine oil: {oil_check_result}'], result_state 
    return State(check)

@curry(2)  
def is_flaps_moving(simulate_value: bool, check_list: list[str]):
    def check(current_state: bool):
        # Логика проверки подвижности механизации крыла
        flaps_check_result = simulate_value
        result_state = current_state and flaps_check_result
        return check_list + [f'Flaps: {flaps_check_result}'], result_state 
    return State(check)
    
@curry(2)
def is_breaking_working(simulate_value: bool, check_list: list[str]):
    def check(current_state: bool):
        # Логика проверки тормозной системы
        breaking_check_result = simulate_value
        result_state = current_state and breaking_check_result
        return check_list + [f'Breaking: {breaking_check_result}'], result_state
    return State(check)    

@curry(2)
def is_avionics_working(simulate_value: bool, check_list: list[str]):
    def check(current_state: bool):
        # Логика проверки авионики кабины
        avionics_check_result = simulate_value
        result_state = current_state and avionics_check_result
        return check_list + [f'Avionics: {avionics_check_result}'], result_state
    return State(check)    

@curry(2)
def is_landing_working(simulate_value: bool, check_list: list[str]):
    def check(current_state: bool):
        # Логика проверки шасси
        landing_check_result = simulate_value
        result_state = current_state and landing_check_result
        return check_list + [f'Landing: {landing_check_result}'], result_state
    return State(check)

check_list_init_state = State.insert([])

failed_fligth_check_list = (check_list_init_state.then(is_fuel_pumps_working(True))
                                          .then(has_engine_oil(True))
                                          .then(is_flaps_moving(False))
                                          .then(is_breaking_working(True))
                                          .then(is_avionics_working(True))
                                          .then(is_landing_working(True)))
                                          
fligth_check_list = (check_list_init_state.then(is_fuel_pumps_working(True))
                                          .then(has_engine_oil(True))
                                          .then(is_flaps_moving(True))
                                          .then(is_breaking_working(True))
                                          .then(is_avionics_working(True))
                                          .then(is_landing_working(True)))
                                          
def check_plane(check_list):
    report, result = check_list.run(True)
    
    print('Plane ready to flight' if result else 'Flight prohibited, there is a malfunction')
    
    print(f'Inspection report:\n{report}\n')
    
                                          
check_plane(failed_fligth_check_list)
'''
Результат:
Flight prohibited, there is a malfunction
Inspection report:
['Pumps: True', 'Engine oil: True', 'Flaps: False', 'Breaking: True', 'Avionics: True', 'Landing: True']
'''

check_plane(fligth_check_list)
'''
Результат:
Plane ready to flight
Inspection report:
['Pumps: True', 'Engine oil: True', 'Flaps: True', 'Breaking: True', 'Avionics: True', 'Landing: True']
'''
