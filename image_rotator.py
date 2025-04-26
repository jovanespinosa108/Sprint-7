
# inicializa el analizador sint�ctico
parser = argparse.ArgumentParser()

# agrega argumentos con sus nombres correspondientes
parser.add_argument('input_file')
parser.add_argument('output_file')
# observa que a continuaci�n usamos opciones y el valor predeterminado para esta opci�n
parser.add_argument('--angle', '-a', type=int, default=90)

# analiza los argumentos
args = parser.parse_args()

# carga una imagen del argumento input_file
im = Image.open(args.input_file)

# muestra el tama�o de la imagen
print(im.size)

# gira la imagen en un �ngulo proporcionado como argumento
rotated = im.rotate(args.angle)

# guarda la imagen girada usando la ruta de salida de un argumento output_file
rotated.save(args.output_file)
