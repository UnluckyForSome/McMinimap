from pathlib import Path
import os
from mgz.summary import Summary
from PIL import Image
from PIL import ImageDraw, ImageOps
import math

import McMinimapData # type: ignore
player_colors = McMinimapData.player_colors
tiles_colors = McMinimapData.tiles_colors
wall_objects = McMinimapData.wall_objects
food_objects = McMinimapData.food_objects
stone_objects = McMinimapData.stone_objects
gold_objects = McMinimapData.gold_objects
relic_objects = McMinimapData.relic_objects
cliff_objects = McMinimapData.cliff_objects

# Settings (you need to update these)
module_mode = False                                                                                                                      # Module mode allows you to call on this script from elsewhere and return a map. Leave this False otherwise.
manual_replay_file_path =  os.path.join(os.path.dirname(__file__), "MP Replay v101.102.52940.0 @2024.08.01 233627 (3).aoe2record")       # The AOE2 replay file to use if module_mode is False.
manual_canvas_save_file_path =  os.path.join(os.path.dirname(__file__))                                                                  # Manual base path for saving the canvas
object_mode = "square"                                                                                                                   # Options are "rotated" and "square". Determines if objects are drawn before or after canvas rotation.
player_tc_marker = "emblem"                                                                                                              # Options are "pixel" and "emblem".
angle = 45                                                                                                                               # Angle the map is drawn at. AOE2's default style is 45.
multiplier_integer = 9                                                                                                                   # UnluckyForSome... Multiplier for the size of the minimap. Higher = more pixels per map. Even numbers mean tiles can never be explicit.
orthographic_ratio = 2                                                                                                                   # When veiwed at a 45 degree angle, this is the "tilt" of the map. AOE2's style is 2.
border_spacing = 4                                                                                                                       # Spacing around the map. Fill it with an optional border

draw_cliffs = True                                                                                                                       # Draw cliffs
draw_walls = True                                                                                                                        # Draw walls

draw_player_objects = False                                                                                                              # Draw player objects
draw_gaia_objects = True                                                                                                                 # Draw gaia objects


# Global variables for extra pixel layer around coords. Setting these to the same as the multiplier_integer will effectively double the size
additional_cliff_size = 1
additional_player_wall_size = 1

additional_relic_size = 4
additional_stone_size = 4
additional_gold_size = 4
additional_food_size = 4
additional_player_object_size = 20
additional_player_tc_size = 40

print("Started in module mode: " + str(module_mode))

# To be honest this got so complicated I don't even know quite how it works, but it does
def rotate_coordinates(pixel_coordinates_x, pixel_coordinates_y, original_map_dimension, new_canvas_dimension, performed_after_enlargement):
    mi = multiplier_integer

    # Step 1: Translate pixel coordinates to be relative to the center of the map
    x_centered = pixel_coordinates_x - (original_map_dimension / 2)
    y_centered = pixel_coordinates_y - (original_map_dimension / 2)

    # Step 2: Apply rotation using the given angle
    x_transformed = x_centered * math.cos(math.radians(-angle)) - y_centered * math.sin(math.radians(-angle))
    y_transformed = x_centered * math.sin(math.radians(-angle)) + y_centered * math.cos(math.radians(-angle))

    # Step 3: Translate the transformed coordinates to be relative to the center of the new canvas
    x_transformed += (new_canvas_dimension / 2)
    y_transformed += (new_canvas_dimension / 2)

    # Step 4: Check if we're applying mcinterger scaling
    if performed_after_enlargement is False:
        mi = 1

    # Step 5: Scale and translate the coordinates using the multiplier and adjust to fit the canvas
    x_transformed = (x_transformed * mi + (new_canvas_dimension - new_canvas_dimension * mi) / 2) 
    y_transformed = (y_transformed * mi + (new_canvas_dimension - new_canvas_dimension * mi) / 2) 

    # Step 6: Convert the transformed coordinates to integers and return the result
    return math.floor(x_transformed), math.floor(y_transformed)                               #######################################################################################################################################################################################



# Convert HEX to RGB
def to_rgb(farbe: str) -> tuple[int, int, int]:
    return tuple(int(farbe[i:i+2], 16) for i in (0, 2, 4))



# Get MGZ Summary
def get_mgz(input_file: str):
    with open(f'{input_file}', 'rb') as data:
        return Summary(data)



# Draw Terrain
def draw_terrain_straight(canvas, map):
    for i in range(map.dimension ** 2):
        x = map.tiles[i].position.x + border_spacing
        y = map.tiles[i].position.y + border_spacing
        terrain = map.tiles[i].terrain
 
        canvas.putpixel((x, y), to_rgb(tiles_colors[terrain]['normal'][1:]))


        # Elevation, only take tiles which have an ajoining bottom right tile
        if x < map.dimension + border_spacing - 1 and y < map.dimension + border_spacing - 1:

            bottom_right_tile = map.tiles[i+map.dimension+1]

            if bottom_right_tile.elevation < map.tiles[i].elevation:
                canvas.putpixel((x, y), to_rgb(tiles_colors[terrain]['sunny'][1:]))

            elif bottom_right_tile.elevation > map.tiles[i].elevation:
                canvas.putpixel((x, y), to_rgb(tiles_colors[terrain]['shady'][1:]))



def draw_permenant_objects(canvas, gaia, players):
    draw = ImageDraw.Draw(canvas)
    # Cliffs look nicer straight regardless of mode, so draw them here

    if draw_cliffs:
        for unit in gaia:
            if unit.object_id in cliff_objects:
                cliff_color = '#714b33'
                
                coords = (unit.position.x, unit.position.y)
                yooo = border_spacing
                coords = (coords[0] + yooo, coords[1] + yooo)
                size = (additional_cliff_size)


                left = coords[0] - size
                top = coords[1] - size

                right = coords[0] + (size)
                bottom = coords[1] + (size)

                draw.rectangle([left, top, right, bottom], fill=cliff_color)

    if draw_walls:
        for player in players:
            for unit in player.objects:
                if unit.object_id in wall_objects:

                    coords = (unit.position.x, unit.position.y)
                    yooo = border_spacing
                    coords = (coords[0] + yooo, coords[1] + yooo)
                    size = (additional_player_wall_size)

                    left = coords[0] - size
                    top = coords[1] - size

                    right = coords[0] + (size)
                    bottom = coords[1] + (size)

                    draw.rectangle([left, top, right, bottom], fill=to_rgb(player_colors[player.color_id][1:]))



# Drawn in reverse order of importance
def draw_gaia_objects_common(canvas, gaia, original_map_dimension, after_rotation):
    draw = ImageDraw.Draw(canvas)

    for unit in gaia:
        if unit.object_id in food_objects:
            food_color = '#A5C46C'
            
            if after_rotation:
                coords = rotate_coordinates((unit.position.x), (unit.position.y), original_map_dimension, canvas.height*orthographic_ratio, performed_after_enlargement=True)  ###################################################################################################################################
                coords = (coords[0], coords[1] / orthographic_ratio) # Divide y coord by orthographic ratio
                size = (math.floor(multiplier_integer / 2)) + (additional_food_size)
                offset = 1 if multiplier_integer % 2 == 0 else 0
            else:
                coords = (unit.position.x * multiplier_integer, unit.position.y * multiplier_integer)
                yooo = border_spacing * multiplier_integer
                coords = (coords[0] + yooo, coords[1] + yooo)
                size = (math.floor(multiplier_integer / 2)) + (additional_food_size)
                offset = 1 if multiplier_integer % 2 == 0 else 0

            left = coords[0] - size
            top = coords[1] - size

            right = coords[0] + (size - offset)
            bottom = coords[1] + (size - offset)

            draw.rectangle([left, top, right, bottom], fill=food_color)

    for unit in gaia:
        if unit.object_id in stone_objects:
            stone_color = '#919191'
            
            if after_rotation:
                coords = rotate_coordinates((unit.position.x), (unit.position.y), original_map_dimension, canvas.height*orthographic_ratio, performed_after_enlargement=True)  ###################################################################################################################################
                coords = (coords[0], coords[1] / orthographic_ratio) # Divide y coord by orthographic ratio
                size = (math.floor(multiplier_integer / 2)) + (additional_stone_size)
                offset = 1 if multiplier_integer % 2 == 0 else 0
            else:
                coords = (unit.position.x * multiplier_integer, unit.position.y * multiplier_integer)
                yooo = border_spacing * multiplier_integer
                coords = (coords[0] + yooo, coords[1] + yooo)
                size = (math.floor(multiplier_integer / 2)) + (additional_stone_size)
                offset = 1 if multiplier_integer % 2 == 0 else 0

            left = coords[0] - size
            top = coords[1] - size

            right = coords[0] + (size - offset)
            bottom = coords[1] + (size - offset)

            draw.rectangle([left, top, right, bottom], fill=stone_color)

    for unit in gaia:
        if unit.object_id in gold_objects:
            gold_color = '#FFC700'
            
            if after_rotation:
                coords = rotate_coordinates((unit.position.x), (unit.position.y), original_map_dimension, canvas.height*orthographic_ratio, performed_after_enlargement=True)  ###################################################################################################################################
                coords = (coords[0], coords[1] / orthographic_ratio) # Divide y coord by orthographic ratio
                size = (math.floor(multiplier_integer / 2)) + (additional_gold_size)
                offset = 1 if multiplier_integer % 2 == 0 else 0
            else:
                coords = (unit.position.x * multiplier_integer, unit.position.y * multiplier_integer)
                yooo = border_spacing * multiplier_integer
                coords = (coords[0] + yooo, coords[1] + yooo)
                size = (math.floor(multiplier_integer / 2)) + (additional_gold_size)
                offset = 1 if multiplier_integer % 2 == 0 else 0

            left = coords[0] - size
            top = coords[1] - size

            right = coords[0] + (size - offset)
            bottom = coords[1] + (size - offset)

            draw.rectangle([left, top, right, bottom], fill=gold_color)

    for unit in gaia:
        if unit.object_id in relic_objects:
            relic_color = '#FFFFFF'
            
            if after_rotation:
                coords = rotate_coordinates((unit.position.x), (unit.position.y), original_map_dimension, canvas.height*orthographic_ratio, performed_after_enlargement=True)  ###################################################################################################################################
                coords = (coords[0], coords[1] / orthographic_ratio) # Divide y coord by orthographic ratio
                size = (math.floor(multiplier_integer / 2)) + (additional_relic_size)
                offset = 1 if multiplier_integer % 2 == 0 else 0
            else:
                coords = (unit.position.x * multiplier_integer, unit.position.y * multiplier_integer)
                yooo = border_spacing * multiplier_integer
                coords = (coords[0] + yooo, coords[1] + yooo)
                size = (math.floor(multiplier_integer / 2)) + (additional_relic_size)
                offset = 1 if multiplier_integer % 2 == 0 else 0

            left = coords[0] - size
            top = coords[1] - size

            right = coords[0] + (size - offset)
            bottom = coords[1] + (size - offset)

            draw.rectangle([left, top, right, bottom], fill=relic_color)



def draw_player_objects_common(canvas, players, original_map_dimension, after_rotation):
    draw = ImageDraw.Draw(canvas)

    for player in players:
        for unit in player.objects:
            if unit.class_id != 80 or unit.object_id not in wall_objects:
                if after_rotation:
                    coords = rotate_coordinates((unit.position.x), (unit.position.y), original_map_dimension, canvas.height*orthographic_ratio, performed_after_enlargement=True)  ###################################################################################################################################
                    coords = (coords[0], coords[1] / orthographic_ratio) # Divide y coord by orthographic ratio
                    size = (math.floor(multiplier_integer / 2)) + (additional_player_object_size)
                    offset = 1 if multiplier_integer % 2 == 0 else 0
                else:
                    coords = (unit.position.x * multiplier_integer, unit.position.y * multiplier_integer)
                    yooo = border_spacing * multiplier_integer
                    coords = (coords[0] + yooo, coords[1] + yooo)
                    size = (math.floor(multiplier_integer / 2)) + (additional_player_object_size)
                    offset = 1 if multiplier_integer % 2 == 0 else 0

                left = coords[0] - size
                top = coords[1] - size

                right = coords[0] + (size - offset)
                bottom = coords[1] + (size - offset)

                draw.rectangle([left, top, right, bottom], fill=to_rgb(player_colors[player.color_id][1:]))



def draw_player_walls_common(canvas, players, original_map_dimension, after_rotation):
    draw = ImageDraw.Draw(canvas)

    for player in players:
        for unit in player.objects:
            if unit.object_id in wall_objects:
                if after_rotation:
                    coords = rotate_coordinates((unit.position.x), (unit.position.y), original_map_dimension, canvas.height*orthographic_ratio, performed_after_enlargement=True)  ###################################################################################################################################
                    coords = (coords[0], coords[1] / orthographic_ratio) # Divide y coord by orthographic ratio
                    size = (math.floor(multiplier_integer / 2)) + (additional_player_wall_size)
                    offset = 1 if multiplier_integer % 2 == 0 else 0
                else:
                    coords = (unit.position.x * multiplier_integer, unit.position.y * multiplier_integer)
                    yooo = border_spacing * multiplier_integer
                    coords = (coords[0] + yooo, coords[1] + yooo)
                    size = (math.floor(multiplier_integer / 2)) + (additional_player_wall_size)
                    offset = 1 if multiplier_integer % 2 == 0 else 0

                left = coords[0] - size
                top = coords[1] - size

                right = coords[0] + (size - offset)
                bottom = coords[1] + (size - offset)

                draw.rectangle([left, top, right, bottom], fill=to_rgb(player_colors[player.color_id][1:]))



def draw_player_tcs(canvas, players, original_map_dimension, after_rotation):
    draw = ImageDraw.Draw(canvas)

    for player in players:
        position = player.position  # Get the player's position object
        if player.position.x is None or player.position.y is None:  # Skip for maps like Nomad
            continue
        if after_rotation:
            coords = rotate_coordinates(position.x, position.y, original_map_dimension, canvas.height * orthographic_ratio, performed_after_enlargement=True)
            coords = (coords[0], coords[1] / orthographic_ratio)
            size = (math.floor(multiplier_integer / 2)) + (additional_player_tc_size)
            offset = 1 if multiplier_integer % 2 == 0 else 0
        else:
            coords = (position.x * multiplier_integer, position.y * multiplier_integer)
            yooo = border_spacing * multiplier_integer
            coords = (coords[0] + yooo, coords[1] + yooo)
            size = (math.floor(multiplier_integer / 2)) + (additional_player_tc_size)
            offset = 1 if multiplier_integer % 2 == 0 else 0

        left = coords[0] - size
        top = coords[1] - size

        right = coords[0] + (size - offset)
        bottom = coords[1] + (size - offset)

        draw.rectangle([left, top, right, bottom], fill=to_rgb(player_colors[player.color_id][1:]))



def create_border_canvas(original_map_dimension):

    # Do every action we've done to the main canvas up to this point:
    border_canvas = Image.new("RGBA", (original_map_dimension, original_map_dimension))

    # Draw the border
    draw = ImageDraw.Draw(border_canvas)
    draw.rectangle(
        [(0, 0), (border_canvas.width - 1, border_canvas.height - 1)],
        outline="rgb(0, 0, 0)",  # Border color
        width=1
    )

    draw.rectangle(
        [(1, 1), (border_canvas.width - 2, border_canvas.height - 2)],
        outline="rgb(157, 135, 114)",  # Border color
        width=1
    )
    
    draw.rectangle(
        [(2, 2), (border_canvas.width - 3, border_canvas.height - 3)],
        outline="rgb(215, 182, 151)",  # Border color
        width=1
    )

    draw.rectangle(
        [(3, 3), (border_canvas.width - 4, border_canvas.height - 4)],
        outline="rgb(31, 31, 31)",  # Border color
        width=1
    )

    # Do everything we subsequently do to the original canvas, but on the border canvas
    border_canvas = border_canvas.resize(((original_map_dimension + border_spacing * 2) * multiplier_integer, (original_map_dimension + border_spacing * 2) * multiplier_integer), resample=Image.Resampling.NEAREST)
    border_canvas = border_canvas.rotate(angle, resample=Image.Resampling.BILINEAR, expand=True)
    border_canvas = border_canvas.resize((border_canvas.size[0], border_canvas.size[1] // orthographic_ratio), resample=Image.Resampling.LANCZOS)
    return border_canvas



def new_canvas(original_map_dimension):
    canvas = Image.new('RGBA', (original_map_dimension + 2 * border_spacing, original_map_dimension + 2 * border_spacing))
    return canvas



def create_transparency_mask(canvas):
    # Create a mask for transparent pixels
    transparency_mask = Image.new('L', canvas.size, 0)
    for x in range(canvas.width):
        for y in range(canvas.height):
            if canvas.getpixel((x, y))[3] == 0:
                transparency_mask.putpixel((x, y), 255)
    return transparency_mask


    
def generate_minimap(input_file):
    print(f'Input file: {input_file}')
    summary = get_mgz(input_file)
    map = summary.match.map
    players = summary.match.players
    gaia = summary.match.gaia
    original_map_dimension = map.dimension

    # Create a canvas the same pixel size as the AOE2 map tile dimensions
    canvas = new_canvas(original_map_dimension)

    # Draw the terrain - including cliffs - 1 to 1 on the canvas
    draw_terrain_straight(canvas, map)

    draw_permenant_objects(canvas, gaia, players)

    # Resize the canvas with nearest neighbour by the multiplier integer, incorporating the border spacing
    canvas = canvas.resize(((original_map_dimension + border_spacing * 2) * multiplier_integer, (original_map_dimension + border_spacing * 2) * multiplier_integer), resample=Image.Resampling.NEAREST)


    if object_mode == "rotated":
        
        # Object drawing happens before post-resize canvas processing
        
        if draw_gaia_objects:
            draw_gaia_objects_common(canvas, gaia, original_map_dimension, after_rotation=False)

        if draw_player_objects:
            draw_player_objects_common(canvas, players, original_map_dimension, after_rotation=False)

        if draw_walls:
            draw_player_walls_common(canvas, players, original_map_dimension, after_rotation=False)

        if player_tc_marker == "pixel":
            draw_player_tcs(canvas, players, original_map_dimension, after_rotation=False)

        canvas = canvas.rotate(angle, resample=Image.Resampling.BILINEAR, expand=True)
        canvas = canvas.resize((canvas.size[0], canvas.size[1] // orthographic_ratio), resample=Image.Resampling.LANCZOS)

    if object_mode == "square":



        canvas = canvas.rotate(angle, resample=Image.Resampling.BILINEAR, expand=True)
        canvas = canvas.resize((canvas.size[0], canvas.size[1] // orthographic_ratio), resample=Image.Resampling.LANCZOS)
        
        original_canvas = canvas.copy()
        transparency_mask = create_transparency_mask(original_canvas)


        # Object drawing happens after post-resize canvas processing

        if draw_gaia_objects:
            draw_gaia_objects_common(canvas, gaia, original_map_dimension, after_rotation=True)

        if draw_player_objects or any((player.position.x is None or player.position.y is None) for player in players):
            draw_player_objects_common(canvas, players, original_map_dimension, after_rotation=True)

        if draw_walls:
            draw_player_walls_common(canvas, players, original_map_dimension, after_rotation=True)

        if player_tc_marker == "pixel":
            draw_player_tcs(canvas, players, original_map_dimension, after_rotation=True)

        # Paste the transparency mask onto the canvas, restoring original transparent areas
        canvas.paste(original_canvas, mask=transparency_mask)


    border_canvas = create_border_canvas(original_map_dimension)

    if player_tc_marker == "emblem":
        civ_emblem_canvas = create_civ_icon_canvas(players, original_map_dimension)
        canvas.paste(civ_emblem_canvas, civ_emblem_canvas)

    # Paste the border canvas over the top of the canvas
    canvas.paste(border_canvas, border_canvas)

    canvas = canvas.resize((1630, 815), resample=Image.Resampling.LANCZOS)  # Adjust the size here
    #canvas = canvas.resize((2242, 1121), resample=Image.Resampling.LANCZOS)  # Adjust the size here



    if module_mode is False:
        canvas.save(f"{manual_canvas_save_file_path}/Manual Output.png")
        print("Done!")



    if module_mode is True:
        return canvas



def create_civ_icon_canvas(players, original_map_dimension):

    # Do every action we've done to the main canvas up to this point:
    civ_emblem_canvas = new_canvas(original_map_dimension)

    civ_emblem_canvas = civ_emblem_canvas.resize(((original_map_dimension + border_spacing * 2) * multiplier_integer, (original_map_dimension + border_spacing * 2) * multiplier_integer), resample=Image.Resampling.NEAREST)

    civ_emblem_canvas = civ_emblem_canvas.rotate(angle, resample=Image.Resampling.BILINEAR, expand=True)

    # Create a new Image object for the seperate canvas
    for player in players:
        position = player.position  # Get the player's position object
        if player.position.x is None or player.position.y is None:  # Skip for maps like Nomad
            continue
        coords = rotate_coordinates(position.x, position.y, original_map_dimension, civ_emblem_canvas.height, performed_after_enlargement=True)

        # Load the civ.png image
        civ_image = Image.open(os.path.join(os.path.dirname(__file__)) + "/emblems/" + player.civilization + ".png")

        

        # Calculate the top-left corner of the image based on the specified coordinates and the image size
        image_width, image_height = civ_image.size
        top_left_coords = (math.floor(coords[0] - image_width / 2), math.floor(coords[1] - image_height / 2))


        # Create an ImageDraw object for the seperate canvas
        draw = ImageDraw.Draw(civ_emblem_canvas)

        radius = max(image_width, image_height) / 2 + additional_player_tc_size



        # Calculate the center of the circle
        center = (top_left_coords[0] + image_width / 2, top_left_coords[1] + image_height / 2)

        # Draw a circle around the image on the seperate canvas
        draw.ellipse([(center[0] - radius, center[1] - radius), (center[0] + radius, center[1] + radius)], outline= (0, 0, 0), fill=to_rgb(player_colors[player.color_id][1:]), width=2)

        # Paste the civ.png image onto the seperate canvas at the calculated top-left coordinates
        civ_emblem_canvas.paste(civ_image, top_left_coords, civ_image)


    # Do everything we subsequently do to the original canvas, but on the civ icon canvas
    civ_emblem_canvas = civ_emblem_canvas.resize((civ_emblem_canvas.size[0], civ_emblem_canvas.size[1] // orthographic_ratio), resample=Image.Resampling.LANCZOS)
    return civ_emblem_canvas

    # Now, you can paste the seperate canvas onto another canvas if needed
    # For example, if 'final_canvas' is the target canvas:
    # final_canvas.paste(civ_emblem_canvas, (0, 0), civ_emblem_canvas)



if module_mode is False:
    generate_minimap(manual_replay_file_path)