package com.mhc.algorithm.leetcode.B_Matrix.AAA_Rotate_Image;

/*
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
分析1
[0,0] -> [0,n-1]
[0,1] -> [1,n-1]
[a,b] -> [b,n-1-a]

分析2
00,01,...0n-2 ->
11,1n-3

起点[a,b]  终点[a,n-2-a]

分析3
以对角线旋转
00, n-1,n-1
01,n-2,n-1
a,b -> n-1-b, n-1-a
*/

class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int tmp;
        for(int i=0; i<n-1; i++){
            for(int j=0; j<n-1-i; j++){
                tmp = matrix[i][j];
                matrix[i][j] = matrix[n-1-j][n-1-i];
                matrix[n-1-j][n-1-i] = tmp;
            }
        }
        for(int i=0; i<n/2; i++){
            for(int j=0; j<n; j++){
                tmp = matrix[i][j];
                matrix[i][j] = matrix[n-1-i][j];
                matrix[n-1-i][j] = tmp;
            }
        }
    }

    public void rotate2(int[][] matrix) {
        int n = matrix.length;
        int tmp;
        for(int i=0; i<n/2; i++){
            for(int j=i; j<n-1-i; j++){
                tmp = matrix[i][j];
                matrix[i][j] = matrix[n-1-j][i];
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j];
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i];
                matrix[j][n-1-i] = tmp;
            }
        }
    }

    public void rotate1(int[][] matrix) {
        int n = matrix.length;
        int[][] res = new int[n][n];
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++) {
                res[j][n-1-i] = matrix[i][j];
            }
        }
        System.arraycopy(res, 0, matrix, 0, n);
    }
}

public class Main {

    public static void main(String[] args) {
        int[][] matrix = new int[][]{{1,2,3}, {4,5,6}, {7,8,9}};
        Solution s = new Solution();
        s.rotate(matrix);
        System.out.println(matrix);
    }

}