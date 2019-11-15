# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.
    Параметры:
    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        if r != 0:
            body.Fx += (-1)*((obj.m * body.m * gravitational_constant)/(r**2)) * ((body.x - obj.x)/r)
            body.Fy += (-1)*((obj.m * body.m * gravitational_constant)/(r**2)) * ((body.y - obj.y)/r)


def move_space_object(body, dt, t_const):
    """Перемещает тело в соответствии с действующей на него силой.
    Параметры:
    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx/body.m
    ay = body.Fy/body.m
    body.Vx += ax*dt*t_const
    body.Vy += ay*dt*t_const
    body.x += body.Vx*dt*t_const
    body.y += body.Vy*dt*t_const


def recalculate_space_objects_positions(space_objects, dt, t_const):
    """Пересчитывает координаты объектов.
    Параметры:
    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt, t_const)


if __name__ == "__main__":
    print("This module is not for direct call!")