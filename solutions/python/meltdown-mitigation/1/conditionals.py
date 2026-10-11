"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    return (
        temperature < 800 
        and neutrons_emitted > 500 
        and temperature * neutrons_emitted < 500000
    )


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    power_output_percentage = (generated_power/theoretical_max_power) * 100

    if power_output_percentage >= 80:
        return 'green'
    elif power_output_percentage >= 60:
        return 'orange'
    elif power_output_percentage >= 30:
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if (temperature * neutrons_produced_per_second) < (0.9 * threshold):
        return 'LOW'
    elif (temperature * neutrons_produced_per_second) < (1.1 * threshold) and (temperature * neutrons_produced_per_second) > (0.9 * threshold):
        return 'NORMAL'
    else:
        return 'DANGER'
