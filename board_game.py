from PIL import Image, ImageDraw,ImageFont

image = Image.new("RGB", (300, 300), "white")
draw = ImageDraw.Draw(image)



def draw_board(grid):
    square_size = 50

    for row in range(0, 300, square_size):
        for col in range(0, 300, square_size):
            if grid[row//square_size][col//square_size] == 1:
                draw.rectangle([col, row, col + square_size, row + square_size], fill="black",outline="white")
            elif grid[row//square_size][col//square_size] == 2 : 
                draw.rectangle([col,row,col+square_size,row+square_size],fill="yellow",outline="white")
            else:
                draw.rectangle([col, row, col + square_size, row + square_size], fill="white",outline="black")


def game_before(grid,inital,final) : 
    draw_board(grid)
    font = ImageFont.truetype("arial.ttf", 30)
    draw.rectangle([inital[0],inital[1],inital[0]+50,inital[1]+50],fill="green")
    draw.text((inital[0] + 15, inital[1] + 10), "S", fill="white", font=font)
    draw.rectangle([final[0],final[1],300,50],fill="red")
    draw.text((final[0] + 15,final[1] + 10), "E", fill="white", font=font)
    image.save("input_image.png")
    image.show()


def game_output(grid,inital,final) : 
    draw_board(grid)
    font = ImageFont.truetype("arial.ttf", 30)
    draw.rectangle([inital[0],inital[1],inital[0]+50,inital[1]+50],fill="green")
    draw.text((inital[0] + 15, inital[1] + 10), "S", fill="white", font=font)
    draw.rectangle([final[0],final[1],300,50],fill="red")
    draw.text((final[0] + 15,final[1] + 10), "E", fill="white", font=font)
    image.save("output_image.png")
    image.show()
