# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import filter_class

path = '3.png'

Image_origin = filter_class.Filter(path).image

Image_1 = filter_class.FIND_EDGES_Filter(path)
Image_1 = Image_1.filter(Image_origin)
Image_2 = filter_class.EDGE_ENHANCE_Filter(path)
Image_2 = Image_2.filter(Image_origin)
Image_3 = filter_class.GaussianBlur_Filter(path)
Image_3 = Image_3.filter(Image_origin)

Image_4 = filter_class.new_Filter(path,0.5,0.5)
Image_4 = Image_4.filter(Image_origin)

Image_origin.show()
Image_1.show()
Image_2.show()
Image_3.show()
Image_4.show()