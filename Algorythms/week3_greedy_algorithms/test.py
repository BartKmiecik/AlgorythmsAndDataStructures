def black_balls(amount:int, boxes:int):
    list_of_boxes = [amount]
    for i in range(1,boxes):
        list_of_boxes[0] -= i
        list_of_boxes.append(i)
    print(list_of_boxes)


def black_balls2(amount:int, boxes:int):
    list_of_boxes = [amount]
    for i in range(1, boxes):
        if i % 2 == 1:
            list_of_boxes[0] -= i%2
            list_of_boxes.append(i%2)
        else:
            list_of_boxes[0] -= i
            list_of_boxes.append(i)
    print(list_of_boxes)


if __name__ == '__main__':
    black_balls2(30, 10)