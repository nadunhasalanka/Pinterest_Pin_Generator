
def image_generator(project_folder, mode ):
    from modules.base import Pinterest
    from modules.image_generator import Template1ImageGenerator, Template2ImageGenerator

    base = Pinterest(project_folder)

    data = base.open_csv(base.GENERATOR_DATA_FILE)

    common_params = {
        'width': 1000,
        'height': 1500,
        'save': True,
        'show': False,
        'write_uploading_data': True
    }

    #Dictionary mapping generation mode to generator class
    generators = {
        base.GENERATOR_MODE_1: Template1ImageGenerator,
        base.GENERATOR_MODE_2: Template2ImageGenerator,
    }

    # check if hte specified mode is in the generators dictionary
    if mode in generators:
        # Get the generator class for the specified mode
        generator_class = generators[mode]
        # Create an instance of the generator
        generator = generator_class(project_folder, **common_params)
        for number, row in enumerate(data, start = 1):
            # Generate an image for each row
            generator.generate_image(row, number)
    else:
        # Raise an exception if the mode is invalid
        raise ValueError(f"Invalid mode: {mode}. Check the available modes in the base class.")



def writing(project_folder, mode):
    from modules.writer import Writer


    table_id = '' # Enter  Your Google sheet's Table ID

    writer = Writer(project_folder)

    data = writer.open_data(mode, google_sheet=True, table_id=table_id)

    for row in data:
        writer.write(row, mode)


if __name__ == '__main__':
    project_name = 'Keto'

    writer_modes = ['video', 'image']
    writing(project_name, writer_modes[1])

    generator_modes = ['template_1', 'template_2']
    image_generator(project_name, generator_modes[0])

