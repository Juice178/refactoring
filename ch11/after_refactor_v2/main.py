from shape import Shape


def main() -> None:
    line = Shape.create_line(Shape.TYPECODE_LINE, 0, 0, 100, 200)
    rectangle= Shape.create_rectangle(Shape.TYPECODE_RECTANGLE, 10, 20, 30, 40)
    oval = Shape.create_oval(Shape.TYPECODE_OVAL, 100, 200, 300, 400)

    shape = [line, rectangle, oval]
    for s in shape:
        s.draw()


if __name__ == '__main__':
    main()