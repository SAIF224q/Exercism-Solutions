"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500:
        if temperature * neutrons_emitted < 500000:
            return True
        else :
            return False
    else : 
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    power_efficiency = (generated_power/theoretical_max_power) * 100
    if power_efficiency >= 80:
        return "green"
    elif power_efficiency < 80 and power_efficiency >= 60:
        return "orange"
    elif power_efficiency < 60 and power_efficiency >=30:
        return "red"
    else :
        return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    threshold_90 = (90/100)*threshold
    threshold_10 = (10/100)*threshold + threshold
    criticality = temperature * neutrons_produced_per_second

    if criticality < threshold_90:
        return "LOW"
    elif criticality >= threshold_90 and criticality <= threshold_10:
        return "NORMAL"
    else:
        return "DANGER"
