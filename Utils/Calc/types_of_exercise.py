import numpy as np
from .body_part_angle import BodyPartAngle
from .utils import *

MIN_WALKING_DIST = 0.3

class TypeOfExercise():
    def __init__(self):
        # super().__init__(landmarks)
        self.max_walk_dist = MIN_WALKING_DIST
        print('typeofEx init')

    def push_up(self, counter, status):
        left_arm_angle = self.calcAngle.angle_of_the_left_arm()
        right_arm_angle = self.calcAngle.angle_of_the_right_arm()
        avg_arm_angle = (left_arm_angle + right_arm_angle) // 2
        if status:
            if avg_arm_angle < 70:
                counter += 1
                status = False
        else:
            if avg_arm_angle > 160:
                status = True

        return [counter, status]


    def pull_up(self, counter, status):
        left_wrist = detection_body_part(self.landmarks, "LEFT_WRIST")
        left_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER")
        if (left_wrist[1] > left_shoulder[1]): return [counter , status]

        left_arm_angle = self.calcAngle.angle_of_the_left_arm()
        right_arm_angle = self.calcAngle.angle_of_the_right_arm()
        avg_arm_angle = (left_arm_angle + right_arm_angle) // 2

        if status:
            if avg_arm_angle < 70:
                counter += 1
                status = False
        else:
            if avg_arm_angle > 160:
                status = True

        return [counter, status]

    def squat(self, counter, status):
        left_leg_angle = self.calcAngle.angle_of_the_right_leg()
        right_leg_angle = self.calcAngle.angle_of_the_left_leg()
        avg_leg_angle = (left_leg_angle + right_leg_angle) // 2

        if status:
            if avg_leg_angle < 70:
                counter += 1
                status = False
        else:
            if avg_leg_angle > 160:
                status = True

        return [counter, status]

    def walk(self, counter, status):
        #self.landmarks is now in IRL cords (center around hip's center)
        #X: Horizontal Axis
        #Y: Vertical Axis
        #Z: Depth Axis
        right_heel = get_body_part_cords(self.landmarks, "RIGHT_HEEL")
        left_heel = get_body_part_cords(self.landmarks, "LEFT_HEEL")
        dist = abs(right_heel[0] - left_heel[0])

        if (dist < MIN_WALKING_DIST): return [counter, status]

        if aprox_same_plane(right_heel, left_heel, 'y', 0.05):
            status = True
            if (dist > self.max_walk_dist): self.max_walk_dist = dist
        elif status:
            counter += self.max_walk_dist
            status = False
            self.max_walk_dist = 0
        return [counter, status]

    def sit_up(self, counter, status):
        angle = self.calcAngle.angle_of_the_abdomen()
        if status:
            if angle < 55:
                counter += 1
                status = False
        else:
            if angle > 105:
                status = True

        return [counter, status]

    def calculate_exercise(self, landmarks, exercise_type, counter, status):
        self.landmarks = landmarks
        self.calcAngle = BodyPartAngle(self.landmarks)
        if exercise_type == "push-up":
            counter, status = self.push_up(
                counter, status)
        elif exercise_type == "pull-up":
            counter, status = self.pull_up(
                counter, status)
        elif exercise_type == "squat":
            counter, status = self.squat(
                counter, status)
        elif exercise_type == "walk":
            counter, status = self.walk(
                counter, status)
        elif exercise_type == "sit-up":
            counter, status = self.sit_up(
                counter, status)

        return [counter, status]
