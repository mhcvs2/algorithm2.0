package com.mhc.algorithm.leetcode.A_Array.AAA_3Sum;

/*
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
*/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {

    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int l = nums.length;
        int s, e, sum;
        boolean sn, en;
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        for(int i=0; i<l-2; i++){
            if(nums[i] > 0) {
                break;
            }
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }
            s = i+1;
            e = l-1;
            while (s<e){
                en = sn = false;
                sum = nums[i] + nums[s] + nums[e];
                if(sum == 0) {
                    res.add(Arrays.asList(nums[i], nums[s], nums[e]));
                    en = true;
                    sn = true;
                } else if (sum > 0){
                    en = true;
                } else {
                    sn = true;
                }
                if(en){
                    while (s<e && nums[e]==nums[e-1]) e--;
                    e--;
                }
                if(sn){
                    while (s<e && nums[s]==nums[s+1]) s++;
                    s++;
                }
            }
        }
        return res;
    }
}

public class Main {

    public static void main(String[] args) {

        Solution s = new Solution();

        System.out.println(s.threeSum(new int[]{-2,0,0,2,2}));
    }

}