#include <iostream>
#include <vector>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> index_list;
        int size = nums.size();

        if (size < 2) {
            cout << "Invalid nums list";
            return index_list;
        }

        for (int j = 0; j < size; j++) {
            for (int i = j + 1; i < size; i++) {
                int sum = nums[j] + nums[i];
                if (sum == target) {
                    index_list.push_back(j);
                    index_list.push_back(i);
                    return index_list;
                }
            }
        }

        return index_list;
    }
};

int main(){
	
	vector<int> list = [1,2,3,6,8];
	int target = 9;
	Solution  sol;
	
	vector<int> result = sol.twosum(list, target);
	
	cout << result;	
	return 0;
}

