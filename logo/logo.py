import numpy as np

inner_radius = 0.2
outer_radius = 0.8
circle_radius = (256 - 8) / 256
half_angle_width = 0.15


def rotate(p, angle):
    c = np.cos(angle)
    s = np.sin(angle)
    x, y = p
    return c * x - s * y, s * x + c * y


def write_svg(color='#3498db', name='logo', size=1024):
    assert size % 2 == 0
    half_size = size // 2

    points = [
        (inner_radius, 0),
        rotate((outer_radius, 0), np.pi / 6 - half_angle_width),
        rotate((outer_radius, 0), np.pi / 6 + half_angle_width),
    ]
    angles = np.linspace(0, 2 * np.pi, 7)[:-1]

    points = [
        rotate(p, angle) for angle in angles for p in points
    ]
    points = np.array(points)

    path = [
        f'M {half_size + half_size * circle_radius} {half_size}',
        f'A {half_size * circle_radius} {half_size * circle_radius} 0 0 1 {half_size - half_size * circle_radius} {half_size}',
        f'A {half_size * circle_radius} {half_size * circle_radius} 0 0 1 {half_size + half_size * circle_radius} {half_size}',
        f'M {half_size + half_size * points[-1][0]} {half_size + half_size * points[-1][1]}'
    ]
    for x, y in points:
        path.append(f'L {half_size + half_size * x} {half_size + half_size * y}')
    path = ' '.join(path)

    svg = [
        f'<svg version="1.1" width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">',
        f'<path fill-rule="evenodd" fill="{color}" d="{path}"/>', f'</svg>'
    ]
    svg = '\n'.join(svg)

    with open(f'{name}.svg', 'w') as f:
        f.write(svg)

    # print('Command to generate logo.png:')
    # print(f'> PATH_TO_INKSCAPE -w {size} -h {size} logo.svg -o logo.png')


if __name__ == '__main__':
    write_svg(color='#3498db', name='logo', size=1024)
