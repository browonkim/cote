class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        result = ""
        columns = len(encodedText) // rows
        m = [[encodedText[x * columns + y] for y in range(columns)] for x in range(rows)]
        for col in range(columns-rows+2):
            for row in range(rows):
                if row+col >= columns:
                    break
                result += m[row][row+col]
        i = len(result) - 1
        while result[i] == " ":
            i -= 1
        result = result[:i+1]
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.decodeCiphertext(encodedText="iveo    eed   l te   olc",rows=4))
