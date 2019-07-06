import cv2


def rectangle_center(top_left, bottom_right):
    x_center = (top_left[0] + bottom_right[0]) // 2
    y_center = (top_left[1] + bottom_right[1]) // 2
    return x_center, y_center


class Converter:
    @staticmethod
    def convert_to_gray(img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


class ThresholdFilter:
    @staticmethod
    def apply_threshold(img, threshold_value=200, max_val=255, style=cv2.THRESH_BINARY):
        _, img = cv2.threshold(img, threshold_value, max_val, style)
        return img


class TemplateMatcher:
    def __init__(self, image_path, template_path):
        self.img = cv2.imread(image_path, 1)
        self.template = cv2.imread(template_path, 1)

    def template_rectangle(self):
        img, template = map(Converter.convert_to_gray, (self.img, self.template))
        img, template = map(ThresholdFilter.apply_threshold, (img, template))

        w, h = template.shape[::-1]

        template = cv2.blur(template, (2, 2))

        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        return top_left, bottom_right
