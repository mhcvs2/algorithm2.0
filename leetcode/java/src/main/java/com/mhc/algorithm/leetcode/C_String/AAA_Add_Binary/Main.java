package com.mhc.algorithm.leetcode.C_String.AAA_Add_Binary;

/*
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
*/

class Solution {

    public int char2Int(char i){
        return Integer.parseInt(String.valueOf(i));
    }

    public String buquan(String x, int nx, int n){
        for(int i=0; i<n-nx; i++){
            x = "0" + x;
        }
        return x;
    }

    public String addBinary(String a, String b) {
        int al = a.length();
        int bl = b.length();
        if(al > bl) {
            b = buquan(b, bl, al);
        } else {
            a = buquan(a, al, bl);
        }
        int max = Math.max(al, bl);
        int an, bn, sum;
        int[] res = new int[max+1];
        boolean jinwei = false;
        for(int i=max-1; i>=0; i--){
            an = char2Int(a.charAt(i));
            bn = char2Int(b.charAt(i));
            sum = an + bn;
            if(jinwei) sum += 1;
            System.out.println(sum);
            if(sum <= 1) {
                res[i] = sum;
                jinwei = false;
            } else if(sum == 2) {
                res[i] = 0;
                jinwei = true;
            } else {
                res[i] = 1;
                jinwei = true;
            }
        }
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<max; i++){
            sb.append(res[i]);
        }
        System.out.println(sb.toString());
        String rs;
        if(jinwei){
            rs = "1" + sb.toString();
        } else {
            rs = sb.toString();
        }
        return rs;
    }
}

public class Main {

    public static void main(String[] args) {

        Solution s = new Solution();

        System.out.println(s.addBinary("1010", "1011"));
    }

}