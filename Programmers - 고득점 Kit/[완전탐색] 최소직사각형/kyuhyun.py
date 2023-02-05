def solution(sizes):

    row = []
    col = []

    for i in range(len(sizes)):
        row.append(sizes[i][0])
        col.append(sizes[i][1])

        answer = max(row) * max(col)

        row[i], col[i] = col[i], row[i]

        if answer < max(col) * max(row):
             row[i], col[i] = col[i], row[i]

    return max(row) * max(col)
