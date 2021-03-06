# InterviewAlgorithmPractice
剑指offer第二版题目练习

#### 面试题03：找出数组中重复的数字 [(练习)](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof)

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
```
输入:
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
```
限制：
2 <= n <= 100000


#### 面试题04: 二维数组中的查找 [(练习)](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof)
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:
```
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

给定 target = 5，返回 true。
给定 target = 20，返回 false。
```

限制：

0 <= n <= 1000
0 <= m <= 1000

Note: 比较右上角的数

#### 面试题05: 替换空格 [(练习)](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof)
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
```
输入：s = "We are happy."
输出："We%20are%20happy."
 ```
限制：
0 <= s 的长度 <= 10000

Note: 从后往前复制以避免覆盖，减少移动次数增加效率

#### 面试题06. 从尾到头打印链表 [(练习)](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
```
输入：head = [1,3,2]
输出：[2,3,1]
``` 

限制：
0 <= 链表长度 <= 10000

#### 面试题07: 重建二叉树 [(练习)](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/)
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

示例 1：
```
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
``` 

限制：
0 <= 节点个数 <= 5000

#### 面试题08：二叉查找树迭代器 [(练习)](https://leetcode.com/problems/binary-search-tree-iterator/)
设计实现一个带有下列属性的二叉查找树的迭代器：
next()返回BST中下一个最小的元素

元素按照递增的顺序被访问（比如中序遍历）
next()和hasNext()的询问操作要求均摊时间复杂度是O(1)

样例 1:
```
输入：{10,1,11,#,6,#,12}
输出：[1, 6, 10, 11, 12]
解释：
二叉查找树如下 :
  10
  /\
 1 11
  \  \
   6  12
可以返回二叉查找树的中序遍历 [1, 6, 10, 11, 12]
```
样例 2:
```
输入：{2,1,3}
输出：[1,2,3]
解释：
二叉查找树如下 :
  2
 / \
1   3
可以返回二叉查找树的中序遍历 [1,2,3]
```

#### 面试题09: 用两个栈实现队列 [(练习)](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
```
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
```

示例 2：
```
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
```
提示：
- 1 <= values <= 10000
- 最多会对 appendTail、deleteHead 进行 10000 次调用
