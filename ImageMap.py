
class ImageMap:
    def __init__(self, _image_matrix):
        self.image_matrix = self.check_image_matrix(_image_matrix)

    def check_image_matrix(self, _image_matrix):
        assert len(_image_matrix) == 2