def rgb_to_hsl(r, g, b):
    # Normalize RGB to [0, 1]
    r /= 255
    g /= 255
    b /= 255

    max_val = max(r, g, b)
    min_val = min(r, g, b)
    delta = max_val - min_val

    # Calculate Lightness
    l = (max_val + min_val) / 2

    # Calculate Saturation
    if delta == 0:
        s = 0
    else:
        s = delta / (1 - abs(2 * l - 1))

    # Calculate Hue
    if delta == 0:
        h = 0
    elif max_val == r:
        h = (g - b) / delta % 6
    elif max_val == g:
        h = (b - r) / delta + 2
    elif max_val == b:
        h = (r - g) / delta + 4

    h *= 60
    if h < 0:
        h += 360

    return [round(h, 2), round(s, 2), round(l, 2)]


def hsl_to_rgb(h, s, l):
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    elif 300 <= h < 360:
        r, g, b = c, 0, x

    # Convert to [0, 255] range
    r = round((r + m) * 255)
    g = round((g + m) * 255)
    b = round((b + m) * 255)

    return [r, g, b]


if __name__ == "__main__":
    # Example usage:
    rgb = (255, 100, 50)
    hsl = rgb_to_hsl(*rgb)
    #hsl[1] /= 2
    print("HSL:", hsl)

    rgb_converted = hsl_to_rgb(*hsl)
    print("RGB:", rgb_converted)
