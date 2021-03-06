from django.db import models


class VehicleSpecs(models.Model):
    id = models.BigAutoField(primary_key=True)
    make_id = models.CharField(max_length=255, blank=True, null=True)
    make_display = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    trim = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    body = models.CharField(max_length=255, blank=True, null=True)
    engine_position = models.CharField(max_length=255, blank=True, null=True)
    engine_cc = models.IntegerField(blank=True, null=True)
    engine_cyl = models.IntegerField(blank=True, null=True)
    engine_type = models.CharField(max_length=255, blank=True, null=True)
    engine_valves_per_cyl = models.IntegerField(blank=True, null=True)
    engine_power_ps = models.CharField(max_length=255, blank=True, null=True)
    engine_power_rpm = models.IntegerField(blank=True, null=True)
    engine_torque_nm = models.CharField(max_length=255, blank=True, null=True)
    engine_torque_rpm = models.IntegerField(blank=True, null=True)
    engine_bore_mm = models.FloatField(blank=True, null=True)
    engine_stroke_mm = models.FloatField(blank=True, null=True)
    engine_compression = models.CharField(max_length=255, blank=True, null=True)
    engine_fuel = models.CharField(max_length=255, blank=True, null=True)
    top_speed_kph = models.IntegerField(blank=True, null=True)
    zero_to_100_kph = models.IntegerField(blank=True, null=True)
    drive = models.CharField(max_length=255, blank=True, null=True)
    drive2 = models.CharField(max_length=255, blank=True, null=True)
    seats = models.IntegerField(blank=True, null=True)
    seats2 = models.IntegerField(blank=True, null=True)
    weight_kg = models.IntegerField(blank=True, null=True)
    length_mm = models.FloatField(blank=True, null=True)
    width_mm = models.FloatField(blank=True, null=True)
    height_mm = models.FloatField(blank=True, null=True)
    wheelbase_mm = models.FloatField(blank=True, null=True)
    lkm_hwy = models.FloatField(blank=True, null=True)
    lkm_mixed = models.FloatField(blank=True, null=True)
    lkm_city = models.FloatField(blank=True, null=True)
    fuel_cap_l = models.IntegerField(blank=True, null=True)
    sold_in_us = models.NullBooleanField()
    co2 = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    forward_collision_warning = models.IntegerField(blank=True, null=True)
    adaptive_cruise_control = models.IntegerField(blank=True, null=True)
    lane_departure_warning = models.IntegerField(blank=True, null=True)
    lane_keeping_assist = models.IntegerField(blank=True, null=True)
    blind_spot_warning = models.IntegerField(blank=True, null=True)
    rear_cross_traffic_alert = models.IntegerField(blank=True, null=True)
    back_up_camera = models.IntegerField(blank=True, null=True)
    adaptive_headlights = models.IntegerField(blank=True, null=True)
    antilock_braking_system = models.IntegerField(blank=True, null=True)
    automatic_emergency_braking = models.IntegerField(blank=True, null=True)
    automatic_parallel_parking = models.IntegerField(blank=True, null=True)
    backup_warning = models.IntegerField(blank=True, null=True)
    biycle_detection = models.IntegerField(blank=True, null=True)
    blind_spot_monitoring = models.IntegerField(blank=True, null=True)
    brake_assist = models.IntegerField(blank=True, null=True)
    curve_speed_warning = models.IntegerField(blank=True, null=True)
    drowsiness_alert = models.IntegerField(blank=True, null=True)
    electronic_stability_control = models.IntegerField(blank=True, null=True)
    high_speed_alert = models.IntegerField(blank=True, null=True)
    hill_descent_assist = models.IntegerField(blank=True, null=True)
    hill_start_assist = models.IntegerField(blank=True, null=True)
    left_turn_crash_avoidance = models.IntegerField(blank=True, null=True)
    pedestrian_detection = models.IntegerField(blank=True, null=True)
    push_button_start = models.IntegerField(blank=True, null=True)
    sideview_camera = models.IntegerField(blank=True, null=True)
    temperature_warning = models.IntegerField(blank=True, null=True)
    tire_pressure_monitoring_system = models.IntegerField(blank=True, null=True)
    traction_control = models.IntegerField(blank=True, null=True)
    obstacle_detection = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_specs'
