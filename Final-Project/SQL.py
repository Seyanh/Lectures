import os
import sqlite3
from PIL import Image

cats_dogs_List = ['dog', 'cat']

def read_images(imagefile="../Dataset/cat/"):
	img_dir = []
	files = os.listdir(imagefile)
	for file in files:
		img_dir.append(imagefile + file)
	return img_dir

def main():
	db = sqlite3.connect("DogvsCat.sqlite")
	cur = db.cursor()  # 获取数据库db的一系列操作cur

	for animal in cats_dogs_List:
		create_table = """
		CREATE TABLE {}(image LONGBOLB, label CHAR, width CHAR, length CHAR);
		""".format(animal)

		try:
			cur.execute(create_table)
			print("Create Table " + str(animal) + " succeed. \n")
		except:
			print("Table " + str(animal) + " already exist. \n")
			pass

		img_dir_list = read_images(imagefile="../Dataset/" + str(animal) + "/")

		for index, img_dir in enumerate(img_dir_list):
			print("No. {}".format(index))
			print("\tResize the img " + str(img_dir) + " and save as {}.png".format(index))

			img = Image.open(img_dir)
			image_resize = img.resize((128, 128), Image.ANTIALIAS)
			image_resize.save("../data/{}/{}.png".format(animal, str(index)))

			print("\tThe img " + str(img_dir) + " is loading to the sqlite.")
			with open("../data/{}/{}.png".format(animal, str(index)), "rb") as f:
				cur.execute("INSERT INTO {} VALUES(?,?,?,?)".format(animal), (f.read(), animal, "128", "128"))
				db.commit()

	cur.close()
	db.close()

if __name__ == "__main__":
	main()















