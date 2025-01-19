import colorgram

image_path = 'images/hirst_spot_painting.jpg'
colors = colorgram.extract(image_path, 32)
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
