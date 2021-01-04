1637 Widest Vertical Area Between Two Points Containing No Points
---
__Difficulty:__ Medium

Description
---
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

Solution
---
In my opinion this isn't a very good question. One can totally ignore the `y`-component and achieve the correct results. But - just sort by the `x`-component, then iterate through adjacent pairs, updating the current max distance as you go.
