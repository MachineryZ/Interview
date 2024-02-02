"""
正在设计一个自动驾驶的雷达系统，该雷达系统可以扫描到障碍物，随着车辆的行驶，障碍物有时会消失，
要求自动驾驶雷达系统有如何下的功能：
1. 需要有添加障碍物接口
2. 需要有弹出障碍物接口(FIFO)
3. 支持查看最近、最远、障碍物功能
4. 当车辆旋转时，可以变换障碍物坐标（支持90，180，270三种）
5. 当车辆行驶时，可以变换障碍物坐标（车头面向x轴方向）
6. 可以查看当前最近的障碍物距离为多少(因为避开障碍物是第一要素，所以要求 O(1)时间查询）

假设所有障碍物坐标是 int 类型的二维坐标，障碍物不会重复
问：这种 fifo 的形式是否有不合理的地方？（转弯，掉头，会导致 FIFO 的 obstacle 失效）
问：要怎么改进？换数据结构，不用queue这种模式
"""
#include <iostream>
#include <math>
#include <queue>

class RadarSystem {
private:
    std::queue<vector<int>> q;
    std::priority_queue<vector<int>, vector<vector<int>>, cmp> heap;


public:
    bool operator(const vector<int>& a, const vector<int>& b) {
        return a[0] * a[0] + a[1] * a[1] >= b[0] * b[0] + b[1] * b[1];
    }

    void scan(const vector<int>& obs) {
        if (obs.size() != 2) 
            throw std::invalid_argument("input obstacle size should be 2 size");
        q.push(obs);
        heap.push(obs);
        return;
    }

    void move(const int& x) {
        int qsize = q.size();
        for (int i = 0; i < qsize; i++) {
            vector<int> tmp = q.front();
            tmp[0] += x;
            q.pop();
            q.push(tmp);
        }
        for (int i = 0; i < qsize; i++) {
            vector<int> tmp = heap.top();
            tmp[0] += x;
            heap.pop();
            heap.push(tmp);
        }
    }

    void rotate(const int& rotate) {
        if (rotate != 0 or rotate != 1 or rotate != 2) // 0 - 90, 1 - 
            throw std::invalid_argument("rotate should be only 90, 180, 270 degree");
        int qsize = q.size();
        for (int i = 0; i < qsize; i++) {
            vector<int> tmp = q.front();
            if (rotate == 0) { // y = x, x = -y
                int x = tmp[0];
                tmp[0] = -tmp[1];
                tmp[1] = x;
            }
            else if (rotate == 1) { // y = -y, x = -x
                tmp[0] = -tmp[0];
                tmp[1] = -tmp[1];
            }
            else if (rotate == 2) { // y = -x, x = y
                int x = tmp[0];
                tmp[0] = -tmp[1];
                tmp[1] = x;
            }
            q.pop();
            q.push(tmp);
        }

        for (int i = 0; i < qsize; i++) {
            vector<int> tmp = heap.front();
            if (rotate == 0) { // y = x, x = -y
                int x = tmp[0];
                tmp[0] = -tmp[1];
                tmp[1] = x;
            }
            else if (rotate == 1) { // y = -y, x = -x
                tmp[0] = -tmp[0];
                tmp[1] = -tmp[1];
            }
            else if (rotate == 2) { // y = -x, x = y
                int x = tmp[0];
                tmp[0] = -tmp[1];
                tmp[1] = x;
            }
            heap.pop();
            heap.push(tmp);
        }
    }

    double check_nearest_obstacle() {
        vector<int> tmp = heap.top();
        return std::sqrt(tmp[0] * tmp[0] + tmp[1] * tmp[1]);
    }

};

class RadarSystem {
private:

public:
    void scan() {}
    void move() {}
    void rotate() {}
    double check_nearest_obstacle() {}
}