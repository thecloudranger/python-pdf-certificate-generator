# Import necessary libraries
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Function to create certificate
def create_certificate(name):
    # Load the template image
    template = Image.open('aws_community_day_certificate.jpg')
    
    # Create a drawing context
    draw = ImageDraw.Draw(template)
    
    # Define font and size
    # font = ImageFont.load_default()
    font = ImageFont.truetype(font='OpenSans-VariableFont_wdth,wght.ttf', size=60)
    
    # calculate length of name
    name_length = len(name)
    
    # If name is longer than 15 characters, wrap it
    if name_length > 20:
        wrapped_text = textwrap.fill(name, width=20)
        draw.multiline_text((710, 540), wrapped_text, font=font, fill='#ff9800', align='center')
    # If name is shorter than 15 characters, don't wrap it
    else:
        draw.text((810, 540), name, font=font, fill='#ff9800', align='center')

    
    # Save the certificate as a PDF with the name
    certificate_filename = f'{name}_certificate.pdf'
    template.save(certificate_filename)

create_certificate("Mohammed Fazalullah Qudrath")
