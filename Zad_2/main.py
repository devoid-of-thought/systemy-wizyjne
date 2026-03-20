import cv2
import numpy as np
def img_from_cl():
    path = input("Podaj ścieżkę do pliku: ")
    return path
def matrix_dim_from_cl():
    dim = int(input("Podaj wymiar macierzy: 2n+1 "))
    if dim % 2 == 0:
        print("Wymiar macierzy musi być nieparzysty.")
        return None
    return dim
def matrix_values_from_cl(dim):
    matrix = []
    print(f"Podaj wartości macierzy {dim}x{dim}:")
    curr_row = 0
    while True:
        row = list(map(float, input(f"Wiersz {curr_row+ 1}: ").split()))
        if len(row) != dim:
            print(f"Musisz podać dokładnie {dim} wartości.")
            continue
        elif curr_row == dim - 1:
            matrix.append(row)
            break
        else:
            curr_row +=1
            matrix.append(row)

    return np.array(matrix, dtype=np.float32)

def main():
    path = img_from_cl()
    dim = matrix_dim_from_cl()
    if dim is None:
        return

    image = cv2.imread(path)
    if image is None:
        print("Nie można wczytać obrazu. Sprawdź ścieżkę.")
        return

    kernel = matrix_values_from_cl(dim)
    blur = cv2.filter2D(image, -1, kernel)

    cv2.imshow("Obraz poddany filtracji", blur)
    cv2.imwrite("pawian Mariusz - poddany filtracji.jpg", blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
        main()