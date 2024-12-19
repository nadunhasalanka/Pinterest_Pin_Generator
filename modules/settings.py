from dataclasses import dataclass
from typing import Tuple

@dataclass
class Template1Settings:
    bg_color: str = '#7c95b3'
    random_bg_color: bool = False
    random_colors: Tuple[str] = ('darkslateblue', 'midnightblue', 'mediumpurple')
    overlay_bg: bool = True
    resize_bg: bool = True

    title_font_size: int = 80
    title_max_width: int = 900
    title_text_color_default: str = 'white'
    title_text_color_dark: str = 'black'
    title_line_spacing: int = 15
    title_margin_from_top: int = 50

    gradient: bool = False
    gradient_direction: int = 360

    tips_count: int = 4
    tips_font_size: int = 40
    tips_top_margin: int = 150
    tips_max_text_width: int = 700
    tips_left_margin: int = 150

    rectangle_top_padding: int = 15
    rectangle_bottom_padding: int = 15
    rectangle_horizontal_spacing: int = 30
    rectangle_horizontal_padding: int = 50
    rectangle_fill_color: str = '#fff9f1'
    rectangle_opacity: int = 200 #(0 - fully transparent, 255 - fully opaque)
    rectangle_corner_radius: int = 20
    rectangle_outline: str = '#fff9f1'
    rectangle_outline_width: int = 0
    tips_text_color: str = 'white'
    tips_line_spacing: int = 10
    margin_between_tips: int = 100
    tips_block_x_offset: int = 20

    circle_radius: int = 40
    circle_x_offset: int = -50
    circle_y_offset: int = 0
    circle_fill_color: str = '#c887ea'
    circle_opacity: int = 128 #(0 - fully transparent, 255 - fully opaque)
    circle_outline: str = 'grey'
    circle_outline_width: int = 0
    tips_number_font_size: int = 40
    circle_text_color: str = 'white'
    circle_text_x_offset: int = 0
    circle_text_y_offset: int = 0

    footer: bool = True
    footer_text: str = 'website.com'
    footer_font_size: int = 40
    footer_height: int = 100
    footer_fill_color: str = '#10563f'
    footer_opacity: int = 225
    footer_text_color: str = 'white'
    footer_text_y_offset: int = 0

@dataclass
class Template2Settings:
    bg_color: str = '#7c95b3'
    random_bg_color: bool = True
    random_colors: Tuple[str] = ('darkslateblue', 'midnightblue', 'mediumpurple')
    overlay_bg: bool = True
    resize_bg: bool = True

    gradient: bool = False
    gradient_direction: int = 360

    title_font_size: int = 90
    title_text_color: str = '#2b322d'
    title_line_spacing: int = 15
    title_max_width: int = 500
    title_y_offset: int = -100

    another_font: bool = True
    strings_with_another_font: int = 3
    another_text_top_padding: int = 40
    another_text_font_size: int = 100
    another_text_color: str = 'purple'
    another_text_line_spacing: int = 0

    rectangle_top_padding: int = 50
    rectangle_bottom_padding: int = 58
    rectangle_horizontal_padding: int = 50
    rectangle_fill_color: str = '#fff9f1'
    # rectangle_fill_color: str = '#a26f4b'
    rectangle_opacity: int = 158  #(0 - fully transparent, 255 - fully opaque)
    rectangle_outline: str = '#fff9f1'
    rectangle_outline_width: int = 0
    rectangle_corner_radius: int = 20

    footer: bool = True
    footer_text: str = 'website.com'
    footer_font_size: int = 40
    footer_height: int = 100
    footer_fill_color: str = '#221f1a'
    footer_opacity: int = 225
    footer_text_color: str = 'white'
    footer_text_y_offset: int = 0





