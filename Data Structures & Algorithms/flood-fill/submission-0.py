class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startcolor = image[sr][sc]

        def helper(image, sr, sc, color, startcolor):
            rows, cols = len(image), len(image[0])
            if(min(sr,sc) < 0 or sr == rows or sc == cols or image[sr][sc] != startcolor):
                return
            if image[sr][sc] == startcolor:
                image[sr][sc] = color
            
            helper(image, sr + 1, sc, color, startcolor)
            helper(image, sr - 1, sc, color, startcolor)
            helper(image, sr, sc + 1, color, startcolor)
            helper(image, sr, sc - 1, color, startcolor)

        if startcolor == color:
            return image
        helper(image, sr, sc, color, startcolor)
        return image