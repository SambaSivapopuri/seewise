def calculate_oee(production_logs):
    availability = performance = quality = 0
    available_time = 3 * 8 * 60  # 3 shifts, 8 hours each, in minutes
    ideal_cycle_time = 5  # minutes

    total_duration = sum([log.duration for log in production_logs])
    total_products = len(production_logs)
    good_products = sum([1 for log in production_logs if log.duration == ideal_cycle_time])
    bad_products = total_products - good_products

    available_operating_time = total_products * ideal_cycle_time
    unplanned_downtime = available_time - available_operating_time
    actual_output = total_products

    if available_time > 0:
        availability = ((available_time - unplanned_downtime) / available_time) * 100

    if available_operating_time > 0:
        performance = ((ideal_cycle_time * actual_output) / available_operating_time) * 100

    if total_products > 0:
        quality = (good_products / total_products) * 100

    oee = (availability * performance * quality) / 10000  # Adjust for percentage
    return {
        "availability": availability,
        "performance": performance,
        "quality": quality,
        "oee": oee
    }
